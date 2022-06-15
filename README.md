# Yapper

Yapper converts Python docstrings to `astro` files for use by the [Astro](https://astro.build/) static site generator.

It uses the `ast` module to parse class and function signatures and uses [`docstring_parser`](https://github.com/rr-/docstring_parser) to parse docstrings, which is compatible with several common docstring styles such as `google` and `numpy`.

Types will be inferred from docstrings. Warnings will be logged if types specified in docstrings don't match those specified in function signatures.

Docstrings and parameter descriptions will be passed through as a raw markdown wrapped in the Astro `<Markdown is:raw></Markdown>` elements.

Class and function elements are wrapped with `html` with `css` classes that can be styled from Astro.

> See the `cityseer.benchmarkurbanism.com` documentation site and associated [docs repo](https://github.com/benchmark-urbanism/cityseer-api/tree/master/docs) for a working example.

For example:

````python
def mock_function(param_a: int) -> str:
    """
    A mock function returning a sum of param_a and param_b if positive numbers, else None

    Parameters
    ----------
    param_a: int
        A *test* _param_.

    Returns
    -------
    scare: str
        Boo

    Notes
    -----
    ```python
    print(mock_function(1))
    # returns "boo"
    ```
    """
    return 'boo'
````

Will be interpreted as:

````html
---
import { Markdown } from 'astro/components';
---

<div class="yap module">
  <h1 class="yap module-title" id="test-mock-file">
    <a aria-hidden="true" href="#test-mock-file" tabindex="-1">
      <svg
        aria-hidden="true"
        class="heading-icon"
        height="15px"
        viewBox="0 0 20 20"
        width="15px"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          clip-rule="evenodd"
          d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
"
          fill-rule="evenodd"
        ></path>
      </svg> </a
    >test.mock_file
  </h1>
  <Markdown is:raw> </Markdown>
  <section class="yap func">
    <h2 class="yap func-title" id="mock-function">
      <a aria-hidden="true" href="#mock-function" tabindex="-1">
        <svg
          aria-hidden="true"
          class="heading-icon"
          height="15px"
          viewBox="0 0 20 20"
          width="15px"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            clip-rule="evenodd"
            d="
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
"
            fill-rule="evenodd"
          ></path>
        </svg> </a
      >mock_function
    </h2>
    <div class="yap func-sig-content">
      <div class="yap func-sig">
        <span>mock_function(</span>
        <div class="yap func-sig-params">
          <div class="yap func-sig-param">param_a)</div>
        </div>
      </div>
    </div>
    <div class="yap">
      <Markdown is:raw>
        A mock function returning a sum of param_a and param_b if positive
        numbers, else None
      </Markdown>
      <h3 class="yap">Parameters</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">param_a</div>
          <div class="yap doc-str-elem-type">int</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown is:raw> A *test* _param_. </Markdown>
        </div>
      </div>
      <h3 class="yap">Returns</h3>
      <div class="yap doc-str-elem-container">
        <div class="yap doc-str-elem-def">
          <div class="yap doc-str-elem-name">scare</div>
          <div class="yap doc-str-elem-type">str</div>
        </div>
        <div class="yap doc-str-elem-desc">
          <Markdown is:raw> Boo </Markdown>
        </div>
      </div>
      <div class="yap doc-str-meta">
        <h3 class="yap">Notes</h3>
        <Markdown is:raw>
          ```python print(mock_function(1)) # returns &quot;boo&quot; ```
        </Markdown>
      </div>
    </div>
  </section>
</div>
````

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
  { module = "test.mock_file", py = "./tests/mock_file.py", astro = "./tests/mock_default.astro" },
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

The `module_map` is mandatory and specifies the names of the python modules to be processed via the `module` key, the `py` key mapping to the input file, and an `astro` key corresponding to the output file:

## Development

`yapper` uses a `pyprojct.toml` file to specify project dependencies and scripts related to project development and publishing.

See `pyproject.toml` for available scripts.
