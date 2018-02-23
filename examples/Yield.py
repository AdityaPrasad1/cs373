#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# --------
# Yield.py
# --------

def f () :
    yield 2
    yield 3
    yield 4

def test1 () :
    p = f()
    assert p is iter(p)
    n = next(p)
    assert n == 2
    n = next(p)
    assert n == 3
    n = next(p)
    assert n == 4
    try :
        n = next(p)
    except StopIteration :
        pass

def test2 () :
    p = f()
    assert list(p) == [2, 3, 4]
    assert list(p) == []

def g () :
    for v in [2, 3, 4] :
        yield v

def test3 () :
    p = g()
    assert p is iter(p)
    n = next(p)
    assert n == 2
    n = next(p)
    assert n == 3
    n = next(p)
    assert n == 4
    try :
        n = next(p)
    except StopIteration :
        pass

def test4 () :
    p = g()
    assert list(p) == [2, 3, 4]
    assert list(p) == []

def main () :
    print("Yield.py")
    for i in range(4) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
