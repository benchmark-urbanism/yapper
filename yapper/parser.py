"""
Uses docspec to parse docstrings to markdown.

Intended for use with static site generators where further linting / linking / styling is done downstream.

Loosely based on Numpy-style docstrings.

Automatically infers types from signature typehints. Explicitly documented types are NOT supported in docstrings.
"""
import ast
import logging
import pathlib

import docstring_parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

line_break_chars = ['-', '_', '!', '|', '>', ':']


def _is_property(mem):
    if mem.decorations is not None:
        for dec in mem.decorations:
            if dec.name == 'property':
                return True
    return False


def _is_setter(mem):
    if mem.decorations is not None:
        for dec in mem.decorations:
            if 'setter' in dec.name:
                return True
    return False


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
    if class_name is not None:
        class_name_esc = class_name.replace('_', '\_')
        # if a class definition use the class template
        if isinstance(member, docspec.Class):
            # when the class is passed-in directly its name is captured in the member_name
            lines.append(config['class_name_template'].format(class_name=class_name_esc))
        # if the class __init__, then display the class name and .__init__
        elif class_name and member.name == '__init__':
            lines.append(config['function_name_template'].format(function_name=f'{class_name_esc}'))
        # if a class property
        elif class_name is not None and _is_property(member):
            lines.append(config['class_property_template'].format(prop_name=f'{class_name_esc}.{member_name}'))
        # if a class method
        elif class_name is not None:
            lines.append(config['function_name_template'].format(function_name=f'{class_name_esc}.{member_name}'))
        if hasattr(member, 'args') and not _is_property(member):
            # prepare the signature string - use member.name instead of escaped versions
            if class_name is not None and member.name == '__init__':
                signature = f'{class_name}('
            elif class_name is not None:
                signature = f'{class_name}.{member.name}('


def process_function(ast_function: ast.FunctionDef,
                     lines: list[str],
                     config: dict[str, str]):
    """ """
    # don't process private members
    if ast_function.name.startswith('_') and not ast_function.name == '__init__':
        return
    # keep track of the arguments and their types for automatically building function parameters later-on
    arg_types_map = {}
    # escape underscores
    func_name = ast_function.name.replace('_', '\_')
    lines.append(config['function_name_template'].format(function_name=func_name))
    # extract parameters
    param_names = []
    param_types = []
    for arg in ast_function.args.args:
        param_names.append(arg.arg)
        if hasattr(arg.annotation, 'id') and getattr(arg.annotation, 'id') is not None:
            param_types.append(arg.annotation.id)
        else:
            param_types.append(None)
    param_defaults = [None] * (len(ast_function.args.args) - len(ast_function.args.defaults))
    for default in ast_function.args.defaults:
        param_defaults.append(getattr(default, 'value'))
    # process signature
    signature = f'{ast_function.name}('
    # the spacer is used for lining up wrapped lines
    spacer = len(signature)
    for idx, (param_name, param_default) in enumerate(zip(param_names, param_defaults)):
        param = f'{param_name}'
        if param_default is not None:
            param += f'={param_default}'
        # first argument is wedged against bracket
        if idx == 0:
            signature += param
        # other arguments start on a new line
        else:
            signature += f'{" " * spacer}{param}'
        # if not the last argument, add a comma
        if idx != len(param_names) - 1:
            signature += ',\n'
    # close the signature
    signature += ')'
    # add the return type if present
    if hasattr(ast_function.returns, 'id') and getattr(ast_function.returns, 'id') is not None:
        signature += f'\n{" " * spacer}-> {getattr(ast_function.returns, "id")}'
    # set into the template
    signature = config['signature_template'].format(signature=signature)
    lines.append(signature)
    # process the docstring
    doc_str = docstring_parser.parse(ast.get_docstring(ast_function))
    if doc_str is not None:
        # split the docstring at new lines
        splits = member.docstring.split('\n')
        # iter the docstring with a lookahead index
        splits_enum = enumerate(splits, start=1)
        try:
            # skip and go straight to headings if no introductory text
            if len(splits) > 1 and splits[1].startswith('---'):
                lookahead_idx, next_line = next(splits_enum)
            # otherwise, look for introductory text
            else:
                lookahead_idx, next_line, text_block = extract_text_block(splits_enum, splits)
                if len(text_block):
                    lines.append(text_block)
            # look for headings
            while lookahead_idx < len(splits):
                # break if not a heading
                if not splits[lookahead_idx].startswith('---'):
                    raise ValueError('Parser out of lockstep with headings.')
                heading = next_line.strip()
                lines.append(config['heading_template'].format(heading=heading))
                # skip the underscore line
                next(splits_enum)
                # if not param-type headings - just extract the text blocks
                if heading not in ['Parameters', 'Returns', 'Yields', 'Raises']:
                    lookahead_idx, next_line, text_block = extract_text_block(splits_enum, splits)
                    if len(text_block):
                        lines.append(text_block)
                # otherwise iterate the parameters and their indented arguments
                else:
                    # initial prime to move from heading to parameter name
                    lookahead_idx, next_line = next(splits_enum)
                    # Iterate nested parameters
                    while True:
                        # this parser doesn't process typehints, use typehints in function declarations instead
                        if ' ' in next_line.strip() or ':' in next_line.strip():
                            raise ValueError('Parser does not support types in docstrings. Use type-hints instead.')
                        # extract the parameter name
                        param_name = next_line.strip()
                        # process the indented parameter description
                        lookahead_idx, next_line, param_description = extract_text_block(splits_enum,
                                                                                         splits,
                                                                                         indented_block=True)
                        # only include type information for Parameters
                        if heading == 'Parameters':
                            param_type = arg_types_map[param_name]
                            param = config['param_template'].format(name=param_name,
                                                                    type=param_type,
                                                                    description=param_description)
                        else:
                            param = config['return_template'].format(name=param_name,
                                                                     description=param_description)
                        lines.append(param)
                        # break if a new heading found
                        if lookahead_idx == len(splits) or splits[lookahead_idx].startswith('---'):
                            break
        # catch exhausted enum
        except StopIteration:
            pass


def parse(module_path: pathlib.Path,
          ast_module: ast.Module,
          yap_config: dict):
    """ """
    lines = []
    # frontmatter
    if yap_config['frontmatter_template'] is not None:
        lines.append(yap_config['frontmatter_template'])
    # module name
    module_str = str(module_path)
    module_str = module_str.rstrip('.py')
    path_splits = module_str.split('/')
    path_splits = [ps for ps in path_splits if ps not in ['..', '.']]
    path_text = '.'.join(path_splits)
    path_text = path_text.replace('_', '\_')
    lines.append(yap_config['module_name_template'].format(module_name=str(path_text)))
    # module docstring
    module_docstring = ast.get_docstring(ast_module)
    if module_docstring is not None:
        lines.append(module_docstring.strip().replace('\n', ' '))
    if yap_config['toc_template'] is not None:
        lines.append(yap_config['toc_template'])
    # iterate the module's members
    for item in ast_module.body:
        # process functions
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            process_function(item, lines, yap_config)
        # process classes and nested methods
        elif isinstance(item, ast.ClassDef):
            process_class(item, lines, yap_config)
    return lines
