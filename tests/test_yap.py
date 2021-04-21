import argparse
import copy
from pathlib import Path

import pytest
from pytest import fixture
import yaml

from yapper import arg_parser, yap_template_config, load_config, process_config, main


def test_load_config():
    # should raise if bad path provided
    with pytest.raises(ValueError):
        args = arg_parser.parse_args(['--config', '/bad/path.boo'])
        load_config(args)
    # should raise if no path provided and no valid files found in working directory
    with pytest.raises(ValueError):
        # temporarily rename .yap_config.yaml so that it is not found
        config_path = Path(Path.cwd() / './.yap_config.yaml')
        temp_path = config_path.rename('.yap_config.temp')
        args = arg_parser.parse_args([])
        load_config(args)
    # reset path
    temp_path.rename('.yap_config.yaml')
    # should work if valid path provided
    args = arg_parser.parse_args(['--config', './.yap_config.yaml'])
    config = load_config(args)
    cross_check_config = yaml.load(open(config_path), Loader=yaml.SafeLoader)
    assert config == cross_check_config


def test_process_config():
    # should raise if module_map not provided
    with pytest.raises(KeyError):
        process_config({})
    # should raise if invalid key provided
    with pytest.raises(KeyError):
        process_config({
            'boo': 'baa',
            'module_map': None
        })
    # should replace default keys with custom keys
    # use deep copies
    ytc = copy.deepcopy(yap_template_config)
    for k in yap_template_config.keys():
        config = copy.deepcopy(ytc)
        config['module_map'] = None
        config[k] = 'boo'
        merged_config = process_config(config)
        assert merged_config[k] == 'boo'
        for mk in merged_config.keys():
            if mk == k:
                assert merged_config[mk] != ytc[mk]
            else:
                assert merged_config[mk] == ytc[mk]

def test_main():
    pass