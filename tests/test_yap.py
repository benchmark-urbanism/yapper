import ast
import copy
from pathlib import Path

import pytest
import toml

from yapper import handler, parser, runner

yapper_clean_config = copy.deepcopy(handler.yapper_template_config)


def test_load_config():
    # should raise if bad path provided
    with pytest.raises(ValueError):
        args = runner.arg_parser.parse_args(["--config", "/bad/path.boo"])
        handler.load_config(args)
    # should work if relative path provided
    args = runner.arg_parser.parse_args(["--config", "./tests/yap_config_basic.toml"])
    yap_config = handler.load_config(args)
    cross_check_config = toml.load(open("./tests/yap_config_basic.toml"))
    assert yap_config == cross_check_config['tool']['yapper']
    # should work if absolute path provided
    args = runner.arg_parser.parse_args(["--config", str(Path("./tests/yap_config_basic.toml").absolute())])
    yap_config = handler.load_config(args)
    cross_check_config = toml.load(open("./tests/yap_config_basic.toml"))
    assert yap_config == cross_check_config['tool']['yapper']


def test_process_config():
    # should raise if module_map not provided
    with pytest.raises(KeyError):
        handler.process_config({})
    # should raise if module map is not a list with items
    with pytest.raises(TypeError):
        handler.process_config({"module_map": None})
    with pytest.raises(TypeError):
        handler.process_config({"module_map": {}})
    with pytest.raises(TypeError):
        handler.process_config({"module_map": []})
    # should raise if a module_map entry's keys and values are not strings
    with pytest.raises(TypeError):
        handler.process_config({"module_map": [None]})
    # should raise if missing keys
    with pytest.raises(KeyError):
        handler.process_config({"module_map": [
            {
                "boo": "some.module",
                "py": "boo.py",
                "astro": "baa.astro"
            }]})
    with pytest.raises(KeyError):
        handler.process_config({"module_map": [
            {
                "module": "some.module",
                "boo": "boo.py",
                "astro": "baa.astro"
            }]})
    with pytest.raises(KeyError):
        handler.process_config({"module_map": [
            {
                "module": "some.module",
                "py": "boo.py",
                "boo": "baa.astro"
            }]})
    # should raise if py and astro files aren't strings with correct endings
    with pytest.raises(ValueError):
        handler.process_config({"module_map": [
            {
                "module": 'some.module',
                "py": "boo",
                "astro": "baa.astro"
            }]})
    with pytest.raises(ValueError):
        handler.process_config({"module_map": [
            {
                "module": 'some.module',
                "py": "boo.py",
                "astro": "baa"
            }]})
    # should raise if invalid key provided
    with pytest.raises(KeyError):
        handler.process_config({
            "boo": "baa",
            "module_map": [
            {
                "module": 'some.module',
                "py": "boo.py",
                "astro": "baa.astro"
            }]})
    # should replace default keys with custom keys
    # use deep copies
    for k in ["package_root_relative_path", "intro_template", "outro_template"]:
        yap_config = copy.deepcopy(yapper_clean_config)
        yap_config[k] = "boo"
        yap_config['module_map'] = [{
                "module": 'some.module',
                "py": "boo.py",
                "astro": "baa.astro"
            }]
        merged_config = handler.process_config(yap_config)
        assert merged_config[k] == "boo"


def test_parse():
    file_path = Path("./tests/comparisons/mock_file.py")
    mock_file = open(file_path)
    ast_module = ast.parse(mock_file.read())
    # using the basic config
    args = runner.arg_parser.parse_args(["--config", "./tests/yap_config_basic.toml"])
    yap_config_basic = handler.load_config(args)
    yap_config_basic = handler.process_config(yap_config_basic)
    astro = parser.parse(module_name="tests.mock_file", ast_module=ast_module, yap_config=yap_config_basic)
    with open('./tests/comparisons/generated_default.html', mode="w") as out_file:
        out_file.write(astro)
    with open("./tests/comparisons/expected_default.html") as expected_html:
        with open('./tests/comparisons/generated_default.html') as generated_html:
            assert generated_html.read().strip() == expected_html.read().strip()
    # using the custom config
    args = runner.arg_parser.parse_args(["--config", "./tests/yap_config_custom.toml"])
    yap_config_custom = handler.load_config(args)
    yap_config_custom = handler.process_config(yap_config_custom)
    astro = parser.parse(module_name="tests.mock_file", ast_module=ast_module, yap_config=yap_config_custom)
    with open('./tests/comparisons/generated_custom.html', mode="w") as out_file:
        out_file.write(astro)
    with open("./tests/comparisons/expected_custom.html") as expected_html:
        with open('./tests/comparisons/generated_custom.html') as generated_html:
            assert generated_html.read().strip() == expected_html.read().strip()


def test_main():
    # using the default config
    args = runner.arg_parser.parse_args(["--config", "./tests/yap_config_basic.toml"])
    yap_config = handler.load_config(args)
    merged_config = handler.process_config(yap_config)
    handler.main(merged_config)
    # verify the output file
    with open("./tests/comparisons/mock_default.astro") as astro_file:
        with open("./tests/comparisons/expected_default.astro") as expected_astro_file:
            assert astro_file.read().strip() == expected_astro_file.read().strip()
    # using the custom yap_config
    args = runner.arg_parser.parse_args(["--config", "./tests/yap_config_custom.toml"])
    yap_config = handler.load_config(args)
    merged_config = handler.process_config(yap_config)
    handler.main(merged_config)
    with open("./tests/comparisons/mock_custom.astro") as astro_file:
        with open("./tests/comparisons/expected_custom.astro") as expected_astro_file:
            assert astro_file.read().strip() == expected_astro_file.read().strip()
