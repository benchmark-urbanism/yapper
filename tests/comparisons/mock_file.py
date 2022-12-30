"""
module docstring content
more content
"""
from typing import Optional, Union

GLOBAL_VAR = 0.9


def mock_function(param_a: int, param_b: Union[int, float] = 2) -> Optional[Union[int, float]]:
    """
    A mock function returning a sum of param_a and param_b if positive numbers, else None

    Parameters
    ----------
    param_a: int
        A *test* _param_.
    param_b: float
        Another *test* _param_.

        | col A |: col B |
        |-------|--------|
        | boo   | baa
        more content across broken line|

    Returns
    -------
    summed_number: float
        The sum of _param_a_ and _param_b_.
    None
        None returned if values are negative.

    Raises
    ------
    ValueError
        Raises value error if params are not numbers.

    Examples
    -----
    ```python
    print(mock_function(1, 2))
    # prints 3
    print("boo")
    print('boo')
    ```

    Random text

    _Random table_

    | col A |: col B |
    |-------|--------|
    | boo   | baa    |

    """
    if param_a < 0 or param_b < 0:
        return None
    if not isinstance(param_a, (int, float)) or not isinstance(param_b, (int, float)):
        raise ValueError("Whoops")
    return param_a + param_b


class ParentClass:
    """
    A parent class

    :::warning
    An admonition
    :::
    """

    parent_prop: str
    """Parent prop description."""

    def __init__(self, a_param: str):
        """
        Parent initialisation.

        Parameters
        ----------
        a_param: str
            A parameter.
            :::note
            Another admonition
            :::
        """
        self.parent_prop = a_param

    def _boo(self):
        """should be ignored."""
        pass

    def no_param(self):
        """No params."""
        pass


class ChildClass(ParentClass):
    """
    A child class
    """

    def __init__(self, param_c: float = 1.1, param_d: float = GLOBAL_VAR):
        """
        Child initialisation.

        Parameters
        ----------
        param_c: float
            Yet another test param.
        param_d: float
            And another.
        """
        super().__init__("boo")
        self.param_c = param_c
        self.param_d = param_d

    @property
    def param_e(self):
        """A property describing property param_e"""
        return self.param_c + self.param_d

    @param_e.setter
    def param_e(self, param_e: float):
        self.param_c = param_e - self.param_d

    def hello(self) -> str:
        """
        A random class method returning "hello"

        Returns
        -------
        str: saying_hello
            A string saying "hello"
        """
        saying_hello = "hello"
        return saying_hello
