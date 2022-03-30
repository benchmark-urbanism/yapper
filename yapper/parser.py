"""
Uses AST and docstring_parser to parse docstrings to html & markdown.

Intended for use with static site generators where further linting / linking / styling is done downstream.

Loosely based on Numpy-style docstrings.

Automatically infers types from signature typehints.
By design, explicitly documented types are NOT supported in docstrings.
"""
from __future__ import annotations

import ast
import logging
from markdown import markdown
import pathlib

import docstring_parser
from dominate import tags, util
from slugify import slugify

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

line_break_chars = ['-', '_', '!', '|', '>', ':']


def extract_text_block(splits_enum, splits, indented_block=False, is_hint_block=False):
    """
    Parses a block of text and decides whether or not to wrap.
    Return if iters finish or on end of indentation (optional) or on start of new heading
    """
    block = []
    while True:
        # feed
        lookahead_idx, next_line = next(splits_enum)
        # return if indented block and next is not indented (but don't get tripped up with empty lines)
        if indented_block and not next_line.startswith(' ') and not next_line.strip() == '':
            return lookahead_idx, next_line, '\n'.join(block)
        # return if the next next-line would be a new heading
        elif lookahead_idx < len(splits) and splits[lookahead_idx].startswith('---'):
            return lookahead_idx, next_line, '\n'.join(block)
        # return if inside a hint block and the end of the hint block has been encountered
        elif is_hint_block and next_line.strip().startswith(':::'):
            return lookahead_idx, next_line, '\n'.join(block)
        # be careful with stripping content for lines with intentional breaks, e.g. indented bullets...
        # if parsing indented blocks, strip the first four spaces
        if indented_block:
            next_line = next_line[4:]
        # code blocks
        if next_line.strip().startswith('```'):
            code_block = next_line.strip() + '\n'
            while True:
                lookahead_idx, next_line = next(splits_enum)
                if indented_block:
                    next_line = next_line[4:]
                code_block += next_line + '\n'
                if next_line.startswith('```'):
                    break
            block.append(code_block)
        # tip blocks
        elif next_line.strip().startswith(':::'):
            hint_in = '\n' + next_line.strip() + '\n\n'
            # unpacks hint block
            lookahead_idx, next_line, hint_block = extract_text_block(splits_enum,
                                                                      splits,
                                                                      indented_block=indented_block,
                                                                      is_hint_block=True)
            # next line will be closing characters, i.e. ':::', insert manually to add newline
            block.append(hint_in + hint_block + '\n:::')
        # if no block content exists yet
        elif not len(block):
            block.append(next_line)
        # keep blank lines
        elif next_line.strip() == '':
            block.append('')
        # don't wrap if the previous line is blank
        elif block[-1] == '':
            block.append(next_line)
        # don't wrap if the line starts with a bullet point, picture, or table character
        elif next_line.strip()[0] in line_break_chars:
            block.append(next_line)
        # or if the previous line ends with a bullet point, picture, or table character
        elif block[-1].strip()[-1] in line_break_chars:
            block.append(next_line)
        # otherwise wrap
        else:
            # should be safe to strip text when wrapping
            block[-1] += ' ' + next_line.strip()
        # return if iters exhausted
        if lookahead_idx == len(splits):
            return lookahead_idx, next_line, '\n'.join(block)


def process_class(ast_class: ast.ClassDef):
    """ """
    if ast_class is not None:
        class_fragment = tags.section(cls='yap class')
        class_fragment.appendChild(tags.h2(ast_class.name,
                                           cls='yap class-title',
                                           id=slugify(ast_class.name)))
        # when the class is passed-in directly its name is captured in the member_name
        for item in ast_class.body:
            if isinstance(item, ast.Expr):
                if isinstance(item.value, ast.Constant):
                    desc = item.value.value.strip().lstrip('\n').rstrip('\n')
                    class_fragment.appendChild(util.raw(markdown(desc,
                                                                 extensions=['extra', 'nl2br', 'sane_lists', 'smarty'])))
                else:
                    raise NotImplementedError
            elif isinstance(item, ast.AnnAssign):
                class_fragment.appendChild(tags.div(
                    tags.div(item.target.id,
                             cls='yap class-prop-def-name'),
                    tags.div(item.annotation.id,
                             cls='yap class-prop-def-type'),
                    cls='yap class-prop-def'))
            elif isinstance(item, ast.FunctionDef):
                is_property = False
                for dec in item.decorator_list:
                    if isinstance(dec, ast.Name):
                        if dec.id == 'property':
                            is_property = True
                        else:
                            raise NotImplementedError
                    else:
                        raise NotImplementedError
                if is_property:
                    prop_type = ''
                    if hasattr(item, 'annotation'):
                        prop_type = item.annotation.id
                    class_fragment.appendChild(tags.div(
                        tags.div(item.name,
                                 cls='yap class-prop-name'),
                        tags.div(prop_type,
                                 cls='yap class-prop-type'),
                        cls='yap class-prop'))
                else:
                    class_fragment.appendChild(
                        process_function(ast_function=item,
                                         class_name=ast_class.name))
        return class_fragment


def process_signature(func_name: str,
                      param_names: list[str],
                      param_defaults: list[str]):
    """ """
    # process signature
    sig_fragment = tags.div(cls='yap func-sig-title')
    sig_fragment.appendChild(
        tags.div(f'{func_name}(',
                 cls='yap func-sig-start'))
    # nest sig params for CSS alignment
    sig_params_fragment = tags.div(cls='yap func-sig-params')
    for idx, (param_name, param_default) in enumerate(zip(param_names, param_defaults)):
        param = f'{param_name}'
        if param_default is not None:
            param += f'={param_default}'
        if idx < len(param_names) - 1:
            param += ', '
        sig_params_fragment.appendChild(
            tags.div(param,
                     cls='yap func-sig-param'))
    # close the signature
    sig_fragment.appendChild(sig_params_fragment)
    sig_fragment.appendChild(
        tags.div(')',
                 cls='yap func-sig-end'))
    return sig_fragment


def add_heading(doc_str_frag: tags.div,
                heading: str):
    """ """
    return doc_str_frag.appendChild(
        tags.h2(heading,
                cls='yap doc-str-heading'))


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
    return doc_str_frag.appendChild(
        tags.div(
            tags.div(
                tags.div(param_name,
                         cls='yap doc-str-elem-name'),
                tags.div(param_types_str,
                         cls='yap doc-str-elem-type'),
                cls='yap doc-str-elem-def'
            ),
            util.raw(markdown(param_description,
                              extensions=['extra', 'nl2br', 'sane_lists', 'smarty'])),
            cls='yap doc-str-elem-container'))


def process_docstring(doc_str: str | None,
                      param_names: list[str],
                      param_types: list[list[str]],
                      return_types: list[str]):
    """ """
    doc_str_frag = tags.div(cls='yap doc-str-content')
    if doc_str is not None:
        parsed_doc_str = docstring_parser.parse(doc_str)
        if parsed_doc_str.short_description is not None:
            doc_str_frag.appendChild(parsed_doc_str.short_description)
        if parsed_doc_str.long_description is not None:
            doc_str_frag.appendChild(util.raw(markdown(parsed_doc_str.long_description,
                                                       extensions=['extra', 'nl2br', 'sane_lists', 'smarty'])))
        if (len(param_names) and parsed_doc_str.params is None) or (len(param_names) != len(parsed_doc_str.params)):
            raise ValueError('Number of docstring params does not match number of signature params')
        if parsed_doc_str.params is not None and len(parsed_doc_str.params):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag,
                                       heading='Parameters')
            for idx, param in enumerate(parsed_doc_str.params):
                param_name = param.arg_name
                if param_name == 'kwargs':
                    param_name = '**kwargs'
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
            raise ValueError('Mismatching number of return types in docstring vs. function signature.')
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
                metas_frag.appendChild(util.raw(markdown(meta.description,
                                                         extensions=['extra', 'nl2br', 'sane_lists', 'smarty'])))
            doc_str_frag.appendChild(metas_frag)

    return doc_str_frag


def extract_types(ast_types: list[str], ast_return: ast.BinOp | ast.Name):
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
    func_fragment.appendChild(tags.h2(func_name,
                                      cls='yap func-title',
                                      id=slugify(func_name)))
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
        extract_types(ast_types=return_types, ast_return=ast_function.returns)
    # process signature
    sig_fragment = process_signature(func_name=func_name,
                                     param_names=param_names,
                                     param_defaults=param_defaults)
    func_fragment.appendChild(tags.div(cls='yap func-sig-content').appendChild(sig_fragment))
    # process docstring
    doc_str = ast.get_docstring(ast_function)
    doc_str_fragment = process_docstring(doc_str=doc_str,
                                         param_names=param_names,
                                         param_types=param_types,
                                         return_types=return_types)
    func_fragment.appendChild(doc_str_fragment)

    return func_fragment


def parse(module_path: pathlib.Path,
          ast_module: ast.Module,
          yap_config: dict):
    """ """
    # module name
    module_str = str(module_path)
    module_str = module_str.rstrip('.py')
    path_splits = module_str.split('/')
    path_splits = [ps for ps in path_splits if ps not in ['..', '.']]
    path_text = '.'.join(path_splits)
    # start the DOM fragment
    dom_fragment = tags.div(cls='yap module')
    # add
    dom_fragment.appendChild(tags.h1(path_text,
                                     cls='yap module-title',
                                     id=slugify(path_text)))
    # module docstring
    module_docstring = ast.get_docstring(ast_module)
    if module_docstring is not None:
        dom_fragment.appendChild(
            tags.div(module_docstring.replace('\n', ' ').strip(),
                     cls='yap doc-str'))
    # iterate the module's members
    for item in ast_module.body:
        # process functions
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            func_fragment = process_function(item)
            dom_fragment.appendChild(func_fragment)
        # process classes and nested methods
        elif isinstance(item, ast.ClassDef):
            class_fragment = process_class(item)
            dom_fragment.appendChild(class_fragment)

    return dom_fragment
