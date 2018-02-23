#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring
# pylint: disable = unidiomatic-typecheck

# ------------
# Operators.py
# ------------

# https://docs.python.org/3/library/operator.html
# https://graphics.stanford.edu/~seander/bithacks.html

from copy     import copy, deepcopy
from operator import add

def test1 () :
    i = 2
    j = 3
    k = i + j     # addition
    assert i == 2
    assert j == 3
    assert k == 5

def test2 () :
    i = 2
    j = 3
    k = add(i, j)
    assert i == 2
    assert j == 3
    assert k == 5

def test3 () :
    i = 4
    j = 2
    f = i / j               # true division
    assert i == 4
    assert j == 2
    assert type(f) is float
    assert str(f) == "2.0"

def test4 () :
    i = 5
    j = 2
    k = i // j            # floor division
    assert i == 5
    assert j == 2
    assert type(k) is int
    assert k == 2

def test5 () :
    f = 5.0
    j = 2
    g = f // j              # floor division
    assert f == 5.0
    assert j == 2
    assert type(g) is float
    assert str(g) == "2.0"

def test6 () :
    i = 2
    j = 3
    k = i ** j    # exponentiation
    assert i == 2
    assert j == 3
    assert k == 8

def test7 () :
    i = 10
    j = 12
    i, j = j, i
    assert i == 12
    assert j == 10

def test8 () :
    i = 3
    j = 5
    k = 7
    l = 8
    assert (i < j) and (j < k) and (k < l)
    assert i < j < k < l

def test9 () :
    s = "abc"
    assert s[1] == "b"
    #s[1] = "d"        # TypeError: 'str' object does not support item assignment

def test10 () :
    a = [2, 3, 4]
    assert a[1] == 3 # list index
    a[1] = 5
    assert a[1] == 5

def test11 () :
    u = (2, 3, 4)
    assert u[1] == 3 # tuple index
    #u[1] = 5        # TypeError: 'tuple' object does not support item assignment

def test12 () :
    s = "a"
    t = "bc"
    m = s + t             # string concatenation
    assert m is not "abc"
    assert m ==     "abc"

def test13 () :
    a = [2]
    b = [3, 4]
    c = a + b                 # list concatenation
    assert c is not [2, 3, 4]
    assert c ==     [2, 3, 4]
    assert c !=     (2, 3, 4)

def test14 () :
    u = (2,)
    v = (3, 4)
    w = (u + v)               # tuple concatenation
    assert w is not (2, 3, 4)
    assert w ==     (2, 3, 4)
    assert w !=     [2, 3, 4]

def test15 () :
    s = "abc"
    t = 2 * s                # string replication
    assert t is not "abcabc"
    assert t ==     "abcabc"

def test16 () :
    a = [2, 3, 4]
    b = 2 * a                          # list replication
    assert b is not [2, 3, 4, 2, 3, 4]
    assert b ==     [2, 3, 4, 2, 3, 4]

def test17 () :
    u = (2, 3, 4)
    v = 2 * u                          # tuple replication
    assert u is not (2, 3, 4, 2, 3, 4)
    assert v ==     (2, 3, 4, 2, 3, 4)

def test18 () :
    a = [2, 3, 4]
    assert a[1]     == 3
    assert a[-1]    == 4
    assert a[1:2]   == [3]
    assert a[1:3]   == [3, 4]
    assert a[0:3]   == [2, 3, 4]
    assert a[0:3:2] == [2, 4]
    assert a[:]     == [2, 3, 4]

def test19 () :
    a = [2, 3, 4]
    b = a[:]
    assert a is not b
    assert a ==     b
    b[1] += 1
    assert a[1] == 3
    assert b[1] == 4

def test20 () :
    u = (2, 3, 4)
    v = u[:]
    assert u is v

def test21 () :
    a = [2, 3, 4]
    b = copy(a)
    assert a is not b
    assert a ==     b
    b[1] += 1
    assert a[1] == 3
    assert b[1] == 4

def test22 () :
    u = (2, 3, 4)
    v = copy(u)
    assert u is v

def test23 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = b[:]
    assert b    is not c
    assert b    ==     c
    assert b[1] is     c[1]

def test24 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = copy(b)
    assert b    is not c
    assert b    ==     c
    assert b[1] is     c[1]

def test25 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = deepcopy(b)
    assert b    is not c
    assert b    ==     c
    assert b[1] is not c[1]
    assert b[1] ==     c[1]

def test26 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b += [5]
    assert a == [2, 3, 4, 5]
    assert a is b

def test27 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b += (5,)
    assert a == [2, 3, 4, 5]
    assert a is b

def test28 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b = b + [5]
    assert a == [2, 3, 4]
    assert b == [2, 3, 4, 5]

def test29 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    #b = b + (5,) # TypeError: can only concatenate list (not "tuple") to list

def test30 () :
    x = (2, 3, 4)
    y = x
    assert x is y
    y += (5,)
    assert x == (2, 3, 4)
    assert y == (2, 3, 4, 5)

def test31 () :
    u = (2, 3, 4)
    v = u
    assert u is v
    #v += [5]     # TypeError: can only concatenate tuple (not "list") to tuple

def test32 () :
    x = (2, 3, 4)
    y = x
    assert x is y
    y = y + (5,)
    assert x == (2, 3, 4)
    assert y == (2, 3, 4, 5)

def test33 () :
    u = (2, 3, 4)
    v = u
    assert u is v
    #v = v + [5]  # TypeError: can only concatenate tuple (not "list") to tuple

def main () :
    print("Operators.py")
    for i in range(33) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
