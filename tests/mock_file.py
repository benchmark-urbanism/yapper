"""
module docstring content
more content
"""

def mock_function(param_a: int,
                  param_b: int = 2) -> int | str:
    """
    A mock function returning a sum of param_a and param_b if positive numbers

    Parameters
    ----------
    param_a
        A *test* _param_.
    param_b
        Another *test* _param_.

        | col A |: col B |
        |=======|========|
        | boo   | baa    |

    Returns
    -------
    summed_number
        The sum of _param_a_ and _param_b_ else "whoops" if negative numbers.

    Notes
    -----
    ```python
    print(mock_function(1, 2))
    # prints 3
    ```
    """
    if param_a < 0 or param_b < 0:
        return 'whoops'
    return param_a + param_b


class ParentClass:
    """
    A parent class
    """
    parent_prop: str

    def __init__(self):
        """
        Parent initialisation.
        """
        self.parent_prop = 'bee'


class ChildClass(ParentClass):
    """
    A child class
    """

    def __init__(self, param_c: float = 1.1, param_d: float = 0.9, **kwargs: dict):
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
        super().__init__()
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
        saying_hello
            A string saying "hello"
        """
        saying_hello = 'hello'
        return saying_hello
