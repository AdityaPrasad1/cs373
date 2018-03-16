#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = dangerous-default-value
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------------
# FunctionDefaults.py
# -------------------

def f (x, y, z=5) :
    return [x, y, z]

def test1 () :
    assert f(2, 3)    == [2, 3, 5]
    assert f(2, 3, 4) == [2, 3, 4]

# def g (x, y=5, z) : # SyntaxError: non-default argument follows default argument
#     return [x, y, z]

def g (x=5, y=6, z=7) :
    return [x, y, z]

def test2 () :
    assert g()        == [5, 6, 7]
    assert g(2)       == [2, 6, 7]
    assert g(2, 3)    == [2, 3, 7]
    assert g(2, 3, 4) == [2, 3, 4]
    assert g(2, z=4)  == [2, 6, 4]

def h1 (x=[]) : # mutable default
    x += [2]
    return x

def test3 () :
    assert h1()    == [2]
    assert h1()    == [2, 2]
    assert h1([1]) == [1, 2]
    assert h1()    == [2, 2, 2]
    assert h1([1]) == [1, 2]

def h2 (x=()) : # immutable default
    x += (2,)
    return x

def test4 () :
    assert h2()     == (2,)
    assert h2()     == (2,)
    assert h2((1,)) == (1, 2)
    assert h2()     == (2,)
    assert h2((1,)) == (1, 2)

def h3 (x=None) :
    if x is None :
        x = []
    x += [2]
    return x

def test5 () :
    assert h3()     == [2]
    assert h3()     == [2]
    assert h3([1])  == [1, 2]
    assert h3()     == [2]
    assert h3([1])  == [1, 2]
    assert h3(None) == [2]

def main () :
    print("FunctionDefaults.py")
    for i in range(5) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
