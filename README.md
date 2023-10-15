# Yapper

> This package is deprecated and is no longer maintained.

Yapper converts Python docstrings to `astro` files for use by the [Astro](https://astro.build/) static site generator.

It uses [`griffe`](https://github.com/mkdocstrings/griffe) to parse python modules and extracts numpy style docstrings.

Types will be inferred from docstrings. Warnings will be logged if types specified in docstrings don't match those specified in function signatures.

Docstrings and parameter descriptions will be parsed using [markdown-it-py](https://markdown-it-py.readthedocs.io/en/latest/).

Class and function elements are wrapped with `html` with `css` classes that can be styled from Astro.

> See the `cityseer.benchmarkurbanism.com` documentation site and associated [docs repo](https://github.com/benchmark-urbanism/cityseer-api/tree/master/docs) for a working example.

## Configuration

Configuration is provided in `pyproject.toml` file placed in the current directory, else a `--config` parameter can be provided with a relative or absolute filepath to a `toml` config file.

```bash
yapper --config ./custom_config.toml
```

The `toml` file must include a `[tool.yapper]` section, with keys corresponding to the default configuration options:

```toml
[tool.yapper]
package_root_relative_path = './'
intro_template = """
---\n
---\n
"""
outro_template = ""
module_map = [
  { module = "test.mock_file", astro = "./tests/mock_default.astro" },
]
```

If you want to wrap the `.astro` output in a particular layout, then set the `intro_template` and `outro_template` accordingly, for example, the following will import the `PageLayout` layout and will wrap the generated content accordingly:

```toml
[tool.yapper]
package_root_relative_path = './'
intro_template = """
---\n
import PageLayout from '../layouts/PageLayout.astro'\n
---\n
\n
<PageLayout>
"""
outro_template = """
</PageLayout>\n
"""
module_map = [
  { module = "test.mock_file", py = "./tests/mock_file.py", astro = "./tests/mock_default.astro" },
]
```

The `module_map` is mandatory and specifies the names of the python modules to be processed via the `module` key and an `astro` key corresponding to the output file:

## Development

`yapper` uses a `pyproject.toml` file to specify project dependencies and scripts related to project development and publishing.

See `pyproject.toml` for available scripts.
