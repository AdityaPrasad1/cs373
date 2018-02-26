#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# Map1.py
# -------

# https://docs.python.org/3/library/functions.html#map

def test1 () :
    m = map(lambda x : x ** 2, [2, 3, 4])
    assert hasattr(m, "__next__")
    assert hasattr(m, "__iter__")
    assert iter(m) is m
    assert list(m) == [4, 9, 16]
    assert list(m) == []

def test2 () :
    m = map(lambda x : x ** 2, {2, 3, 4})
    assert set(m) == {4, 9, 16}
    assert set(m) == set()

def test3 () :
    m = map(None, ())
    assert list(m) == []

def main () :
    for n in range(3) :
        eval("test" + str(n + 1) + "()")

if __name__ == "__main__" : # pragma: no cover
    print("Map.py")
    main()
    print("Done.")
