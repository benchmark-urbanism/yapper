import ast
import copy
import importlib
from pathlib import Path

import pytest
import toml

from yapper import cli, handler, parser

yapper_clean_config = copy.deepcopy(handler.yapper_template_config)


def test_load_config():
    # should raise if bad path provided
    with pytest.raises(ValueError):
        args = cli.arg_parser.parse_args(["--config", "/bad/path.boo"])
        handler.load_config(args)
    # should raise if pyproject.toml is missing a [tool.yapper] section.
    # misses tool section in TOML
    args = cli.arg_parser.parse_args(["--config", "./tests/yap_config_bad_A.toml"])
    with pytest.raises(KeyError):
        yapper_config = handler.load_config(args)
    # misses yapper section in TOML
    args = cli.arg_parser.parse_args(["--config", "./tests/yap_config_bad_B.toml"])
    with pytest.raises(KeyError):
        yapper_config = handler.load_config(args)
    # should work if relative path provided
    args = cli.arg_parser.parse_args(["--config", "./tests/yap_config_basic.toml"])
    yapper_config = handler.load_config(args)
    cross_check_config = toml.load(open("./tests/yap_config_basic.toml"))
    assert yapper_config == cross_check_config["tool"]["yapper"]
    # should work if absolute path provided
    args = cli.arg_parser.parse_args(["--config", str(Path("./tests/yap_config_basic.toml").absolute())])
    yapper_config = handler.load_config(args)
    cross_check_config = toml.load(open("./tests/yap_config_basic.toml"))
    assert yapper_config == cross_check_config["tool"]["yapper"]


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
        handler.process_config({"module_map": [{"boo": "some.module", "py": "boo.py", "astro": "baa.astro"}]})
    with pytest.raises(KeyError):
        handler.process_config({"module_map": [{"module": "some.module", "boo": "boo.py", "astro": "baa.astro"}]})
    with pytest.raises(KeyError):
        handler.process_config({"module_map": [{"module": "some.module", "py": "boo.py", "boo": "baa.astro"}]})
    # should raise if py and astro files aren't strings with correct endings
    with pytest.raises(ValueError):
        handler.process_config({"module_map": [{"module": "some.module", "py": "boo", "astro": "baa.astro"}]})
    with pytest.raises(ValueError):
        handler.process_config({"module_map": [{"module": "some.module", "py": "boo.py", "astro": "baa"}]})
    # should raise if invalid key provided
    with pytest.raises(KeyError):
        handler.process_config(
            {"boo": "baa", "module_map": [{"module": "some.module", "py": "boo.py", "astro": "baa.astro"}]}
        )
    # should replace default keys with custom keys
    # use deep copies
    for k in ["package_root_relative_path", "intro_template", "outro_template"]:
        yapper_config = copy.deepcopy(yapper_clean_config)
        yapper_config[k] = "boo"
        yapper_config["module_map"] = [{"module": "some.module", "py": "boo.py", "astro": "baa.astro"}]
        merged_config = handler.process_config(yapper_config)
        assert merged_config[k] == "boo"


def test_parse():
    file_path = Path("./tests/comparisons/mock_file.py")
    mock_file = open(file_path)
    ast_module = ast.parse(mock_file.read())
    # using the basic config
    args_basic = cli.arg_parser.parse_args(["--config", "./tests/yap_config_basic.toml"])
    yapper_config_basic = handler.load_config(args_basic)
    yapper_config_basic = handler.process_config(yapper_config_basic)
    module_content = importlib.import_module("tests.comparisons.mock_file")
    astro = parser.parse(
        module_name="tests.comparisons.mock_file",
        module_content=module_content,
        ast_module=ast_module,
        yapper_config=yapper_config_basic,
    )
    with open("./tests/comparisons/generated_default.html", mode="w") as out_file:
        out_file.write(astro)
    with open("./tests/comparisons/expected_default.html") as expected_html:
        with open("./tests/comparisons/generated_default.html") as generated_html:
            assert generated_html.read().strip() == expected_html.read().strip()
    # using the custom config
    args_custom = cli.arg_parser.parse_args(["--config", "./tests/yap_config_custom.toml"])
    yapper_config_custom = handler.load_config(args_custom)
    yapper_config_custom = handler.process_config(yapper_config_custom)
    module_content = importlib.import_module("tests.comparisons.mock_file")
    astro = parser.parse(
        module_name="tests.comparisons.mock_file",
        module_content=module_content,
        ast_module=ast_module,
        yapper_config=yapper_config_custom,
    )
    with open("./tests/comparisons/generated_custom.html", mode="w") as out_file:
        out_file.write(astro)
    with open("./tests/comparisons/expected_custom.html") as expected_html:
        with open("./tests/comparisons/generated_custom.html") as generated_html:
            assert generated_html.read().strip() == expected_html.read().strip()


def test_main():
    # using the default config
    args_basic = cli.arg_parser.parse_args(["--config", "./tests/yap_config_basic.toml"])
    yapper_config_basic = handler.load_config(args_basic)
    yapper_config_basic = handler.process_config(yapper_config_basic)
    handler.main(yapper_config_basic)
    # verify the output file
    with open("./tests/comparisons/mock_default.astro") as astro_file:
        with open("./tests/comparisons/expected_default.astro") as expected_astro_file:
            assert astro_file.read().strip() == expected_astro_file.read().strip()
    # using the custom yapper_config
    args_custom = cli.arg_parser.parse_args(["--config", "./tests/yap_config_custom.toml"])
    yapper_config_custom = handler.load_config(args_custom)
    yapper_config_custom = handler.process_config(yapper_config_custom)
    handler.main(yapper_config_custom)
    with open("./tests/comparisons/mock_custom.astro") as astro_file:
        with open("./tests/comparisons/expected_custom.astro") as expected_astro_file:
            assert astro_file.read().strip() == expected_astro_file.read().strip()
