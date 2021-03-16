# PEP 8 Style Guide

- Use `spaces` instead of **tabs** for indentation.
- Use `four spaces` for each level of syntactically significant indenting.
- Lines should be `79` characters in length or less.
- Continuations of `long expressions` onto additional lines should
be indented by `four extra spaces` from their normal indentation
level.

```py
sentence = 'In Python, whitespace is syntactically significant. Python \
    programmers are especially sensitive to the effects of whitespace on code \
    clarity. Follow these guidelines related to whitespace.'

print(sentence)
```

- In a file, `functions` and `classes` should be separated by `two` blank
lines.

```py
def add_two_nums(a, b):
    return a + b
# two lines gap
# two lines gap
class A:
    pass
```

- In a `class`, `methods` should be separated by `one` blank line.

```py
class A:

    def __init__(self):
        pass
    # one line
    def __repr__(self):
        pass
    # one line
    def add(self):
        pass
```

- In a `dictionary`, put `no whitespace` between each `key` and `colon`,
and put a `single space` before the corresponding `value` if it fits on
the same line.

```py
student_info = {
    # key(nospace):(single_space)value
    'name': 'Md. Nahid Hassan',
    'dept': 'Computer Science and Engineering'
}
```

- Put `one`—and only `one—space` before and after the `=` operator in a
variable assignment.

```py
# variable_name(one space)=(one space)value
name = 'Nahid Hassan'
```

- For type annotations, ensure that there is no separation between
the variable name and the colon, and use a space before the type
information.

```py
# Later added
```

## Naming

- Functions, variables, and attributes should be in lowercase_
underscore format.

```py
# function name
def add_two_numbers(a, b):
    pass

# variable name
full_name = 'Md. Nahid Hassan'

# attributes name
class A:
    full_name = "Md. Nahid Hassan"
```

- Protected instance attributes should be in _leading_underscore
format.

```py
# protected variable
_age = 23
_year = 1997

class A:

    _age = 34
    _year = 1988

    def __init__(self, name):
        self._name = name
```

- Private instance attributes should be in __double_leading_
underscore format.

```py
# protected variable
__age = 23
__year = 1997

class A:

    __age = 34
    __year = 1988

    def __init__(self, name):
        self.__name = name
```

- Classes (including exceptions) should be in CapitalizedWord
format.

```py
class Student:
    pass


class Course:
    pass

class Dept:
    pass
```

- Module-level constants should be in ALL_CAPS format.

```py
# pwd
# /media/nahid/..../stack
# ls
# __init__.py stack.py

# stack.py

class Student:

    MIN_AGE = 20
    MAX_AGE = 32
    DEBUG = tRUE
```

- Instance methods in classes should use self , which refers to the
object, as the name of the first parameter.

```py
class A:

    # instance method
    def __init__(self, something):
        self.something = something

    # instance method
    def display(self):
        print(self.something)
```

- Class methods should use cls , which refers to the class, as the
name of the first parameter.

```python
class A:

    # instance method
    def __init__(self):
        pass

    #classmethod
    @classmethod
    def class_method(cls):
        pass
```

## Expression and Statements

- Use `inline negation` ( `if a is not b` ) instead of negation of positive
expressions ( `if not a is b` ).

```py
# No use
if not a is b:
    pass

# use
if a is not b:
    pass
```

- Don’t check for `empty` containers or sequences (like `[]` or `''` )
by comparing the length to zero ( `if len(somelist) == 0` ). Use
`if not somelist` and assume that empty values will implicitly
evaluate to `False`.

```py
# Don't Do
empty_list = []

if len(empty_list) == 0:
    # write your code here

# Do
if not empty_list:
    # write your code here
```

- The same thing goes for **non-empty** containers or sequences (like
`[1]` or `'hi'` ). The statement `if somelist` is implicitly True for non-
empty values.

```py
# Don't Do
single_item_list = []

if len(single_item_list) == 0:
    # write your code here

# Do
if single_item_list:
    # write your code here
```

- Avoid single-line if statements, for and while loops, and except
compound statements. Spread these over multiple lines for
clarity.

- If you can’t fit an expression on one line, surround it with
parentheses and add line breaks and indentation to make it easier to
read.

```py
a = 10
expression = [{(a + 34) + 343 / 343} + (-90 + 34) \
    10 + 3043 + a]
```

- Prefer surrounding multiline expressions with parentheses over
using the `\ line continuation character`.

## Import

- Always put import statements (including from x import y ) at the
top of a file.

```py
# top of the code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

- Always use absolute names for modules when importing them, not
names relative to the current module’s own path. For example, to
import the foo module from within the bar package, you should
use from bar import foo , not just import foo .

```py
from os import path
from random import randint
from collections import Counter
```

- If you must do relative imports, use the explicit syntax
from . import foo .

```py
from . import views
```

- Imports should be in sections in the following order: standard
library modules, third-party modules, your own modules. Each
subsection should have imports in alphabetical order.

**Note**:

> The `Pylint` tool (<https://www.pylint.org>) is a popular static analyzer for Python source code. Pylint provides automated enforcement of the PEP 8 style guide and detects many other types of common errors in Python programs. Many IDEs and editors also include linting tools or support similar plug-ins.
