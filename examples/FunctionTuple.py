#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------------
# FunctionTuple.py
# ----------------

def f (x, y, *z) :
    return [x, y, z]

def test1 () :
    assert f(2, 3)       == [2, 3, ()]
    assert f(2, 3, 4)    == [2, 3, (4,)]
    assert f(2, 3, 4, 5) == [2, 3, (4, 5)]

def test2 () :
    t = (3, 4)
    assert f(2, 5,  t)  == [2, 5, ((3, 4),)]
    assert f(2, 5, *t)  == [2, 5, (3, 4)]
    assert f(2, *t)     == [2, 3, (4,)]
    assert f(*t)        == [3, 4, ()]

def test3 () :
    u = (2,)
    assert f(y=3, *u)  == [2, 3, ()]
    assert f(*u,  y=3) == [2, 3, ()]

def test4 () :
    d = {"y" : 3, "x" : 2}
    assert f(**d) == [2, 3, ()]

def test5 () :
    d = {"y" : 3}
    assert f(2,   **d) == [2, 3, ()]
    assert f(x=2, **d) == [2, 3, ()]

def main () :
    print("FunctionTuple.py")
    for i in range(5) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
