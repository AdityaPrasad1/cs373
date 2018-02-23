# -----------
# Mon, 19 Feb
# -----------

a = [2, 3, 4]
print(type(a))    # list

p = iter(a)       # a.__iter__()
print(type(p))    # list iterator

print(p is a)     # False

for v in a :       # iterable over anything
    ...

for v, w in a :    # iterable over iterables of length 2
    ...

for u, _, _ in a : # ignore the second and third elements
    ...

list(...)
tuple(...)
set(...)

a = [2, 3, 4]
print(a[1])             # 3
print(a.__getitem__(1)) # 3

a = [2, 3, 4]
print(type(a)) # list

p = iter(a)
print(type(p)) # list iterator

print(p is a)  # False

q = iter(p)
print(type(q)) # list iterator

print(q is a)  # False
print(q is p)  # True

for v in a :   # iterate over an iterable
    ...

for v in p :   # iterate over an iterator
    ...

"""
all iterables ARE NOT iterators
all iterators ARE     iterables

iterables (e.g. list, set, range)                   ARE NOT exhaustible
iterators (e.g. list iterator, range iterator, zip) ARE exhaustible

iterators (e.g. list iterator, range iterator, count, zip) are all lazy constant time, constant space objects

being lazy (e.g. zip) accommodates infinite structures (e.g. count)
"""
