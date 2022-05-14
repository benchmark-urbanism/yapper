"""
Uses AST and docstring_parser to parse docstrings to astro html.

Intended for use with the Astro static site generator where further linting / linking / styling is done downstream.
"""
from __future__ import annotations

import ast
import logging

import docstring_parser
from dominate import dom_tag, svg, tags, util
from slugify import slugify

from yapper import YapperConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# custom class for markdown
class Markdown(dom_tag.dom_tag):
    """Custom dom tag for markdown."""


LINK_ICON = """
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
"""


def heading_linker(heading_level: str, heading_name: str, heading_cls: str):
    """Create a heading of specified level with a link anchor."""
    if heading_level == "h1":
        h = tags.h1(id=slugify(heading_name), cls=heading_cls)
    elif heading_level == "h2":
        h = tags.h2(id=slugify(heading_name), cls=heading_cls)
    else:
        raise NotImplementedError(f"Heading level {heading_level} is not implemented for linking.")
    with h:
        a = tags.a(aria_hidden="true", tab_index="-1", href=f"#{slugify(heading_name)}")
        with a:
            s = svg.svg(
                xmlns="http://www.w3.org/2000/svg",
                viewbox="0 0 20 20",
                ariaHidden="true",
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
    code_block = False
    code_padding = None
    admonition = False
    text = ""
    for next_line in splits:
        # code blocks
        if "```" in next_line:
            if code_block is False:
                code_block = True
                code_padding = next_line.index("```")
                text += f"\n{next_line[code_padding:]}"
            else:
                text += f"\n{next_line[code_padding:]}\n"
                code_block = False
                code_padding = None
        elif code_block:
            text += f"\n{next_line[code_padding:]}"
        # double breaks
        elif next_line == "":
            text += "\n\n"
        # admonitions
        elif ":::" in next_line:
            admonition = True
            text += f"\n{next_line.strip()}"
        elif admonition is True:
            admonition = False
            text += f"\n{next_line.strip()}"
        # tables
        elif next_line.strip().startswith("|") and next_line.strip().endswith("|"):
            text += f"\n{next_line.strip()}"
        # otherwise weld if possible
        elif weld_candidate(text, next_line):
            text += f" {next_line.strip()}"
        else:
            text += f"\n{next_line.strip()}"
    if code_block:
        raise ValueError(f"Unclosed code block or admonition encountered for content: \n{text}")
    text += "\n"
    md: Markdown = Markdown(text)
    # add is:raw directive
    fragment += util.raw(md.render().replace("<Markdown>", "<Markdown is:raw>"))  # type: ignore
    return fragment


def process_class(ast_class: ast.ClassDef) -> tags.section | None:
    """Process a python class."""
    if ast_class is None:
        return None
    # build class fragment
    class_fragment: tags.section = tags.section(cls="yap class")
    class_fragment += heading_linker(heading_level="h2", heading_name=ast_class.name, heading_cls="yap class-title")
    # base classes
    for base in ast_class.bases:
        with class_fragment:
            base_item = tags.p(cls="yap class-base")
            with base_item:
                util.text("Inherits from")
                tags.a(base.id, href=f"#{slugify(base.id)}")  # type: ignore
                util.text(".")
    # when the class is passed-in directly its name is captured in the member_name
    methods: list[ast.FunctionDef] = []
    props: list[ast.Expr | ast.AnnAssign | ast.FunctionDef] = []
    for item in ast_class.body:
        if isinstance(item, ast.Expr):
            if isinstance(item.value, ast.Constant):
                desc = item.value.value.strip()
                class_fragment = add_markdown(fragment=class_fragment, text=desc)  # type: ignore
            else:
                raise NotImplementedError(f"Unable to process item: {type(item)}")
        elif isinstance(item, ast.AnnAssign):
            props.append(item)
        elif isinstance(item, ast.FunctionDef):
            is_property = False
            for dec in item.decorator_list:
                if isinstance(dec, ast.Name):
                    if dec.id == "property":
                        is_property = True
                    else:
                        raise NotImplementedError(f"Unable to process decorator: {dec}")
                elif isinstance(dec, ast.Attribute) and dec.attr == "setter":
                    logger.warning(f"Skipping setter for {item.name}")
                else:
                    raise NotImplementedError(f"Unable to process decorator: {dec}")
            if is_property:
                props.append(item)
            else:
                methods.append(item)
    # process props
    if props:
        class_fragment = add_heading(doc_str_frag=class_fragment, heading="Properties")  # type: ignore
    for prop in props:
        if hasattr(prop, "name"):
            prop_name: str = prop.name  # type: ignore
        elif isinstance(prop, ast.AnnAssign):
            prop_name: str = prop.target.id  # type: ignore
        else:
            raise NotImplementedError(f"Unable to extract property name from: {prop}")
        prop_type = ""
        if hasattr(prop, "annotation"):
            prop_type: str = prop.annotation.id  # type: ignore
        prop_desc = ""
        with class_fragment:
            tags.div(
                tags.div(
                    tags.div(prop_name, cls="yap class-prop-def-name"),
                    tags.div(prop_type, cls="yap class-prop-def-type"),
                    cls="yap class-prop-def",
                ),
                tags.div(prop_desc, cls="yap class-prop-def-desc"),
                cls="yap class-prop-elem-container",
            )
    # process methods
    if methods:
        class_fragment = add_heading(doc_str_frag=class_fragment, heading="Methods")  # type: ignore
    for method in methods:
        func_fragment = process_function(ast_function=method, class_name=ast_class.name)
        if func_fragment is not None:
            class_fragment += func_fragment

    return class_fragment


def process_signature(func_name: str, param_names: list[str], param_defaults: list[str | None]) -> tags.div:
    """Process function signature."""
    # process signature
    sig_fragment: tags.div = tags.div(cls="yap func-sig")
    with sig_fragment:
        tags.span(f"{func_name}(")
    # nest sig params for CSS alignment
    sig_params_fragment = tags.div(cls="yap func-sig-params")
    for idx, (param_name, param_default) in enumerate(zip(param_names, param_defaults)):
        param = f"{param_name}"
        if param_default is not None:
            param += f"={param_default}"
        if idx < len(param_names) - 1:
            param += ", "
        else:
            param += ")"
        with sig_params_fragment:
            tags.div(param, cls="yap func-sig-param")
    sig_fragment += sig_params_fragment

    return sig_fragment


def add_heading(doc_str_frag: tags.div | tags.section, heading: str) -> tags.div | tags.section:
    """Add a heading."""
    with doc_str_frag:
        tags.h3(heading, cls="yap")
    return doc_str_frag


def add_param_set(doc_str_frag: tags.div, param_name: str, param_type: list[str], param_description: str) -> tags.div:
    """Add a parameter set."""
    if param_name is None:
        param_name = ""
    if param_type is None:
        param_types_str = "None"
    else:
        param_types_str = " | ".join(param_type)
    elem_desc_frag = tags.div(cls="yap doc-str-elem-desc")
    elem_desc_frag = add_markdown(fragment=elem_desc_frag, text=param_description)
    with doc_str_frag:
        tags.div(
            tags.div(
                tags.div(param_name, cls="yap doc-str-elem-name"),
                tags.div(param_types_str, cls="yap doc-str-elem-type"),
                cls="yap doc-str-elem-def",
            ),
            elem_desc_frag,
            cls="yap doc-str-elem-container",
        )
    return doc_str_frag


def process_docstring(
    doc_str: str | None, param_names: list[str], param_types: list[list[str]], return_types: list[str]
) -> tags.div:
    """Process a docstring."""
    doc_str_frag: tags.div = tags.div(cls="yap")
    if doc_str is not None:
        parsed_doc_str = docstring_parser.parse(doc_str)
        if parsed_doc_str.short_description is not None:
            desc = parsed_doc_str.short_description
            if parsed_doc_str.long_description is not None:
                desc += f"\n{parsed_doc_str.long_description}"
            doc_str_frag = add_markdown(fragment=doc_str_frag, text=desc)  # type: ignore
        if (len(param_names) and parsed_doc_str.params is None) or (len(param_names) != len(parsed_doc_str.params)):
            raise ValueError(
                f"""
            Number of docstring params does not match number of signature params:
            signature paramters: {param_names}
            parsed doc-str params: {parsed_doc_str.params}
            doc string: {doc_str}
            """
            )
        if parsed_doc_str.params is not None and len(parsed_doc_str.params):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Parameters")  # type: ignore
            for param in parsed_doc_str.params:
                param_name = param.arg_name
                if "kwargs" in param_name:
                    param_name = param_name.lstrip("**")
                    param_name = f"**{param_name}"
                try:
                    param_idx = param_names.index(param_name)
                except ValueError as err:
                    raise ValueError(
                        f"Docstring param: {param_name} not found in function signature parameters."
                    ) from err
                param_type = param_types[param_idx]
                if param.type_name is not None and param.type_name not in param_type:
                    raise ValueError(f"Docstring param {param_name} type mismatch against function signature.")
                doc_str_frag = add_param_set(
                    doc_str_frag=doc_str_frag,
                    param_name=param_name,
                    param_type=param_type,
                    param_description=param.description,  # type: ignore
                )
        doc_str_return_types = []
        if parsed_doc_str.many_returns is not None and len(parsed_doc_str.many_returns):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag, heading="Returns")  # type: ignore
            for doc_str_return in parsed_doc_str.many_returns:
                if doc_str_return.type_name in [None, "None"]:
                    types = None
                else:
                    types = doc_str_return.type_name.split("|")  # type: ignore
                    types = [rt.strip() for rt in types]
                    doc_str_return_types += types  # type: ignore
                # if there is a single return and if the return types are no specified,
                # then infer return types from the signature if available
                if len(parsed_doc_str.many_returns) == 1 and not doc_str_return_types:
                    types = return_types
                doc_str_frag = add_param_set(
                    doc_str_frag=doc_str_frag,
                    param_name=doc_str_return.return_name,  # type: ignore
                    param_type=types,  # type: ignore
                    param_description=doc_str_return.description,  # type: ignore
                )
        # if types were provided in both the signature and the docstring, check that these match
        if doc_str_return_types and return_types and not len(doc_str_return_types) == len(return_types):
            raise ValueError(
                f"""
            Mismatching number of return types in docstring vs. function signature:
            paramters: {param_names}
            types per signature: {return_types}
            types per doc-str: {doc_str_return_types}
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


def extract_types(ast_types: list[str], ast_return: ast.BinOp | ast.Name):
    """Extract parameter types."""
    if isinstance(ast_return, ast.Name):
        ast_types.append(ast_return.id)
    if hasattr(ast_return, "left"):
        if isinstance(ast_return.left, ast.Name):  # type: ignore
            ast_types.append(ast_return.left.id)  # type: ignore
        elif isinstance(ast_return.left, ast.BinOp):  # type: ignore
            extract_types(ast_types=ast_types, ast_return=ast_return.left)  # type: ignore
    if hasattr(ast_return, "right"):
        if isinstance(ast_return.right, ast.Name):  # type: ignore
            ast_types.append(ast_return.right.id)  # type: ignore
        elif isinstance(ast_return.right, ast.BinOp):  # type: ignore
            extract_types(ast_types=ast_types, ast_return=ast_return.right)  # type: ignore


def process_function(
    ast_function: ast.FunctionDef | ast.AsyncFunctionDef, class_name: str | None = None
) -> tags.section | None:
    """Process a function."""
    # don't process private members
    if ast_function.name.startswith("_") and not ast_function.name == "__init__":
        return None
    func_fragment: tags.section = tags.section(cls="yap func")
    if class_name and ast_function.name == "__init__":
        func_name = f"{class_name}.__init__"
    elif class_name:
        func_name = f"{class_name}.{ast_function.name}"
    else:
        func_name = ast_function.name
    func_fragment += heading_linker(heading_level="h2", heading_name=func_name, heading_cls="yap func-title")
    # extract parameters, types, defaults
    param_names: list[str] = []
    param_types: list[list[str]] = []
    param_defaults: list[str | None] = []
    # pad defaults to keep in sync
    pad = len(ast_function.args.args) - len(ast_function.args.defaults)
    for idx, arg in enumerate(ast_function.args.args):
        if arg.arg == "self":
            continue
        param_names.append(arg.arg)
        types: list[str] = []
        if isinstance(arg.annotation, (ast.Name, ast.BinOp)):
            extract_types(types, arg.annotation)
        param_types.append(types)
        if idx < pad:
            param_defaults.append(None)
        elif hasattr(ast_function.args.defaults[idx - pad], "value"):
            param_defaults.append(getattr(ast_function.args.defaults[idx - pad], "value"))
        else:
            param_defaults.append("(*)")
    if hasattr(ast_function.args, "kwarg") and ast_function.args.kwarg is not None:
        param_names.append("**kwargs")
        param_types.append([])
        param_defaults.append(None)
    # extract return types
    return_types: list[str] = []
    if isinstance(ast_function.returns, (ast.BinOp, ast.Name)):
        extract_types(ast_types=return_types, ast_return=ast_function.returns)
    # process signature
    with func_fragment:
        tags.div(cls="yap func-sig-content").appendChild(  # type: ignore
            process_signature(func_name=func_name, param_names=param_names, param_defaults=param_defaults)
        )
    # process docstring
    doc_str = ast.get_docstring(ast_function)
    func_fragment.appendChild(  # type: ignore
        process_docstring(doc_str=doc_str, param_names=param_names, param_types=param_types, return_types=return_types)
    )

    return func_fragment


def parse(module_name: str, ast_module: ast.Module, yapper_config: YapperConfig) -> str:
    """Parse a python module."""
    # start the DOM fragment
    dom_fragment: tags.div = tags.div(cls="yap module")
    dom_fragment += heading_linker(heading_level="h1", heading_name=module_name, heading_cls="yap module-title")
    # module docstring
    module_docstring = ast.get_docstring(ast_module)
    if module_docstring is not None:
        frag_text = module_docstring.replace("\n", " ").strip()
        dom_fragment = add_markdown(fragment=dom_fragment, text=frag_text)  # type: ignore
    # iterate the module's members
    for item in ast_module.body:
        # process functions
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if item.name.startswith("_"):
                continue
            dom_fragment += process_function(item)
        # process classes and nested methods
        elif isinstance(item, ast.ClassDef):
            dom_fragment += process_class(item)
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
