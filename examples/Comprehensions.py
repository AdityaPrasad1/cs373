#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = unidiomatic-typecheck
# pylint: disable = no-name-in-module

# -------------
# Indexables.py
# -------------

# https://docs.python.org/3.6/tutorial/datastructures.html

from types import GeneratorType

def test1 () :
    a = [2, 3, 4]
    b = []
    for v in a :
        b += [v * v]
    assert type(b) is list
    assert a       == [2, 3,  4]
    assert b       == [4, 9, 16]

def test2 () :
    a = [2, 3, 4]
    b = [v * v for v in a]       # list comprehension
    assert type(b) is list
    assert a       == [2, 3,  4]
    assert b       == [4, 9, 16]

def test3 () :
    a = [2, 3, 4]
    g = (v * v for v in a)          # generator
    assert hasattr(g, "__next__")
    assert hasattr(g, "__iter__")
    assert type(g) is GeneratorType
    assert g       is iter(g)
    assert a       == [2, 3,  4]
    assert list(g) == [4, 9, 16]
    assert list(g) == []

def test4 () :
    a = [2, 3, 4]
    m = map(lambda v : v * v, a)
    assert hasattr(m, "__next__")
    assert hasattr(m, "__iter__")
    assert type(m) is map
    assert m       is iter(m)
    assert a       == [2, 3,  4]
    assert list(m) == [4, 9, 16]
    assert list(m) == []

def test5 () :
    a = [2, 3, 4]
    g = (v * v for v in a)
    a += [5]
    assert a       == [2, 3,  4,  5]
    assert list(g) == [4, 9, 16, 25]
    assert list(g) == []
    a += [5]
    assert list(g) == []

def test6 () :
    a = [2, 3, 4]
    m = map(lambda v : v * v, a)
    a += [5]
    assert a       == [2, 3,  4,  5]
    assert list(m) == [4, 9, 16, 25]
    assert list(m) == []
    a += [5]
    assert list(m) == []

def test7 () :
    a = [2, 3, 4, 5, 6]
    b = []
    for v in a :
        if v % 2 :
            b += [v * v]
    assert a == [2, 3, 4,  5,  6]
    assert b == [   9,    25]

def test8 () :
    a = [2, 3, 4, 5, 6]
    b = [v * v for v in a if v % 2]
    assert a == [2, 3, 4,  5,  6]
    assert b == [   9,    25]

def test9 () :
    a = [2, 3, 4, 5, 6]
    g = (v * v for v in a if v % 2)
    assert a       == [2, 3, 4,  5,  6]
    assert list(g) == [   9,    25]
    assert list(g) == []

def test10 () :
    a = [2, 3, 4, 5, 6]
    f = filter(lambda v : v % 2, a)
    assert hasattr(f, "__next__")
    assert hasattr(f, "__iter__")
    assert type(f) is filter
    assert f       is iter(f)
    m = map(lambda v : v * v, f)
    assert a       == [2, 3, 4,  5,  6]
    assert list(m) == [   9,    25]
    assert list(f) == []
    assert list(m) == []

def test11 () :
    a = [2, 3, 4]
    b = [4, 5]
    c = []
    for v in a :
        for w in b :
            c += [v + w]
    assert a == [2, 3, 4]
    assert b == [4, 5]
    assert c == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
    assert c == [  6,   7,   7,   8,   8,   9]

def test12 () :
    a = [2, 3, 4]
    b = [4, 5]
    c = [v + w for v in a for w in b]
    assert a == [2, 3, 4]
    assert b == [4, 5]
    assert c == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
    assert c == [  6,   7,   7,   8,   8,   9]

def test13 () :
    a = [2, 3, 4]
    b = [4, 5]
    g = (v + w for v in a for w in b)
    assert a       == [2, 3, 4]
    assert b       == [4, 5]
    assert list(g) == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
    assert list(g) == []

def test14 () :
    s = {2, 3, 4}
    t = set()
    for v in s :
        t |= {v * v}
    assert s == {2, 3,  4}
    assert t == {4, 9, 16}

def test15 () :
    s = {2, 3, 4}
    t = {v * v for v in s}   # set comprehension
    assert s == {2, 3,  4}
    assert t == {4, 9, 16}

def test16 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    e = {}
    for k in d :
        e[k + 1] = d[k] + "xyz"
    assert d == {2: "abc",    3: "def",    4: "ghi"}
    assert e == {3: "abcxyz", 4: "defxyz", 5: "ghixyz"}

def test17 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    e = {k + 1: d[k] + "xyz" for k in d}                # dict comprehension
    assert d == {2: "abc",    3: "def",    4: "ghi"}
    assert e == {3: "abcxyz", 4: "defxyz", 5: "ghixyz"}

def main () :
    print("Comprehensions.py")
    for i in range(17) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
