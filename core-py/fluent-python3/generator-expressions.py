"""
Generator Expressions
    To initialize tuples, arrays, and other types of sequences, you could also start from a
    listcomp, but a genexp saves memory because it yields items one by one using the iterator
    protocol instead of building a whole list just to feed another constructor.
    Genexps use the same syntax as listcomps, but are enclosed in parentheses rather than
    brackets.
"""
from array import array

symbols = '$¢£¥€¤'

gen_expr = tuple(ord(symbol) for symbol in symbols)
print(gen_expr)

# array
arr = array('I', (ord(symbol) for symbol in symbols))
print(arr)
