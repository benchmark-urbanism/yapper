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
    'frontmatter_template': None,
    'module_name_template': '# {module_name}\n\n',
    'toc_template': None,
    'function_name_template': '\n\n## {function_name}\n\n',
    'class_name_template': '\n\n## **class** {class_name}\n\n',
    'class_property_template': '\n\n#### {prop_name}\n\n',
    'signature_template': '\n\n```py\n{signature}\n```\n\n',
    'heading_template': '\n\n#### {heading}\n\n',
    'param_template': '\n\n**{name}** _{type}_: {description}\n\n',
    'return_template': '\n\n**{name}**: {description}\n\n'
}


def load_config(args: argparse.Namespace) -> dict:
    """

    Parameters
    ----------
    args

    Returns
    -------
    config_file
    """
    logger.info('Parsing config.')
    file_name = None
    if hasattr(args, 'config'):
        file_name = args.config
    if file_name is None:
        for name in ('.yap_config.yaml', '.yap_config.yml'):
            fp = Path(Path.cwd() / name)
            if fp.exists():
                file_name = name
    if file_name is None or not Path(Path.cwd() / file_name).exists():
        raise ValueError('Yapper requires either a "--config" command-line parameter with a valid relative filepath '
                         'as an argument, else a ".yap_config.yaml" file should be placed in the current directory.')
    file_path = Path(Path.cwd() / file_name)
    return yaml.load(open(file_path), Loader=yaml.SafeLoader)


def process_config(config_file: dict) -> dict:
    """

    Parameters
    ----------
    config_file

    Returns
    -------
    yap_config
    """
    if 'module_map' not in config_file:
        raise KeyError('The configuration file requires a dictionary mapping modules to output paths for markdown.')
    # check for invalid keys
    for k in config_file.keys():
        if k not in yap_template_config and k != 'module_map':
            raise KeyError(f'Config file key: {k} is not a valid configuration setting.')
    # override defaults from config file
    for def_key in yap_template_config.keys():
        if def_key in config_file:
            yap_template_config[def_key] = config_file[def_key]
    return yap_template_config


def main(args) -> None:
    """
    Parameters
    ----------
    args:
    """
    config_file = load_config(args)
    yap_config = process_config(config_file)
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
    # call main function
    main(args)
