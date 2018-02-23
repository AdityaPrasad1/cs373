#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------------
# RangeIterator.py
# ----------------

def test1 () :
    x = range(2, 2)
    p = iter(x)
    assert p is iter(p)
    try :
        next(p)
    except StopIteration :
        pass

def test2 () :
    x = range(2, 3)
    p = iter(x)
    assert p is iter(p)
    assert next(p) == 2
    try :
        next(p)
    except StopIteration :
        pass

def test3 () :
    x = range(2, 4)
    p = iter(x)
    assert p is iter(p)
    assert next(p) == 2
    assert next(p) == 3
    try :
        next(p)
    except StopIteration :
        pass

def test4 () :
    x = range(2, 5)
    p = iter(x)
    assert p is iter(p)
    a = []
    for v in p :
        a.append(v)
    assert a == [2, 3, 4]

def test5 () :
    x = range(2, 5)
    p = iter(x)
    assert p is iter(p)
    assert list(p) == [2, 3, 4]
    assert list(p) == []

def main () :
    for n in range(5) :
        eval("test" + str(n + 1) + "()")

if __name__ == "__main__" : # pragma: no cover
    print("RangeIterator.py")
    main()
    print("Done.")
