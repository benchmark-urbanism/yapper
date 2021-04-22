"""
Uses docspec to parse docstrings to markdown.

Intended for use with static site generators where further linting / linking / styling is done downstream.

Loosely based on Numpy-style docstrings.

Automatically infers types from signature typehints. Explicitly documented types are NOT supported in docstrings.
"""
import argparse
import logging
from pathlib import Path
import sys

import docspec_python
import yaml

from yapper import parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# prepare args
arg_parser = argparse.ArgumentParser(description='Load YAML configuration file for yapper.')
arg_parser.add_argument('--config',
                        type=str,
                        help='Relative file path to the configuration file.',
                        default=None,
                        required=False)
# template configs
yap_template_config = {
    'package_root_relative_path': '.',
    'frontmatter_template': None,
    'module_name_template': '# {module_name}\n\n',
    'toc_template': None,
    'function_name_template': '\n\n## {function_name}\n\n',
    'class_name_template': '\n\n## **class** {class_name}\n\n',
    'class_property_template': '\n\n#### {prop_name}\n\n',
    'signature_template': '\n\n```py\n{signature}\n```\n\n',
    'heading_template': '\n\n#### {heading}\n\n',
    'param_template': '\n\n**{name}** _{type}_: {description}\n\n',
    'return_template': '\n\n**{name}**: {description}\n\n',
    'module_map': None
}


def load_config(args: argparse.Namespace) -> dict:
    logger.info('Parsing config.')
    file_name = None
    if hasattr(args, 'config'):
        file_name = args.config
    if file_name is None:
        for name in ('.yap_config.yaml', '.yap_config.yml'):
            fp = Path(Path.cwd() / name)
            if fp.exists():
                file_name = name
                break
    if file_name is None or not Path(Path.cwd() / file_name).exists():
        raise ValueError('Yapper requires either a "--config" command-line parameter with a valid relative filepath '
                         'as an argument, else a ".yap_config.yaml" file should be placed in the current directory.')
    file_path = Path(Path.cwd() / file_name)
    logger.info(f'Loading yapper config from {file_path}')
    return yaml.load(open(file_path), Loader=yaml.SafeLoader)


def process_config(yap_config: dict) -> dict:
    if 'module_map' not in yap_config:
        raise KeyError('The configuration file requires a dictionary mapping modules to output paths for markdown.')
    # check for invalid keys
    for k in yap_config.keys():
        if k not in yap_template_config:
            raise KeyError(f'Config file key: {k} is not a valid configuration setting.')
    # override defaults from config file
    for def_key in yap_template_config.keys():
        if def_key in yap_config:
            yap_template_config[def_key] = yap_config[def_key]
    return yap_template_config


def main(yap_config: dict) -> None:
    # check and add package root path if spec'd in config
    # this should only be necessary if the script is placed somewhere other than the package root
    if 'package_root_relative_path' in yap_config:
        package_path = str(Path(Path.cwd() / yap_config['package_root_relative_path']))
        logger.info(f'Adding {package_path} to Python paths')
        sys.path.append(package_path)
    # parse the module / doc path pairs
    for module_name, doc_path in yap_config['module_map'].items():
        logger.info(f'Processing {module_name} to {doc_path}')
        # process the module
        modules = docspec_python.load_python_modules(modules=[module_name])
        for module in modules:
            lines = parser.parse(module_name, module, yap_config)
            # create the path and output directories as needed
            out_file = Path(doc_path)
            out_file.parent.mkdir(parents=True, exist_ok=True)
            # write!
            with open(out_file, mode='w') as out_file:
                for line in lines:
                    out_file.write(line)


if __name__ == '__main__':
    args = arg_parser.parse_args()
    config_file = load_config(args)
    yap_config = process_config(config_file)
    # call main function
    main(yap_config)
