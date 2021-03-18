"""
Things to Remember
✦ bytes
contains sequences of 8-bit values, and str contains
sequences of Unicode code points.
✦
Use helper functions to ensure that the inputs you operate on
are the type of character sequence that you expect (8-bit values,
UTF-8-encoded strings, Unicode code points, etc).
✦ bytes
and str instances can’t be used together with operators (like
> , == , + , and % ).
✦ If you want to read or write binary data to/from a file, always open
the file using a binary mode (like 'rb' or 'wb' ).
✦ If you want to read or write Unicode data to/from a file, be care-
ful about your system’s default text encoding. Explicitly pass the
encoding parameter to open if you want to avoid surprises.
"""


# bytes string
a = b'h\x65llo'
print(list(a))  # [104, 101, 108, 108, 111]
print(a)  # b'hello'

# character string(Unicode string)
a = 'a\u0300 propos'
print(list(a))  # ['a', '`', ' ', 'p', 'r', 'o', 'p', 'o', 's']
print(a)  # à propos

"""
    Unicode  -- Call str.encode()   --->  Binary
    Binary   -- call bytes.decode() ---> Unicode
"""

"""
>>> isinstance(b'foo', bytes)
True
>>> isinstance('foo', bytes)
False
>>> isinstance('foo', str)
True
"""


def to_str(bytes_or_str):
    """
        The first function takes a bytes or str instance and always returns
        a str.
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value  # Instance of str


print(to_str(b'foo'))
print(to_str('bar'))

# The first issue is that bytes and str seem to work the same way, but
# their instances are not compatible with each other, so you must be
# deliberate about the types of character sequences that you’re passing
# around.
# By using the + operator, you can add bytes to bytes and str to str ,
# respectively:

print(b'one' + b'two')
print('one' + 'two')

"""
>>> b'ab' + 'ab'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't concat str to bytes
>>>
"""
# Same for > < and == operator.
# == operator allways returns false.

# OK!!!!!!!!!
assert b'red' > b'blue'
assert 'red' > 'blue'

# Not OK!!!!!!!!!!!
# assert b'red' > 'blue'
# assert 'red' > b'blue'

"""
Traceback ...
TypeError: '>' not supported between instances of 'str' and
 ̄'bytes'
"""

"""
The % operator works with format strings for each type, respectively:
print(b'red %s' % b'blue')
print('red %s' % 'blue')
>>>
b'red blue'
red blue
"""

# 'w' for text mode for str string
# 'wb' for binary mode for bytes string

with open('data.bin', 'wb') as f:
    f.write(b'h\x65llo')

with open('data.bin', 'rb') as f:
    data = f.read()
    print(data)

    print(to_str(data))

with open('data.bin', 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

with open('data.bin', 'r', encoding='latin-1') as f:
    data = f.read()
assert data == 'ñòóôõ'
