from __future__ import annotations

import importlib
import re
from pathlib import Path

import docstring_parser
from dominate import tags, util
from pdoc import doc, markdown2, render, render_helpers
from pygments.formatters import HtmlFormatter

formatter = HtmlFormatter(
    cssclass="pdoc-code codehilite",
    linenos="inline",
    anchorlinenos=True,
)
markdown_extensions = {
    "code-friendly": None,
    "cuddled-lists": None,
    "fenced-code-blocks": {"cssclass": formatter.cssclass},
    "footnotes": None,
    "header-ids": None,
    "link-patterns": None,
    "markdown-in-html": None,
    "mermaid": None,
    "pyshell": None,
    "strike": None,
    "tables": None,
    "task_list": None,
    "toc": {"depth": 2},
}
markdown_link_patterns = [
    (
        re.compile(
            r"""
            \b
            (
                (?:https?://|(?<!//)www\.)    # prefix - https:// or www.
                \w[\w_\-]*(?:\.\w[\w_\-]*)*   # host
                [^<>\s"']*                    # rest of url
                (?<![?!.,:*_~);])             # exclude trailing punctuation
                (?=[?!.,:*_~);]?(?:[<\s]|$))  # make sure that we're not followed by " or ', i.e. we're outside of href="...".
            )
        """,
            re.X,
        ),
        r"\1",
    )
]


def add_heading(doc_str_frag: tags.div | tags.section, heading: str) -> tags.div | tags.section:
    """Add a heading."""
    with doc_str_frag:
        tags.h3(heading)
    return doc_str_frag


def add_param_set(doc_str_frag: tags.div, param_name: str, param_type: str | None, param_description: str) -> tags.div:
    """Add a parameter set."""
    if not param_name:
        param_name = ""
    if param_type is None:
        param_type = "None"
    elem_desc_frag = tags.div(cls="desc")
    elem_desc_frag = add_markdown(fragment=elem_desc_frag, text=param_description)
    with doc_str_frag:
        tags.div(
            tags.div(
                tags.div(param_name, cls="name"),
                tags.div(param_type, cls="type"),
                cls="def",
            ),
            elem_desc_frag,
            cls="container",
        )
    return doc_str_frag


def weld_candidate(text_a: str, text_b: str) -> bool:
    """Determine whether two strings can be merged into a single line."""
    if not text_a or text_a == "":
        return False
    if not text_b or text_b == "":
        return False
    for char in ["|", ">"]:
        if text_a.strip().endswith(char):
            return False
    for char in ["|", "!", "<", "-", "*"]:
        if text_b.strip().startswith(char):
            return False
    return True


def add_markdown(fragment: tags.section | tags.div, text: str) -> tags.section | tags.div:
    """Add a markdown text block."""
    content_str = ""
    if text:
        content_str = text.strip()
    splits = content_str.split("\n")
    code_padding = None
    code_block = False
    other_block = False
    cleaned_text = ""
    for next_line in splits:
        # code blocks
        if "```" in next_line:
            if code_block is False:
                code_block = True
                code_padding = next_line.index("```")
                cleaned_text += f"\n{next_line[code_padding:]}"
            else:
                cleaned_text += f"\n{next_line[code_padding:]}\n"
                code_block = False
                code_padding = None
        elif code_block:
            cleaned_text += f"\n{next_line[code_padding:]}"
        # double breaks
        elif next_line == "":
            cleaned_text += "\n\n"
        # admonitions
        elif next_line.startswith(":::") or next_line.startswith("$$"):
            if not other_block:
                other_block = True
                cleaned_text += f"\n{next_line.strip()}"
            else:
                other_block = False
                cleaned_text += f"\n{next_line.strip()}"
        elif other_block:
            cleaned_text += f"\n{next_line.strip()}"
        # tables
        elif next_line.strip().startswith("|") and next_line.strip().endswith("|"):
            cleaned_text += f"\n{next_line.strip()}"
        # otherwise weld if possible
        elif weld_candidate(cleaned_text, next_line):
            cleaned_text += f" {next_line.strip()}"
        else:
            cleaned_text += f"\n{next_line.strip()}"
    if code_block or other_block:
        raise ValueError(f"Unclosed code block or admonition encountered for content: \n{cleaned_text}")
    cleaned_text += "\n"
    cleaned_text = cleaned_text.replace("\n\n\n", "\n\n")
    with fragment:
        util.raw(render_helpers.to_html(cleaned_text))
    return fragment


def process_docstring(doc_str: str) -> str:
    """Process a docstring."""
    doc_str_frag: tags.div = tags.div(cls="docstring")
    parsed_doc_str = docstring_parser.parse(doc_str)
    if parsed_doc_str.short_description is not None:
        desc = parsed_doc_str.short_description
        if parsed_doc_str.long_description is not None:
            desc += f"\n{parsed_doc_str.long_description}"
        doc_str_frag = add_markdown(fragment=doc_str_frag, text=desc)  # type: ignore
    if parsed_doc_str.params and len(parsed_doc_str.params):
        doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Parameters")  # type: ignore
        for param in parsed_doc_str.params:
            param_name = param.arg_name
            if "kwargs" in param_name:
                param_name = param_name.lstrip("**")
                param_name = f"**{param_name}"
            doc_str_frag = add_param_set(
                doc_str_frag=doc_str_frag,
                param_name=param_name,
                param_type=param.type_name,
                param_description=param.description,  # type: ignore
            )
    # track types parsed from return docstrings
    return_types_in_docstring: list[str] = []
    if parsed_doc_str.many_returns and len(parsed_doc_str.many_returns):
        doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Returns")  # type: ignore
        for doc_str_return in parsed_doc_str.many_returns:
            if doc_str_return.type_name in [None, "None"]:
                param_type = None
            else:
                param_type = doc_str_return.type_name
                return_types_in_docstring.append(param_type)  # type: ignore
            # add fragment
            doc_str_frag = add_param_set(
                doc_str_frag=doc_str_frag,
                param_name=doc_str_return.return_name,  # type: ignore
                param_type=param_type,  # type: ignore
                param_description=doc_str_return.description,  # type: ignore
            )
    if len(parsed_doc_str.raises):
        doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Raises")  # type: ignore
        for raises in parsed_doc_str.raises:
            doc_str_frag = add_param_set(
                doc_str_frag=doc_str_frag,
                param_name="",
                param_type=[raises.type_name],  # type: ignore
                param_description=raises.description,  # type: ignore
            )
    if parsed_doc_str.deprecation is not None:
        raise NotImplementedError("Deprecation not implemented.")
    metas: list[docstring_parser.common.DocstringMeta] = []
    for met in parsed_doc_str.meta:
        if not isinstance(
            met,
            (
                docstring_parser.common.DocstringParam,
                docstring_parser.common.DocstringDeprecated,
                docstring_parser.common.DocstringRaises,
                docstring_parser.common.DocstringReturns,
            ),
        ):
            metas.append(met)
    if metas:
        metas_frag = tags.div(cls="meta")
        metas_frag = add_heading(doc_str_frag=metas_frag, heading="Notes")
        for meta in metas:
            metas_frag = add_markdown(metas_frag, meta.description)  # type: ignore
        doc_str_frag += metas_frag

    return doc_str_frag.render()


# Add custom function
render.env.filters["process_docstring"] = process_docstring
here = Path(__file__).parent

module_file_maps = [
    ("tests.comparisons.mock_file", here / "tests/comparisons/test.astro"),
]
for module_name, output_path in module_file_maps:
    render.configure(template_directory=here / "templates", docformat="numpy", math=True)
    module = importlib.import_module(module_name)
    d = doc.Module(module)
    out = render.html_module(module=d, all_modules={module_name: d})
    with open(output_path, "w") as f:
        f.write(out)
