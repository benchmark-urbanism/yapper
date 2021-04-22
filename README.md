# Yapper

Yapper converts Python docstrings to `markdown` for use by static site generators. It uses the [`docspec`](https://github.com/NiklasRosenstein/docspec).
- It is based on a simple-as-possible configuration file. These configuration parameters can be set to control selected styling and component templates for subsequent interpretation by downstream static site-generators.
- Linting and any other markdown processing is left to downstream workflows; for example, most IDEs have built-in linting and, if using the `markdown` for a static site generator, then any linting, linking, footnoting, emoticons, etc. can be handled by the respective `markdown` ecosystem. e.g. `remark` [plugins](https://github.com/remarkjs/remark/blob/main/doc/plugins.md) or similar.

> If you need to generate `MkDocs` or `Hugo` documentation then you may want to use the [`pydoc-markdown`](https://github.com/NiklasRosenstein/pydoc-markdown) package instead.

## Docstrings

`yapper` supports a simplified version of `numpy` docstring syntax:
- It recognises `Parameter`, `Returns`, `Yields`, and `Raises` headings;
- Types will be inferred automatically from signature typehints. Explicitly documented types within docstrings are (intentionally) *not* supported.
- Docstrings should otherwise use conventional `markdown` formatting, e.g. for tables or emphasis, and these will be passed-through into the generated `markdown` file.

For example:
```python
def mock_function(param_a: str, param_b: int = 1) -> int:
    """
    A mock function for testing purposes

    Parameters
    ----------
    param_a
        A *test* _param_.
    param_b
        Another *test* _param_.

        | col A |: col B |
        |=======|========|
        | boo   | baa    |
    """
    pass
```

Will be interpreted as:
````markdown
## mock\_function

```py
mock_function(param_a,
              param_b=1)
              -> int
```

A mock function for testing purposes

#### Parameters

**param_a** _str_: A *test* _param_.

**param_b** _int_: Another *test* _param_.

| col A |: col B |
|=======|========|
| boo   | baa    |
````

## Configuration

Configuration is provided in the form of a `.yap_config.yaml` file placed in the current directory, else a `--config` parameter can be provided with a relative filepath to the config file.

```bash
yapper --config ./my_config.yaml
```

Any parameter keys specified in the configuration file must match one of those available in the default configuration, which is as follows:

```python
yap_template_config = {
    'package_root_relative_path': '.',
    'frontmatter_template': None,
    'module_name_template': '# {module_name}\n\n',
    'toc_template': None,
    'function_name_template': '\n\n## {function_name}\n\n',
    'class_name_template': '\n\n## **class** {class_name}\n\n',
    'class_property_template': '\n\n#### {prop_name}\n\n',
    'signature_template': '\n\n```py\n{signature}\n```\n\n',
    'heading_template': '\n\n#### {heading}\n\n',
    'param_template': '\n\n**{name}** _{type}_: {description}\n\n',
    'return_template': '\n\n**{name}**: {description}\n\n',
    'module_map': None
}
```

When overriding a default config parameter, use `\n` for newlines and retain the same argument names for string interoplation (i.e curly brackets). For example, changing the heading template from a fourth-level to third-level markdown heading would look like this:

```yaml
heading_template: "\n\n### {heading}\n\n"
```

The configuration can be used to generate custom formatted markdown files that work for static site generators, and this is particularly useful when using custom `javascript` components from a static site generator such as `vuepress` / `vitepress` / `gridsome`, etc.

The `module_map` key is mandatory and specifies the python modules which should be processed by `yapper` mapped to the relative output filepath to which the generated `markdown` file will saved.

The following config:

```yaml
signature_template: "\n\n<FuncSignature>\n<pre>\n{signature}\n</pre>\n</FuncSignature>\n\n"
heading_template: "\n\n<FuncHeading>{heading}</FuncHeading>\n\n"
param_template: "\n\n<FuncElement name='{name}' type='{type}'>\n\n{description}\n\n</FuncElement>\n\n"
return_template: "\n\n<FuncElement name='{name}'>\n\n{description}\n\n</FuncElement>\n\n"
module_map:
  tests.mock_file: mock_custom_file.md
```

Would generate a `./mock_custom_file.md` file with the following markdown (for the same `mock_function` example shown above):
```markdown
## mock\_function

<FuncSignature>
<pre>
mock_function(param_a,
              param_b=1)
              -> int
</pre>
</FuncSignature>

A mock function for testing purposes

<FuncHeading>Parameters</FuncHeading>

<FuncElement name='param_a' type='str'>

A *test* _param_.

</FuncElement>

<FuncElement name='param_b' type='int'>

Another *test* _param_.

| col A |: col B |
|=======|========|
| boo   | baa    |

</FuncElement>
```

## Use from javascript

Many or most static site generators make use of javascript and the related ecosystem available from `npm` / `yarn` package managers.

As such, you may want to invoke `yapper` from a `package.json` file when building your documentation for development. This can be done with the help of `python-shell`. For example:

```js
const path = require('path')
const { PythonShell } = require('python-shell')

const options = {
  mode: 'text',
  pythonOptions: ['-u'],
  pythonPath: path.resolve(__dirname, '../venv/bin/python'),
  scriptPath: path.resolve(__dirname, '../venv/lib/python3.9/site-packages/yapper'),
  args: ['--config', '../.yap_config.yaml'],
}

PythonShell.run('__init__.py', options, function (err) {
  if (err) throw err
})

```

`yapper` can then be invoked from `node` or the `package.json` file's scripts parameter, and can be coupled to other steps such as linting or validation, e.g.
```json
{
  "scripts": {
    "generate": "node generateDocs.js",
    "lint": "markdownlint 'content/**/*.md' --fix",
    "validateLinks": "remark -u validate-links ."
  }
}
```