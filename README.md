# Yapper

Yapper converts Python docstrings to `astro` files for use by the [Astro](https://astro.build/) static site generator.

It uses [`griffe`](https://github.com/mkdocstrings/griffe) to parse python modules and extracts numpy style docstrings.

It is up to the user to maintain consistency between types specified in signatures and docstrings. Differences betweten the two can be preferable where docstrings represent simplified forms of typing information than might otherwise be necessary for function signatures.

Docstrings and parameter descriptions will be passed through as a raw markdown wrapped in the Astro `<Markdown is:raw></Markdown>` elements.

Class and function elements are wrapped with `html` with `css` classes that can be styled from Astro.

> See the `cityseer.benchmarkurbanism.com` documentation site and associated [docs repo](https://github.com/benchmark-urbanism/cityseer-api/tree/master/docs) for a working example.

Conversion of markdown formatting, code blocks, admonitions, etc., is all handled downstream by Astro. Styling is likewise handled downstream via `css` targeting the associated element classes.

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
import { Markdown } from 'astro/components';\n
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
import { Markdown } from 'astro/components';\n
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
