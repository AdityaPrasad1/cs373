#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = function-redefined
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = redefined-outer-name
# pylint: disable = singleton-comparison
# pylint: disable = too-few-public-methods
# pylint: disable = too-many-locals
# pylint: disable = unidiomatic-typecheck
# pylint: disable = unused-import

# --------
# Types.py
# --------

# https://docs.python.org/3.6/library/types.html

from collections import deque
from typing      import Dict, FrozenSet, List, Set, Tuple
from types       import FunctionType

def test1 () :
    b = bool()
    assert b          == False
    b = True
    assert b          == True
    assert type(b)    is bool
    assert type(bool) is type

def test2 () :
    i = int()
    assert i         == 0
    i = 2
    assert i         == 2
    assert type(i)   is int
    assert type(int) is type

def test3 () :
    f = float()
    assert f           == 0.0
    f = 2.34
    assert f           == 2.34
    assert type(f)     is float
    assert type(float) is type

def test4 () :
    c = complex()
    assert c             == 0 + 0j
    c = complex(2, 3)
    assert c             == 2 + 3j
    assert type(c)       is complex
    assert type(complex) is type

def test5 () :
    s = str()
    assert s         == ""
    s = "abc"
    assert s         == "abc"
    assert type(s)   is str
    assert type(str) is type

def test6 () :
    a = list()
    assert a          == []
    a = [2, 3, 4]
    assert a          == [2, 3, 4]
    assert type(a)    is list
    assert type(list) is type

def test7 () :
    u = tuple()
    assert u           == ()
    u = (2, "abc", 3.45)
    assert u           == (2, "abc", 3.45)
    assert type(u)     is tuple
    assert type(tuple) is type

def test8 () :
    x = set()
    assert x         == set()     # not {}
    x = {2, 3, 4}
    assert x         == {2, 3, 4}
    assert type(x)   is set
    assert type(set) is type

def test9 () :
    y = frozenset()
    assert y               == frozenset()
    y = frozenset((2, 3, 4))
    assert y               == frozenset([2, 3, 4])
    assert type(y)         is frozenset
    assert type(frozenset) is type

def test10 () :
    d = dict()
    assert d          == {}
    d = {2: "abc", 3: "def", 4: "ghi"}
    assert d          == {2: "abc", 3: "def", 4: "ghi"}
    assert type(d)    is dict
    assert type(dict) is type

def test11 () :
    q = deque()
    assert q           == deque()
    q = deque((2, 3, 4))
    assert q           == deque((2, 3, 4))
    assert type(q)     is deque
    assert type(deque) is type

def test12 () :
    def g (v) :
        return v + 1
    assert type(g)            is FunctionType
    assert type(FunctionType) is type

def test13 () :
    h = lambda v : v + 1
    assert type(h) is FunctionType

def test14 () :
    class A :
        def __init__ (self, i, f) :
            self.i = i
            self.f = f

    z = A(2, 3.45)
    assert z       != A(2, 3.45)
    assert type(z) is A
    assert type(A) is type

    assert isinstance(z, A)
    assert isinstance(z, object)

    assert issubclass(A, object)

    assert type(type) is type

def main () :
    print("Types.py")
    for i in range(14) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
