# List comprehension is more readable

# without using list comprehension
symbols = '$¢£¥€¤'

codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# using list comprehension
codes = [ord(symbol) for symbol in symbols]
print(codes)

# Python2.7

"""
>>> x = 'my precious'
>>> dummy = [x for x in 'ABC']
>>> x
'C'
"""

# Python3+

"""
>>> x = 'ABC'
>>> dummy = [ord(x) for x in x]
>>> x
'ABC'
"""

# using list comprehension
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

# using map and filter
# map(func, iterable) return iterable
# filter(func or None, iterable) return filter object

"""
filter(function or None, iterable) --> filter object

  Return an iterator yielding those items of iterable for which function(item)
  is true. If function is None, return the items that are true.
"""
# ord(character) return the ascii value of this character
# map(ord, symbols) return map object. which is an iterable

"""
>>> dir(a)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(filter)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(map) == dir(filter)
True
"""

if '__iter__' in dir(map(ord, symbols)):
    print("map() object is an iterable.")

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

# Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))
