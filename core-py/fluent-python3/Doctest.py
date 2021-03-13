"""
>>> add(10, 20)
30
>>> add(20, 40)
60
>>> add(87, 9)
96
"""


def add(a, b):
    """
    >>> add(10, 20)
    30
    >>> add(20, 40)
    60
    >>> add(87, 9)
    96
    """

    return a + b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
