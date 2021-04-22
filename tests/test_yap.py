import copy
from pathlib import Path

import docspec_python
import pytest
import yaml

from tests import expected
import yapper


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
    # should work if valid path provided
    args = yapper.arg_parser.parse_args(['--config', './.yap_config.yaml'])
    yap_config = yapper.load_config(args)
    cross_check_config = yaml.load(open(config_path), Loader=yaml.SafeLoader)
    assert yap_config == cross_check_config


def test_process_config():
    # should raise if module_map not provided
    with pytest.raises(KeyError):
        yapper.process_config({})
    # should raise if invalid key provided
    with pytest.raises(KeyError):
        yapper.process_config({
            'boo': 'baa',
            'module_map': None
        })
    # should replace default keys with custom keys
    # use deep copies
    ytc = copy.deepcopy(yap_clean_config)
    for k in ytc.keys():
        yap_config = copy.deepcopy(ytc)
        yap_config['module_map'] = None
        yap_config[k] = 'boo'
        merged_config = yapper.process_config(yap_config)
        assert merged_config[k] == 'boo'
        for mk in merged_config.keys():
            if mk == k:
                assert merged_config[mk] != ytc[mk]
            else:
                assert merged_config[mk] == ytc[mk]


def test_parse():
    modules = docspec_python.load_python_modules(modules=['tests.mock_file'])
    for module in modules:
        # using the basic config
        lines = yapper.parser.parse('tests.mock_file', module, yap_clean_config)
        assert lines == expected.lines_default
        # using the custom config
        args = yapper.arg_parser.parse_args(['--config', './.yap_config.yaml'])
        yap_config = yapper.load_config(args)
        merged_config = yapper.process_config(yap_config)
        lines = yapper.parser.parse('tests.mock_file', module, merged_config)
        assert lines == expected.lines_custom


def test_main():
    # using the default config
    yap_config = copy.deepcopy(yap_clean_config)
    yap_config['module_map'] = {
        'tests.mock_file': 'mock_default_file.md'
    }
    print(yap_config)
    yapper.main(yap_config)
    # verify the output file
    with open('./mock_default_file.md') as md_file:
        assert md_file.read() == expected.md_file_default
    # using the custom yap_config
    args = yapper.arg_parser.parse_args(['--config', './.yap_config.yaml'])
    yap_config = yapper.load_config(args)
    merged_config = yapper.process_config(yap_config)
    yapper.main(merged_config)
    with open('./mock_custom_file.md') as md_file:
        assert md_file.read() == expected.md_file_custom
