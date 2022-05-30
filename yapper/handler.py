#!python
"""
Yapper logic for loading and processing the config, and for using the config to parse docstrings to astro files.
"""

import argparse
import ast
import copy
import importlib
import logging
import sys
from pathlib import Path

import toml

from yapper import YapperConfig, parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# template configs
yapper_template_config: YapperConfig = {
    "package_root_relative_path": "./",
    "intro_template": "---\n\nimport { Markdown } from 'astro/components';\n\n---\n\n",
    "outro_template": "",
    "module_map": [],
}


def load_config(args: argparse.Namespace) -> YapperConfig:
    """Load the yapper configuration from a .toml file."""
    logger.info("Parsing config.")
    file_name = None
    if hasattr(args, "config"):
        file_name = args.config
    if file_name is None:
        candidate_filepath = Path(Path.cwd() / "pyproject.toml")
        if candidate_filepath.exists():
            file_name = "pyproject.toml"
    if file_name is None:
        raise ValueError(
            'Yapper requires either a "--config" command-line parameter with a valid relative or absolute '
            'filepath as an argument, else a "pyproject.toml" file in the current directory.'
        )
    if Path(file_name).is_absolute():
        file_path = Path(file_name)
    else:
        file_path = Path(Path.cwd() / file_name)
    if not file_path.exists():
        raise ValueError(f"Config file path of {file_path} does not exist.")
    logger.info(f"Loading yapper config from {file_path}")
    with open(file_path) as config:
        py_config = toml.load(config)
    if "tool" not in py_config or "yapper" not in py_config["tool"]:
        logger.info(
            "Yapper requires a [tool.yapper] section in pyproject.toml. "
            "Please refer to the yapper documentation for more information."
        )
    yapper_config = py_config["tool"]["yapper"]

    return yapper_config


def process_config(yapper_config: YapperConfig) -> YapperConfig:
    """Validate and prepares a yapper config for downstream use."""
    err_msg = """
    The "module_map" should consist of an array of inline tables. 
    Each inline table should contain: 
    - a "module" key with the module name; 
    - a "py" key with the filepath to the input Python file; 
    - an "astro" key with output filepath for the astro file.
    """
    if "module_map" not in yapper_config:
        raise KeyError('The configuration file requires a "module_map" key.')
    if not isinstance(yapper_config["module_map"], list) or not yapper_config["module_map"]:  # type: ignore
        raise TypeError(err_msg)
    for module_info in yapper_config["module_map"]:
        if not isinstance(module_info, dict):  # type: ignore
            raise TypeError(err_msg)
        if "module" not in module_info.keys():
            raise KeyError(err_msg)
        if "py" not in module_info.keys():
            raise KeyError(err_msg)
        if "astro" not in module_info.keys():
            raise KeyError(err_msg)
        py_path = module_info["py"]
        astro_path = module_info["astro"]
        if not py_path.endswith(".py"):
            raise ValueError(f'Expecting a python input file type ending in ".py" but encountered "{py_path}"')
        if not astro_path.endswith(".astro"):
            raise ValueError(f'Expecting an astro output file type ending in ".astro" but encountered "{astro_path}"')
    # check for invalid keys
    for key in yapper_config.keys():
        if key not in yapper_template_config:
            raise KeyError(f"Config file key: {key} is not a valid configuration key.")
    # override defaults from config file
    merged_config: YapperConfig = copy.deepcopy(yapper_template_config)
    for config_key in merged_config.keys():
        if config_key in yapper_config:
            merged_config[config_key] = yapper_config[config_key]

    return merged_config


def main(yapper_config: YapperConfig) -> None:
    """Use a yapper config to parse docstrings from a python file to an astro output file."""
    yapper_config = process_config(yapper_config)
    # check and add package root path if spec'd in config
    # this should only be necessary if the script is placed somewhere other than the package root
    if "package_root_relative_path" in yapper_config:
        config_path: str = yapper_config["package_root_relative_path"]
        package_path = Path(Path.cwd() / config_path)
    else:
        package_path = Path.cwd()
    logger.info(f"Adding {package_path} to Python paths")
    sys.path.append(str(package_path))
    # parse the modules
    for module_info in yapper_config["module_map"]:
        py_path = module_info["py"]
        in_path = Path(package_path / py_path)
        astro_path = module_info["astro"]
        out_path = Path(package_path / astro_path)
        logger.info(f"Processing {in_path} to {out_path}")
        # get the module name
        module_name = module_info["module"]
        module_content = importlib.import_module(module_name)
        # process the module to AST
        with open(in_path) as py_file:
            ast_module = ast.parse(py_file.read())
        # parse
        astro = parser.parse(  # type: ignore
            module_name=module_name, module_content=module_content, ast_module=ast_module, yapper_config=yapper_config
        )
        # create the path and output directories as needed
        astro_path = Path(out_path)
        astro_path.parent.mkdir(parents=True, exist_ok=True)
        # write!
        with open(astro_path.absolute(), mode="w") as out_file:
            out_file.write(astro)
