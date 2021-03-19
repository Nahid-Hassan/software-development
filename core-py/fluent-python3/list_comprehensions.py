# unicode character
symbols = '$¢£¥€¤'
codes = []

# create a list using for loop
for symbol in symbols:
    # ord(): return the ascii value
    codes.append(ord(symbol))

print(codes)

# using list comprehensions
codes = [ord(symbol) for symbol in symbols]
print(codes)

"""Listcomps No Longer Leak Their Variables"""
x = 'my precious'
dummy = [x for x in x]
print(dummy)
print(x)

"""Listcomps Versus map and filter"""
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

# filter(function, iter)
# map(function, iter)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
