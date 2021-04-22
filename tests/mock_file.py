def mock_function(param_a: str, param_b: int = 1) -> int:
    """
    A mock function for testing purposes

    Parameters
    ----------
    param_a
        A *test* _param_.
    param_b
        Another *test* _param_.

        | col A |: col B |
        |=======|========|
        | boo   | baa    |
    """
    pass

class MockClass:
    """
    A mock class for testing purposes.
    """

    def __init__(self, param_c: float = 1.1, param_d: float = 0.9):
        """
        Mock class initialisation

        Parameters
        ----------
        param_c
            Yet another test param.
        param_d
            And another.
        """
        self.param_c = param_c
        self.param_d = param_d

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
