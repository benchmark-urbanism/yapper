"""
module docstring content
more content
"""
from __future__ import annotations


def mock_function(param_a: int,
                  param_b: int | float = 2) -> int | float | None:
    """
    A mock function returning a sum of param_a and param_b if positive numbers, else None

    Parameters
    ----------
    param_a
        A *test* _param_.
    param_b
        Another *test* _param_.

        | col A |: col B |
        |-------|--------|
        | boo   | baa
        more content across broken line|

    Returns
    -------
    summed_number: int | float
        The sum of _param_a_ and _param_b_.
    None
        None returned if values are negative.

    Raises
    ------
    ValueError
        Raises value error if params are not numbers.

    Notes
    -----
    ```python
    print(mock_function(1, 2))
    # prints 3
    ```

    Random text

    _Random table_

    | col A |: col B |
    |-------|--------|
    | boo   | baa    |

    """
    if param_a < 0 or param_b < 0:
        return
    if not isinstance(param_a, (int, float)) or not isinstance(param_b, (int, float)):
        raise ValueError('Whoops')
    return param_a + param_b


class ParentClass:
    """
    A parent class
    """
    parent_prop: str

    def __init__(self, **kwargs: dict):
        """
        Parent initialisation.

        Parameters
        ----------
        kwargs
            Keyword args.
        """
        self.parent_prop = 'bee'

    def _boo(self):
        """ should be ignored """
        pass


class ChildClass(ParentClass):
    """
    A child class
    """

    def __init__(self,
                 param_c: float = 1.1,
                 param_d: float = 0.9,
                 **kwargs: dict):
        """
        Child initialisation.

        Parameters
        ----------
        param_c
            Yet another test param.
        param_d
            And another.
        kwargs
            Keyword args.
        """
        super().__init__(**kwargs)
        self.param_c = param_c
        self.param_d = param_d
        print(f'ignoring {kwargs}')

    @property
    def param_e(self):
        """ A property describing property param_e """
        return self.param_c + self.param_d

    def hello(self) -> str:
        """
        A random class method returning "hello"

        Returns
        -------
        str: saying_hello
            A string saying "hello"
        """
        saying_hello = 'hello'
        return saying_hello
