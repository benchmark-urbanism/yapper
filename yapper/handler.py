#!python
import ast
import argparse
import logging
from pathlib import Path
import sys

import yaml

from yapper import parser


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# template configs
yap_template_config = {
    'package_root_relative_path': '.',
    'intro_template': None,
    'outro_template': None,
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
    if file_name is None:
        raise ValueError('Yapper requires either a "--config" command-line parameter with a valid relative filepath '
                         'as an argument, else a ".yap_config.yaml" file should be placed in the current directory.')
    if Path(file_name).is_absolute():
        file_path = Path(file_name)
    else:
        file_path = Path(Path.cwd() / file_name)
    if not file_path.exists():
        raise ValueError(f'Config file path of {file_path} does not exist.')
    logger.info(f'Loading yapper config from {file_path}')
    return yaml.load(open(file_path), Loader=yaml.SafeLoader)


def process_config(yap_config: dict) -> dict:
    if 'module_map' not in yap_config:
        raise KeyError('The configuration file requires a "module_map" key.')
    if not isinstance(yap_config['module_map'], dict) or not len(yap_config['module_map'].keys()):
        raise TypeError('The "module_map" key should be a "dict" type '
                        'containing "str" keys consisting of a module names '
                        'pointing to "dict" values with "py" and "astro" keys '
                        'corresponding to input and output filepaths.')
    for module_name, module_paths in yap_config['module_map'].items():
        if not isinstance(module_paths, dict):
            raise TypeError('Module names must correspond to values of type "dict".')
        if 'py' not in module_paths.keys():
            raise KeyError('Module paths must contain a "py" key with the path to a python file for parsing.')
        if 'astro' not in module_paths.keys():
            raise KeyError('Module paths must contain an "astro" key with a destination path for the parsed content.')
        py_path = module_paths['py']
        astro_path = module_paths['astro']
        if not py_path.endswith('.py'):
            raise ValueError(f'Expecting a python input file type ending in ".py" but encountered "{py_path}"')
        if not astro_path.endswith('.astro'):
            raise ValueError(f'Expecting an astro output file type ending in ".astro" but encountered "{astro_path}"')
    # check for invalid keys
    for k in yap_config.keys():
        if k not in yap_template_config:
            raise KeyError(f'Config file key: {k} is not a valid configuration key.')
    # override defaults from config file
    merged_config = {}
    for def_key in yap_template_config.keys():
        if def_key in yap_config:
            merged_config[def_key] = yap_config[def_key]
        else:
            merged_config[def_key] = yap_template_config[def_key]

    return merged_config


def main(yap_config: dict) -> None:
    """ """
    yap_config = process_config(yap_config)
    # check and add package root path if spec'd in config
    # this should only be necessary if the script is placed somewhere other than the package root
    if 'package_root_relative_path' in yap_config:
        package_path = Path(Path.cwd() / yap_config['package_root_relative_path'])
    else:
        package_path = Path.cwd()
    logger.info(f'Adding {package_path} to Python paths')
    sys.path.append(str(package_path))
    # parse the modules
    for module_name, module_paths in yap_config['module_map'].items():
        py_path = module_paths['py']
        astro_path = module_paths['astro']
        in_path = Path(package_path / py_path)
        out_path = Path(package_path / astro_path)
        logger.info(f'Processing {in_path} to {out_path}')
        # process the module
        ast_module = ast.parse(open(in_path).read())
        astro = parser.parse(module_name=module_name,
                             ast_module=ast_module,
                             yap_config=yap_config)
        # create the path and output directories as needed
        out_file = Path(out_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        # write!
        with open(out_file, mode='w') as out_file:
            out_file.write(astro)
