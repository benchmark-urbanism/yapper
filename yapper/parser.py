"""
Uses AST and docstring_parser to parse docstrings to .astro files.

Intended for use with the Astro static site generator where further linting / linking / styling is done downstream.
"""
from __future__ import annotations

import ast
import logging

import docstring_parser
from dominate import tags, util, dom_tag, svg
from slugify import slugify

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# custom class for markdown
class Markdown(dom_tag.dom_tag):
    pass

link_icon = f'''
M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z
'''


def heading_linker(heading_level: str,
                   heading_name: str,
                   heading_cls: str):
    """ """
    if heading_level == 'h1':
        h = tags.h1(id=slugify(heading_name),
                    cls=heading_cls)
    elif heading_level == 'h2':
        h = tags.h2(id=slugify(heading_name),
                    cls=heading_cls)
    else:
        raise NotImplementedError(f'Heading level {heading_level} is not implemented for linking.')
    with h:
        a = tags.a(aria_hidden='true',
                   tab_index='-1',
                   href=f'#{slugify(heading_name)}')
        with a:
            s = svg.svg(xmlns='http://www.w3.org/2000/svg',
                        viewbox='0 0 20 20',
                        ariaHidden='true',
                        width='15px',
                        height='15px',
                        cls='heading-icon')
            with s:
                svg.path(d=link_icon,
                         fill_rule='evenodd',
                         clip_rule='evenodd')
        util.text(heading_name)

    return h


def addMarkdown(content: str):
    """ """
    content_str = ''
    if content is not None:
        content_str = content.strip().strip('\n')
    md = Markdown(content_str,
                  cls='doc-str-content')
    return md


def process_class(ast_class: ast.ClassDef):
    """ """
    if ast_class is None:
        return
    # build class fragment
    class_fragment = tags.section(cls='yap class')
    class_fragment += heading_linker(heading_level='h2',
                                     heading_name=ast_class.name,
                                     heading_cls='yap class-title')
    # base classes
    for base in ast_class.bases:
        with class_fragment:
            base_item = tags.p(cls='doc-str-content')
            with base_item:
                util.text('Inherits from')
                tags.a(base.id,
                       cls='yap class-base',
                       href=f'#{slugify(base.id)}')
                util.text('.')
    # when the class is passed-in directly its name is captured in the member_name
    methods = []
    props = []
    for item in ast_class.body:
        if isinstance(item, ast.Expr):
            if isinstance(item.value, ast.Constant):
                desc = item.value.value.strip().lstrip('\n').rstrip('\n')
                class_fragment += addMarkdown(desc)
            else:
                raise NotImplementedError(f'Unable to process item: {type(item)}')
        elif isinstance(item, ast.AnnAssign):
            props.append(item)
        elif isinstance(item, ast.FunctionDef):
            is_property = False
            for dec in item.decorator_list:
                if isinstance(dec, ast.Name):
                    if dec.id == 'property':
                        is_property = True
                    else:
                        raise NotImplementedError(f'Unable to process decorator: {dec}')
                elif isinstance(dec, ast.Attribute) and dec.attr == 'setter':
                    logger.warning(f'Skipping setter for {item.name}')
                else:
                    raise NotImplementedError(f'Unable to process decorator: {dec}')
            if is_property:
                props.append(item)
            else:
                methods.append(item)
    # process props
    if len(props):
        class_fragment = add_heading(doc_str_frag=class_fragment,
                                     heading='Properties')
    for prop in props:
        if hasattr(prop, 'name'):
            prop_name = prop.name
        elif hasattr(prop, 'target') and hasattr(prop.target, 'id'):
            prop_name = prop.target.id
        else:
            NotImplementedError(f'Unable to extract property name from: {prop}')
        prop_type = ''
        if hasattr(prop, 'annotation'):
            prop_type = prop.annotation.id
        prop_desc = ''
        with class_fragment:
            tags.div(
                tags.div(
                    tags.div(prop_name,
                             cls='yap class-prop-def-name'),
                    tags.div(prop_type,
                             cls='yap class-prop-def-type'),
                    cls='yap class-prop-def'),
                tags.div(prop_desc,
                         cls='yap class-prop-def-desc'),
                cls='yap class-prop-elem-container')
    # process methods
    if len(methods):
        class_fragment = add_heading(doc_str_frag=class_fragment,
                                     heading='Methods')
    for method in methods:
        with class_fragment:
            process_function(ast_function=method,
                             class_name=ast_class.name)

    return class_fragment


def process_signature(func_name: str,
                      param_names: list[str],
                      param_defaults: list[str]):
    """ """
    # process signature
    sig_fragment = tags.div(cls='yap func-sig')
    with sig_fragment:
        tags.span(f'{func_name}(')
    # nest sig params for CSS alignment
    sig_params_fragment = tags.div(cls='yap func-sig-params')
    for idx, (param_name, param_default) in enumerate(zip(param_names, param_defaults)):
        param = f'{param_name}'
        if param_default is not None:
            param += f'={param_default}'
        if idx < len(param_names) - 1:
            param += ', '
        with sig_params_fragment:
            tags.div(param,
                     cls='yap func-sig-param')
    sig_fragment += sig_params_fragment
    # close the signature
    with sig_fragment:
        tags.span(')')
    return sig_fragment


def add_heading(doc_str_frag: tags.dom_tag,
                heading: str):
    """ """
    with doc_str_frag:
        tags.h3(heading,
                cls='yap doc-str-heading')
    return doc_str_frag


def add_param_set(doc_str_frag: tags.div,
                  param_name: str,
                  param_type: list[str],
                  param_description: str):
    """ """
    if param_name is None:
        param_name = ''
    if param_type is None:
        param_types_str = 'None'
    else:
        param_types_str = ' | '.join(param_type)
    with doc_str_frag:
        tags.div(
            tags.div(
                tags.div(param_name,
                         cls='yap doc-str-elem-name'),
                tags.div(param_types_str,
                         cls='yap doc-str-elem-type'),
                cls='yap doc-str-elem-def'
            ),
            tags.div(
                addMarkdown(param_description),
                cls='yap doc-str-elem-desc'
            ),
            cls='yap doc-str-elem-container')
    return doc_str_frag


def process_docstring(doc_str: str | None,
                      param_names: list[str],
                      param_types: list[list[str]],
                      return_types: list[str]):
    """ """
    doc_str_frag = tags.div(cls='yap doc-str-content')
    if doc_str is not None:
        parsed_doc_str = docstring_parser.parse(doc_str)
        if parsed_doc_str.short_description is not None:
            desc = parsed_doc_str.short_description
            if parsed_doc_str.long_description is not None:
                desc += parsed_doc_str.long_description
            doc_str_frag += addMarkdown(desc)
        if (len(param_names) and parsed_doc_str.params is None) or (len(param_names) != len(parsed_doc_str.params)):
            raise ValueError(f'''
            Number of docstring params does not match number of signature params:
            signature paramters: {param_names}
            parsed doc-str params: {parsed_doc_str.params}
            ''')
        if parsed_doc_str.params is not None and len(parsed_doc_str.params):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag,
                                       heading='Parameters')
            for idx, param in enumerate(parsed_doc_str.params):
                param_name = param.arg_name
                if 'kwargs' in param_name:
                    param_name = param_name.lstrip('**')
                    param_name = f'**{param_name}'
                try:
                    param_idx = param_names.index(param_name)
                except ValueError:
                    raise ValueError(f'docstring param: {param_name} not found in function signature parameters.')
                param_type = param_types[param_idx]
                if param.type_name is not None and param.type_name != param_type:
                    raise ValueError(f'docstring param {param_name} type mismatch against function signature.')
                doc_str_frag = add_param_set(doc_str_frag=doc_str_frag,
                                             param_name=param_name,
                                             param_type=param_type,
                                             param_description=param.description)
        doc_str_return_types = []
        if parsed_doc_str.many_returns is not None and len(parsed_doc_str.many_returns):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag,
                                       heading='Returns')
            for doc_str_return in parsed_doc_str.many_returns:
                if doc_str_return.type_name in [None, 'None']:
                    types = None
                else:
                    types = doc_str_return.type_name.split('|')
                    types = [rt.strip() for rt in types]
                    doc_str_return_types += types
                # if there is a single return and if the return types are no specified,
                # then infer return types from the signature if available
                if len(parsed_doc_str.many_returns) == 1 \
                        and not len(doc_str_return_types):
                    types = return_types
                doc_str_frag = add_param_set(doc_str_frag=doc_str_frag,
                                             param_name=doc_str_return.return_name,
                                             param_type=types,
                                             param_description=doc_str_return.description)
        # if types were provided in both the signature and the docstring, check that these match
        if len(doc_str_return_types) and len(return_types) and not len(doc_str_return_types) == len(return_types):
            raise ValueError(f'''
            Mismatching number of return types in docstring vs. function signature:
            paramters: {param_names}
            types per signature: {return_types}
            types per doc-str: {doc_str_return_types}
            ''')
        if len(parsed_doc_str.raises):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag,
                                       heading='Raises')
            for raises in parsed_doc_str.raises:
                doc_str_frag = add_param_set(doc_str_frag=doc_str_frag,
                                             param_name='',
                                             param_type=[raises.type_name],
                                             param_description=raises.description)
        if parsed_doc_str.deprecation is not None:
            raise NotImplementedError('Deprecation not implemented.')
        metas = []
        for met in parsed_doc_str.meta:
            if not isinstance(met, (docstring_parser.common.DocstringParam,
                                    docstring_parser.common.DocstringDeprecated,
                                    docstring_parser.common.DocstringRaises,
                                    docstring_parser.common.DocstringReturns)):
                metas.append(met)
        if len(metas):
            metas_frag = tags.div(cls='yap doc-str-meta')
            metas_frag = add_heading(doc_str_frag=metas_frag,
                                     heading='Notes')
            for meta in metas:
                metas_frag += addMarkdown(meta.description)
            doc_str_frag += metas_frag

    return doc_str_frag


def extract_types(ast_types: list[str],
                  ast_return: ast.BinOp | ast.Name):
    """ """
    if isinstance(ast_return, ast.Name):
        ast_types.append(ast_return.id)
    if hasattr(ast_return, 'left'):
        if isinstance(ast_return.left, ast.Name):
            ast_types.append(ast_return.left.id)
        elif isinstance(ast_return.left, ast.BinOp):
            extract_types(ast_types=ast_types,
                          ast_return=ast_return.left)
    if hasattr(ast_return, 'right'):
        if isinstance(ast_return.right, ast.Name):
            ast_types.append(ast_return.right.id)
        elif isinstance(ast_return.right, ast.BinOp):
            extract_types(ast_types=ast_types,
                          ast_return=ast_return.right)


def process_function(ast_function: ast.FunctionDef,
                     class_name: str = None):
    """ """
    # don't process private members
    if ast_function.name.startswith('_') and not ast_function.name == '__init__':
        return
    func_fragment = tags.section(cls='yap func')
    if class_name and ast_function.name == '__init__':
        func_name = f'{class_name}'
    elif class_name:
        func_name = f'{class_name}.{ast_function.name}'
    else:
        func_name = ast_function.name
    func_fragment += heading_linker(heading_level='h2',
                                    heading_name=func_name,
                                    heading_cls='yap func-title')
    # extract parameters, types, defaults
    param_names = []
    param_types = []
    param_defaults = []
    # pad defaults to keep in sync
    pad = len(ast_function.args.args) - len(ast_function.args.defaults)
    for idx, arg in enumerate(ast_function.args.args):
        if arg.arg == 'self':
            continue
        param_names.append(arg.arg)
        types = []
        if isinstance(arg.annotation, (ast.Name, ast.BinOp)):
            extract_types(types, arg.annotation)
        param_types.append(types)
        if idx < pad:
            param_defaults.append(None)
        else:
            param_defaults.append(getattr(ast_function.args.defaults[idx - pad], 'value'))
    if hasattr(ast_function.args, 'kwarg') and ast_function.args.kwarg is not None:
        param_names.append('**kwargs')
        param_types.append([])
        param_defaults.append(None)
    # extract return types
    return_types = []
    if isinstance(ast_function.returns, (ast.BinOp, ast.Name)):
        extract_types(ast_types=return_types,
                      ast_return=ast_function.returns)
    # process signature
    with func_fragment:
        tags.div(cls='yap func-sig-content').appendChild(
            process_signature(func_name=func_name,
                              param_names=param_names,
                              param_defaults=param_defaults))
    # process docstring
    doc_str = ast.get_docstring(ast_function)
    func_fragment.appendChild(
        process_docstring(doc_str=doc_str,
                          param_names=param_names,
                          param_types=param_types,
                          return_types=return_types))

    return func_fragment


def parse(module_name: str,
          ast_module: ast.Module,
          yap_config: dict):
    """ """
    # start the DOM fragment
    dom_fragment = tags.div(cls='yap module')
    dom_fragment += heading_linker(heading_level='h1',
                                   heading_name=module_name,
                                   heading_cls='yap module-title')
    # module docstring
    module_docstring = ast.get_docstring(ast_module)
    if module_docstring is not None:
        with dom_fragment:
            tags.div(module_docstring.replace('\n', ' ').strip(),
                     cls='yap doc-str-content')
    # iterate the module's members
    for item in ast_module.body:
        # process functions
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if item.name.startswith('_'):
                continue
            dom_fragment += process_function(item)
        # process classes and nested methods
        elif isinstance(item, ast.ClassDef):
            dom_fragment += process_class(item)
    astro = ''
    if yap_config['intro_template'] is not None:
        for line in yap_config['intro_template'].split('\n'):
            astro += f'{line.strip()}\n'
    astro += dom_fragment.render().strip()
    if yap_config['outro_template'] is not None:
        for line in yap_config['outro_template'].split('\n'):
            astro += f'{line.strip()}\n'

    return astro
