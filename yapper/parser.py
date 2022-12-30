"""
Uses AST and docstring_parser to parse docstrings to astro html.

Intended for use with the Astro static site generator where further linting / linking / styling is done downstream.
"""
from __future__ import annotations

import logging

from dominate import dom_tag, svg, tags, util  # type: ignore
from griffe.dataclasses import Class, Function, Module
from griffe.docstrings import numpy as np_parser
from griffe.docstrings.dataclasses import (
    DocstringParameter,
    DocstringRaise,
    DocstringReturn,
    DocstringSectionDeprecated,
    DocstringSectionExamples,
    DocstringSectionParameters,
    DocstringSectionRaises,
    DocstringSectionReturns,
    DocstringSectionText,
    DocstringSectionYields,
    DocstringYield,
)
from slugify import slugify

from yapper import YapperConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Markdown(dom_tag.dom_tag):
    """Custom dom tag for markdown."""


LINK_ICON = """
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
"""


def generate_heading(heading_level: str, heading_name: str, heading_cls: str):
    """Create a heading of specified level with a link anchor."""
    if heading_level == "h1":
        h = tags.h1(id=slugify(heading_name), cls=heading_cls)
    elif heading_level == "h2":
        h = tags.h2(id=slugify(heading_name), cls=heading_cls)
    else:
        raise NotImplementedError(f"Heading level {heading_level} is not implemented for linking.")
    with h:
        a = tags.a(aria_hidden="true", tabindex="-1", href=f"#{slugify(heading_name)}")
        with a:
            s = svg.svg(
                xmlns="http://www.w3.org/2000/svg",
                viewBox="0 0 20 20",
                aria_hidden="true",
                width="15px",
                height="15px",
                cls="heading-icon",
            )
            with s:
                svg.path(d=LINK_ICON, fill_rule="evenodd", clip_rule="evenodd")
        util.text(heading_name)

    return h


def weld_candidate(text_a: str, text_b: str) -> bool:
    """Determine whether two strings can be merged into a single line."""
    if text_a is None or text_a == "":
        return False
    if text_b is None or text_b == "":
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
    if text is not None:
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
    md: Markdown = Markdown(util.raw(cleaned_text))  # type: ignore
    # add is:raw directive
    fragment += util.raw(md.render().replace("<Markdown>", "<Markdown is:raw>"))  # type: ignore
    return fragment


def process_class(module_class: Class) -> tags.section | None:
    """Process a python class."""
    logger.info(f"Processing class {module_class.name}.")
    # build class fragment
    class_fragment: tags.section = tags.section(cls="yap class")
    class_fragment += generate_heading(
        heading_level="h2", heading_name=module_class.name, heading_cls="yap class-title"
    )
    # class docstring
    if module_class.docstring is not None:
        class_fragment = add_markdown(fragment=class_fragment, text=module_class.docstring.value)  # type: ignore
    # base classes
    for base in module_class.bases:
        with class_fragment:
            base_item = tags.p(cls="yap class-base")
            with base_item:
                for base in module_class.bases:
                    util.text("Inherits from")
                    tags.a(base.brief, href=f"#{slugify(base.brief)}")  # type: ignore
                    util.text(".")
    # process props
    prop_keys: list[str] = []
    for prop_key in module_class.attributes.keys():
        if not prop_key.startswith("_"):
            prop_keys.append(prop_key)
    if prop_keys:
        class_fragment = add_heading(doc_str_frag=class_fragment, heading="Properties")  # type: ignore
    for prop_key in prop_keys:
        prop_val = module_class.attributes[prop_key]
        prop_type = ""
        if prop_val.annotation is not None and hasattr(prop_val.annotation, "full"):
            prop_type = prop_val.annotation.full  # type: ignore
        prop_desc = ""
        if prop_val.docstring is not None:
            prop_desc = prop_val.docstring.value
        with class_fragment:
            tags.div(
                tags.div(
                    tags.div(prop_val.name, cls="yap class-prop-def-name"),
                    tags.div(prop_type, cls="yap class-prop-def-type"),
                    cls="yap class-prop-def",
                ),
                tags.div(prop_desc, cls="yap class-prop-def-desc"),
                cls="yap class-prop-elem-container",
            )
    # process methods
    method_keys: list[str] = []
    for method_key in module_class.functions.keys():
        if not method_key.startswith("_") or method_key == "__init__":
            method_keys.append(method_key)
    if method_keys:
        class_fragment = add_heading(doc_str_frag=class_fragment, heading="Methods")  # type: ignore
    for method_key in method_keys:
        func_fragment = process_function(module_class.functions[method_key])
        class_fragment += func_fragment

    return class_fragment


def process_signature(module_function: Function) -> tags.div:
    """Process function signature."""
    # process signature
    sig_fragment: tags.div = tags.div(cls="yap func-sig")
    # use parent class if __init__ method
    if module_function.name == "__init__":
        func_name = module_function.parent.name  # type: ignore
    else:
        func_name = module_function.name
    n_params = 0
    for param in module_function.parameters:
        if param.name != "self":
            n_params += 1
    if n_params == 0:
        with sig_fragment:
            tags.span(f"{func_name}()")
    else:
        with sig_fragment:
            tags.span(f"{func_name}(")
        # nest sig params for CSS alignment
        sig_params_fragment = tags.div(cls="yap func-sig-params")
        for idx, (param) in enumerate(module_function.parameters):
            if param.name == "self":
                continue
            param_text = f"{param.name}"
            if param.default is not None:
                param_text += f"={param.default}"
            if idx < len(module_function.parameters) - 1:
                param_text += ", "
            else:
                param_text += ")"
            with sig_params_fragment:
                tags.div(param_text, cls="yap func-sig-param")
        sig_fragment += sig_params_fragment
    return sig_fragment


def add_heading(doc_str_frag: tags.div | tags.section, heading: str) -> tags.div | tags.section:
    """Add a heading."""
    with doc_str_frag:
        tags.h3(heading, cls="yap")
    return doc_str_frag


docstringContentType = DocstringParameter | DocstringReturn | DocstringRaise | DocstringYield


def add_docstr_params(doc_str_frag: tags.div, param_set: docstringContentType) -> tags.div:
    """Add a parameter set."""
    param_name = ""
    if hasattr(param_set, "name") and param_set.name is not None:  # type: ignore
        param_name = param_set.name  # type: ignore
    param_anno = "None"
    if param_set.annotation is not None and hasattr(param_set.annotation, "full"):
        if hasattr(param_set.annotation, "full"):
            param_anno = str(param_set.annotation.full)  # type: ignore
    # strip away extraneous annotation information
    if param_anno.startswith("Optional"):
        param_anno = param_anno.replace("Optional[", "")
        param_anno = param_anno[:-1]
    if param_anno.startswith("Union"):
        param_anno = param_anno.replace("Union[", "")
        param_anno = param_anno[:-1]
        param_anno = param_anno.split(",")
        param_anno = "|".join([pa.strip() for pa in param_anno])
    # only remain tail descriptor
    if "." in param_anno and not "np." in param_anno or "npt." in param_anno:
        param_anno = param_anno.rsplit(".", maxsplit=1)[-1]
    elem_desc_frag = tags.div(cls="yap doc-str-elem-desc")
    elem_desc_frag = add_markdown(fragment=elem_desc_frag, text=param_set.description)
    with doc_str_frag:
        tags.div(
            tags.div(
                tags.div(param_name, cls="yap doc-str-elem-name"),
                tags.div(param_anno, cls="yap doc-str-elem-type"),
                cls="yap doc-str-elem-def",
            ),
            elem_desc_frag,
            cls="yap doc-str-elem-container",
        )
    return doc_str_frag


def process_func_docstring(module_function: Function) -> tags.div:
    """Process a docstring."""
    doc_str_frag: tags.div = tags.div(cls="yap")
    if module_function.docstring is not None:  # pylint: disable=too-many-nested-blocks
        doc_str = np_parser.parse(module_function.docstring)
        for doc_str_content in doc_str:
            if isinstance(doc_str_content, DocstringSectionText):
                text_content = doc_str_content.value
                doc_str_frag = add_markdown(fragment=doc_str_frag, text=text_content)  # type: ignore
            elif isinstance(doc_str_content, DocstringSectionExamples):
                doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Examples")  # type: ignore
                for content in doc_str_content.value:
                    for sub_content in content:
                        if isinstance(sub_content, str):
                            doc_str_frag = add_markdown(fragment=doc_str_frag, text=sub_content)  # type: ignore
            elif isinstance(doc_str_content, DocstringSectionParameters):
                doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Parameters")  # type: ignore
                for content in doc_str_content.value:
                    doc_str_frag = add_docstr_params(doc_str_frag=doc_str_frag, param_set=content)
            elif isinstance(doc_str_content, DocstringSectionRaises):
                doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Raises")  # type: ignore
                for content in doc_str_content.value:
                    doc_str_frag = add_docstr_params(doc_str_frag=doc_str_frag, param_set=content)
            elif isinstance(doc_str_content, DocstringSectionYields):
                doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Yields")  # type: ignore
                for content in doc_str_content.value:
                    doc_str_frag = add_docstr_params(doc_str_frag=doc_str_frag, param_set=content)
            elif isinstance(doc_str_content, DocstringSectionReturns):
                doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Returns")  # type: ignore
                for content in doc_str_content.value:
                    doc_str_frag = add_docstr_params(doc_str_frag=doc_str_frag, param_set=content)
            elif isinstance(doc_str_content, DocstringSectionDeprecated):
                doc_str_frag = add_markdown(fragment=doc_str_frag, text=doc_str_content.value)  # type: ignore
            else:
                raise NotImplementedError(f"Docstring type: {type(doc_str_content)} not implemented.")

    return doc_str_frag


def process_function(
    module_function: Function,
) -> tags.section | None:
    """Process a function."""
    # don't process private members
    if module_function.name.startswith("_") and not module_function.name == "__init__":
        return None
    logger.info(f"Processing function: {module_function.name}")
    func_fragment: tags.section = tags.section(cls="yap func")
    is_method = False
    if isinstance(module_function.parent, Class):
        is_method = True
    if is_method and module_function.name == "__init__":
        heading_name = f"{module_function.parent.name}.__init__"  # type: ignore
    elif is_method:
        heading_name = f"{module_function.parent.name}.{module_function.name}"  # type: ignore
    else:
        heading_name = module_function.name
    func_fragment += generate_heading(heading_level="h2", heading_name=heading_name, heading_cls="yap func-title")
    # process signature
    with func_fragment:
        tags.div(cls="yap func-sig-content").appendChild(process_signature(module_function))  # type: ignore
    # process docstring
    func_fragment.appendChild(process_func_docstring(module_function))  # type: ignore

    return func_fragment


def parse(module_content: Module, yapper_config: YapperConfig) -> str:
    """Parse a python module."""
    logger.info(f"Parsing module: {module_content.canonical_path}")
    # start the DOM fragment
    dom_fragment: tags.div = tags.div(cls="yap module")
    dom_fragment += generate_heading(
        heading_level="h1", heading_name=module_content.canonical_path, heading_cls="yap module-title"
    )
    # module docstring
    if module_content.docstring is not None:
        dom_fragment = add_markdown(fragment=dom_fragment, text=module_content.docstring.value)  # type: ignore
    # iterate the module's members
    for member in module_content.members.values():
        # process functions
        if isinstance(member, Function):
            if member.name.startswith("_"):
                continue
            dom_fragment += process_function(member)
        # process classes and nested methods
        elif isinstance(member, Class):
            dom_fragment += process_class(member)
    astro: str = ""
    if yapper_config["intro_template"] is not None:
        for line in yapper_config["intro_template"].split("\n"):
            astro += f"{line.strip()}\n"
    astro += dom_fragment.render().strip()  # type: ignore
    if yapper_config["outro_template"] is not None:
        astro += "\n"
        for line in yapper_config["outro_template"].split("\n"):
            astro += f"{line.strip()}\n"

    return astro
