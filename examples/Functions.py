#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = cell-var-from-loop
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ------------
# Functions.py
# ------------

def square1 (v) :
    return v ** 2

def test1 () :
    a = [2, 3, 4]
    m = map(square1, a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []

class square2 :
    def __call__ (self, v) :
        return v ** 2

def test2 () :
    a = [2, 3, 4]
    m = map(square2(), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []

class square3 :
    def __init__ (self, n) :
        self.n = n

    def __call__ (self, v) :
        return v ** self.n

def test3 () :
    a = [2, 3, 4]
    n = 2
    m = map(square3(n), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []

def test4 () :
    a = [2, 3, 4]
    m = map(lambda v : v ** 2, a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []

def test5 () :
    a = [2, 3, 4]
    n = 2
    m = map(lambda v : v ** n, a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []

def test6 () :
    a = [2, 3, 4]
    n = 1
    m = map(lambda v : v ** n, a)
    n = 2
    assert list(m) == [4, 9, 16]
    assert list(m) == []

def test7 () :
    a  = [2, 3, 4]
    fs = [lambda v : v ** n for n in range(3)]
    ms = [map(f, a) for f in fs]
    assert [list(m) for m in ms] == [[4, 9, 16], [4, 9, 16], [4, 9, 16]]
    assert [list(m) for m in ms] == [[],         [],         []]

def main () :
    print("Functions.py")
    for i in range(7) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
