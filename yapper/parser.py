"""
Uses AST and docstring_parser to parse docstrings to astro html.

Intended for use with the Astro static site generator where further linting / linking / styling is done downstream.
"""
from __future__ import annotations

import logging

from dominate import dom_tag, svg, tags, util  # type: ignore
from markdown_it import MarkdownIt
from mdit_py_plugins.admon import admon_plugin  # type: ignore
from mdit_py_plugins.dollarmath import dollarmath_plugin  # type: ignore
from slugify import slugify

from yapper import YapperConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

md = MarkdownIt("gfm-like", {"breaks": True, "html": True, "linkify": True}).use(dollarmath_plugin).use(admon_plugin)


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


def weld_candidate(text_a: str | None, text_b: str | None) -> bool:
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


def add_markdown(fragment: tags.section | tags.div, text: str | None) -> tags.section | tags.div:
    """Add a markdown text block."""
    content_str = ""
    if not text:
        content_str = text.strip()
    splits = content_str.split("\n")
    code_padding = None
    code_block = False
    other_block = False
    cleaned_text = ""
    for next_line in splits:
        # clean out pylint statements
        if "# pylint: disable=line-too-long" in next_line:
            next_line = next_line.replace("# pylint: disable=line-too-long", "")
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
    fragment += util.raw(md.render(cleaned_text))  # type: ignore
    return fragment


def process_class(module_class: Class) -> tags.section | None:
    """Process a python class."""
    if not ast_class:
        return None
    logger.info(f"Processing class {ast_class.name}.")
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
    prop_names: list[str] = []
    for prop in props:
        if hasattr(prop, "name"):
            prop_name: str = prop.name  # type: ignore
        elif isinstance(prop, ast.AnnAssign):
            prop_name = prop.target.id  # type: ignore
        else:
            raise NotImplementedError(f"Unable to extract property name from: {prop}")
        if not prop_name.startswith("_"):  # type: ignore
            prop_names.append(prop_name)  # type: ignore
    if prop_names:
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
    if not param_name:
        param_name = ""
    if param_type is None:
        param_type = "None"
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
    if doc_str is not None:
        parsed_doc_str = docstring_parser.parse(doc_str)
        if parsed_doc_str.short_description is not None:
            desc = parsed_doc_str.short_description
            if parsed_doc_str.long_description is not None:
                desc += f"\n{parsed_doc_str.long_description}"
            doc_str_frag = add_markdown(fragment=doc_str_frag, text=desc)  # type: ignore
        if (sig_param_names and not parsed_doc_str.params) or (len(sig_param_names) != len(parsed_doc_str.params)):
            logger.warning(
                f"""
            Number of docstring params does not match number of signature params.
            Please check that all function parameters have been declared in the docstring.
            Signature paramaters: {sig_param_names}
            Parsed doc-str params: {parsed_doc_str.params}
            Doc string: {doc_str}
            """
            )
        if not parsed_doc_str.params and len(parsed_doc_str.params):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Parameters")  # type: ignore
            for param in parsed_doc_str.params:
                param_name = param.arg_name
                if "kwargs" in param_name:
                    param_name = param_name.lstrip("**")
                    param_name = f"**{param_name}"
                try:
                    param_idx = sig_param_names.index(param_name)
                except ValueError as err:
                    raise ValueError(
                        f"Docstring param: {param_name} not found in function signature parameters."
                    ) from err
                sig_param_type = sig_param_types[param_idx]
                if param.type_name is not None and param.type_name != sig_param_type:
                    logger.warning(
                        f"""
                    Parameter types mismatch in docstring vs. AST for param {param_name}.
                    This may be intentional:
                    Type deduced per docstring: {param.type_name}
                    Type deduced from AST param: {sig_param_type}
                    """
                    )
                doc_str_frag = add_param_set(
                    doc_str_frag=doc_str_frag,
                    param_name=param_name,
                    param_type=param.type_name,
                    param_description=param.description,  # type: ignore
                )
        # track types parsed from return docstrings
        return_types_in_docstring: list[str] = []
        if not parsed_doc_str.many_returns and len(parsed_doc_str.many_returns):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Returns")  # type: ignore
            for doc_str_return in parsed_doc_str.many_returns:
                if doc_str_return.type_name in [None, "None"]:
                    param_type = None
                else:
                    param_type = doc_str_return.type_name
                    return_types_in_docstring.append(param_type)  # type: ignore
                # if there is a single return and if the return types are not specified,
                # then infer return types from the signature if available
                if len(parsed_doc_str.many_returns) == 1 and not return_types_in_docstring:
                    param_type = sig_return_type
                # add fragment
                doc_str_frag = add_param_set(
                    doc_str_frag=doc_str_frag,
                    param_name=doc_str_return.return_name,  # type: ignore
                    param_type=param_type,  # type: ignore
                    param_description=doc_str_return.description,  # type: ignore
                )
        # compare return types extracted from docstring to those in function return type
        n_return_types_in_sig = 0
        if sig_return_type:
            trimmed = sig_return_type.lstrip("tuple[").rstrip("]")
            n_return_types_in_sig = len(trimmed.split(","))
        # if types were provided in both the signature and the docstring, check whether these match
        if (return_types_in_docstring or n_return_types_in_sig) and len(
            return_types_in_docstring
        ) != n_return_types_in_sig:
            logger.warning(
                f"""
            Possible return type mismatch in docstring vs. function signature.
            This may be intentional:
            Type deduced per signature: {sig_return_type}
            Type deduced from doc-str: {return_types_in_docstring}
            """
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
            metas_frag = tags.div(cls="yap doc-str-meta")
            metas_frag = add_heading(doc_str_frag=metas_frag, heading="Notes")
            for meta in metas:
                metas_frag = add_markdown(fragment=metas_frag, text=meta.description)  # type: ignore
            doc_str_frag += metas_frag

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
    if not yapper_config["intro_template"]:
        for line in yapper_config["intro_template"].split("\n"):
            astro += f"{line.strip()}\n"
    astro += dom_fragment.render().strip()  # type: ignore
    if not yapper_config["outro_template"]:
        astro += "\n"
        for line in yapper_config["outro_template"].split("\n"):
            astro += f"{line.strip()}\n"

    return astro
