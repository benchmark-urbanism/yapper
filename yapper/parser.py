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
import pathlib

import docstring_parser
from dominate import tags
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


def process_class(ast_class: ast.ClassDef,
                  lines: list[str],
                  config: dict[str, str]):
    """ """
    if ast_class is not None:
        class_name = ast_class.name.replace('_', '\_')
        # when the class is passed-in directly its name is captured in the member_name
        lines.append(config['class_name_template'].format(class_name=class_name))
        for item in ast_class.body:
            if isinstance(item, ast.Expr):
                if isinstance(item.value, ast.Constant):
                    v = item.value.value.lstrip('\n').lstrip()
                    lines.append(f'\n{v}')
                else:
                    raise NotImplementedError
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
                    lines.append(config['class_property_template'].format(prop_name=f'{class_name}.{item.name}'))
                else:
                    is_init = item.name == '__init__'
                    process_function(ast_function=item,
                                     lines=lines,
                                     config=config,
                                     class_name=class_name,
                                     is_init=is_init)


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
    for param_name, param_default in zip(param_names, param_defaults):
        param = f'{param_name}'
        if param_default is not None:
            param += f'={param_default}'
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
                  param_type: str,
                  param_description: str):
    """ """
    return doc_str_frag.appendChild(
        tags.div(
            tags.div(
                tags.div(param_name,
                         cls='yap doc-str-param-name'),
                tags.div(param_type,
                         cls='yap doc-str-param-type'),
                cls='yap doc-str-param-def'
            ),
            tags.div(param_description,
                     cls='yap doc-str-param-desc'),
            cls='yap doc-str-param-container'))


def process_docstring(doc_str: str | None,
                      param_names: list[str],
                      param_types: list[str]):
    """ """
    doc_str_frag = tags.div(cls='yap doc-str-content')
    if doc_str is not None:
        parsed_doc_str = docstring_parser.parse(doc_str)
        if parsed_doc_str.short_description is not None:
            doc_str_frag.appendChild(
                tags.p(parsed_doc_str.short_description,
                       cls='yap doc-str-text'))
        if parsed_doc_str.long_description is not None:
            doc_str_frag.appendChild(
                tags.p(parsed_doc_str.long_description,
                       cls='yap doc-str-text'))
        if parsed_doc_str.params is not None:
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag,
                                       heading='Parameters')
            for idx, param in enumerate(parsed_doc_str.params):
                param_name = param.arg_name
                if param_name == 'kwargs':
                    param_type = 'dict'
                else:
                    param_idx = param_names.index(param_name)
                    param_type = param_types[param_idx]
                doc_str_frag = add_param_set(doc_str_frag=doc_str_frag,
                                             param_name=param_name,
                                             param_type=param_type,
                                             param_description=param.description)
        if len(parsed_doc_str.raises):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag,
                                       heading='Raises')
            print('here')
        if len(parsed_doc_str.many_returns):
            logger.warning('Many Returns not implemented.')
        if parsed_doc_str.returns is not None:
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag,
                                       heading='Returns')
            print('here')
        if len(parsed_doc_str.examples):
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag,
                                       heading='Examples')
            print('here')
        if parsed_doc_str.deprecation is not None:
            doc_str_frag = add_heading(doc_str_frag=doc_str_frag,
                                       heading='Deprecation')
            print('here')
    return doc_str_frag


def process_function(ast_function: ast.FunctionDef,
                     config: dict[str, str],
                     class_name: str = None,
                     is_init: bool = False):
    """ """
    # don't process private members
    if ast_function.name.startswith('_') and not ast_function.name == '__init__':
        return
    func_fragment = tags.div(cls='yap func')
    if class_name:
        name = f'{class_name}.{ast_function.name}'
    else:
        name = ast_function.name
    func_fragment.appendChild(tags.h2(name,
                                      cls='yap func-title',
                                      id=slugify(name)))
    # extract parameters
    param_names = []
    param_types = []
    param_defaults = []
    # pad defaults to keep in sync
    pad = len(ast_function.args.args) - len(ast_function.args.defaults)
    for idx, arg in enumerate(ast_function.args.args):
        if arg.arg == 'self':
            continue
        param_names.append(arg.arg)
        if hasattr(arg.annotation, 'id') and getattr(arg.annotation, 'id') is not None:
            param_types.append(arg.annotation.id)
        else:
            param_types.append(None)
        if idx < pad:
            param_defaults.append(None)
        else:
            param_defaults.append(getattr(ast_function.args.defaults[idx - pad], 'value'))
    # process signature
    if class_name:
        func_name = f'{class_name}.{ast_function.name}('
    else:
        func_name = f'{ast_function.name}('
    sig_fragment = process_signature(func_name=func_name,
                                     param_names=param_names,
                                     param_defaults=param_defaults)
    func_fragment.appendChild(tags.div(cls='yap func-sig-content').appendChild(sig_fragment))
    # process docstring
    doc_str = ast.get_docstring(ast_function)
    doc_str_fragment = process_docstring(doc_str=doc_str,
                                         param_names=param_names,
                                         param_types=param_types)
    func_fragment.appendChild(tags.div(cls='yap func-doc-str-content').appendChild(doc_str_fragment))
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
                     cls='yap docstring'))
    # iterate the module's members
    for item in ast_module.body:
        # process functions
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            func_fragment = process_function(item, yap_config)
            if func_fragment is not None:
                dom_fragment.appendChild(func_fragment)
        # process classes and nested methods
        elif isinstance(item, ast.ClassDef):
            process_class(item, lines, yap_config)
    return lines
