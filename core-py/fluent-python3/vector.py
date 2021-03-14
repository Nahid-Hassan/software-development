# hypot is use for calculating euclidian distance
from math import hypot
import doctest


class Vector:
    # docstring for doctest

    """
    >>> v1 = Vector(3, 5)
    >>> v1
    Vector (3, 5)
    >>> v2 = Vector(2, 3)
    >>> abs(v1)
    5.8309518948453
    >>> abs(v2)
    3.6055512754639896
    >>> v1 * 3
    Vector (9, 15)
    >>> v2 * 3
    Vector (6, 9)
    >>> v1 + v2
    Vector (5, 8)
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # representation of vector is something like Vector(3, 5)
    def __repr__(self):
        # return f'Vector ({self.x}, {self.y})'
        return 'Vector (%r, %r)' % (self.x, self.y)

    # return the euclidian distance
    # r = sqrt(x ** 2, y ** 2)
    def __abs__(self):
        return hypot(self.x, self.y)

    # return scalar multiplication of vector
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # perform vector addition
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # return is object is empty or not
    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)


if __name__ == '__main__':
    # perform doctest
    # doctest.testmod()
    # from command line
    # python -m doctest -v vector.py

    v1 = Vector(3, 4)
    v2 = Vector(5, 4)

    print(v1)
    print(abs(v1))
    print(v1 + v2)
    print(v1 * 3)
    print(bool(v1))
