# Fluent Python

## Table of Contents

- [Fluent Python](#fluent-python)
  - [Table of Contents](#table-of-contents)
    - [Python Data Model](#python-data-model)
      - [Doctest](#doctest)
      - [Data Model](#data-model)
    - [An Array of Sequences](#an-array-of-sequences)

### Python Data Model

#### Doctest

```py
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
```

#### Data Model

```py
def __repr__(self):
    # return f'Vector ({self.x}, {self.y})'
    return 'Vector (%r, %r)' % (self.x, self.y)

# return the euclidean distance
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

# return the len of the _cards
def __len__(self):
    return len(self._cards)

# now we can perform indexing, slicing, iteration operation
# easily.
# to understand the effect just comment out this function
# and try to perform above "slicing, indexing or iteration"
# operation
def __getitem__(self, position):
    return self._cards[position]
```

### An Array of Sequences

The standard library offers a rich selection of sequence types implemented in C:

- Container sequences

```text
    list , tuple , and collections.deque can hold items of different types.
```

- Flat sequences

```text
    str , bytes , bytearray , memoryview , and array.array hold items of one type.
```

Container sequences hold references to the objects they contain, which may be of any
type, while flat sequences physically store the value of each item within its own memory
space, and not as distinct objects. Thus, flat sequences are more compact, but they are
limited to holding primitive values like characters, bytes, and numbers.
Another way of grouping sequence types is by mutability:

- Mutable sequences

```text
    list , bytearray , array.array , collections.deque , and memoryview
```

- Immutable sequences

```text
    tuple , str , and bytes
```
