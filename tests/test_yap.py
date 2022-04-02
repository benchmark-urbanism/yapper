import ast
import copy
from pathlib import Path

import pytest
import yaml

import yapper
from tests import expected

yap_clean_config = copy.deepcopy(yapper.yap_template_config)


def test_load_config():
    # should raise if bad path provided
    with pytest.raises(ValueError):
        args = yapper.arg_parser.parse_args(['--config', '/bad/path.boo'])
        yapper.load_config(args)
    # should raise if no path provided and no valid files found in working directory
    with pytest.raises(ValueError):
        # temporarily rename .yap_config.yaml so that it is not found
        config_path = Path(Path.cwd() / './.yap_config.yaml')
        temp_path = config_path.rename('.yap_config.temp')
        args = yapper.arg_parser.parse_args([])
        yapper.load_config(args)
    # reset path
    temp_path.rename('.yap_config.yaml')
    # should work if relative path provided
    args = yapper.arg_parser.parse_args(['--config', './.yap_config.yaml'])
    yap_config = yapper.load_config(args)
    cross_check_config = yaml.load(open(config_path), Loader=yaml.SafeLoader)
    assert yap_config == cross_check_config
    # should work if absolute path provided
    args = yapper.arg_parser.parse_args(['--config', str(Path('./.yap_config.yaml').absolute())])
    yap_config = yapper.load_config(args)
    cross_check_config = yaml.load(open(config_path), Loader=yaml.SafeLoader)
    assert yap_config == cross_check_config


def test_process_config():
    # should raise if module_map not provided
    with pytest.raises(KeyError):
        yapper.process_config({})
    # should raise if module map is not a dictionary or an empty dict
    with pytest.raises(TypeError):
        yapper.process_config({'module_map': None})
    with pytest.raises(TypeError):
        yapper.process_config({'module_map': {}})
    # should raise if keys are not strings or values are not dicts
    with pytest.raises(KeyError):
        yapper.process_config({
            'boo': 'baa',
            0: {
                'some.module': {
                    'py': 'boo.py',
                    'astro': 'baa.astro'
                }
            }
        })
    with pytest.raises(TypeError):
        yapper.process_config({
            'boo': 'baa',
            'module_map': {
                'some.module': 'not a dict'
            }
        })
    # should raise if py or astro keys are missing
    with pytest.raises(KeyError):
        yapper.process_config({
            'boo': 'baa',
            'module_map': {
                'some.module': {
                    '-': 'boo.py',
                    'astro': 'baa.astro'
                }
            }
        })
    with pytest.raises(KeyError):
        yapper.process_config({
            'boo': 'baa',
            'module_map': {
                'some.module': {
                    'py': 'boo.py',
                    '-': 'baa.astro'
                }
            }
        })
    # should raise if file endings are not valid
    with pytest.raises(ValueError):
        yapper.process_config({
            'boo': 'baa',
            'module_map': {
                'some.module': {
                    'py': 'boo',
                    'astro': 'baa.astro'
                }
            }
        })
    with pytest.raises(ValueError):
        yapper.process_config({
            'boo': 'baa',
            'module_map': {
                'some.module': {
                    'py': 'boo.py',
                    'astro': 'baa'
                }
            }
        })
    # should raise if invalid key provided
    with pytest.raises(KeyError):
        yapper.process_config({
            'boo': 'baa',
            'module_map': {
                'some.module': {
                    'py': 'boo.py',
                    'astro': 'baa.astro'
                }
            }
        })
    # should replace default keys with custom keys
    # use deep copies
    config_template = {
        'package_root_relative_path': '.',
        'intro_template': None,
        'outro_template': None,
        'module_map': {
            'some.module': {
                'py': 'boo.py',
                'astro': 'baa.astro'
            }
        }
    }
    for k in ['package_root_relative_path', 'intro_template', 'outro_template']:
        yap_config = copy.deepcopy(config_template)
        yap_config[k] = 'boo'
        merged_config = yapper.process_config(yap_config)
        assert merged_config[k] == 'boo'


def test_parse():
    file_path = Path('../tests/mock_file.py')
    mock_file = open(file_path)
    ast_module = ast.parse(mock_file.read())
    # using the basic config
    astro = yapper.parser.parse(module_name='tests.mock_file',
                                ast_module=ast_module,
                                yap_config=yap_clean_config)
    assert astro.strip() == expected.lines_default.strip()
    # using the custom config
    args = yapper.arg_parser.parse_args(['--config', './.yap_config_custom.yaml'])
    yap_config = yapper.load_config(args)
    merged_config = yapper.process_config(yap_config)
    astro = yapper.parser.parse(module_name='tests.mock_file',
                                ast_module=ast_module,
                                yap_config=merged_config)
    assert astro.strip() == expected.lines_custom.strip()


def test_main():
    # using the default config
    args = yapper.arg_parser.parse_args(['--config', './.yap_config_basic.yaml'])
    yap_config = yapper.load_config(args)
    merged_config = yapper.process_config(yap_config)
    yapper.main(merged_config)
    # verify the output file
    with open('mock_basic_file.astro') as astro_file:
        assert astro_file.read().strip() == expected.astro_file_default.strip()
    # using the custom yap_config
    args = yapper.arg_parser.parse_args(['--config', './.yap_config_custom.yaml'])
    yap_config = yapper.load_config(args)
    merged_config = yapper.process_config(yap_config)
    yapper.main(merged_config)
    with open('mock_custom_file.astro') as astro_file:
        assert astro_file.read().strip() == expected.astro_file_custom.strip()
