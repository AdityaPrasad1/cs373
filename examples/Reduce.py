#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# Reduce.py
# ---------

# https://docs.python.org/3.6/library/functools.html

from functools import reduce
from operator  import add, mul, sub

def test1 () :
    assert reduce(add,  [2, 3, 4], 0) == 9

def test2 () :
    assert reduce(mul,  (2, 3, 4), 1) == 24

def test3 () :
    assert reduce(sub,  {2, 3, 4}, 2) == -7

def test4 () :
    assert reduce(None, [],        3) == 3

def main () :
    for n in range(4) :
        eval("test" + str(n + 1) + "()")

if __name__ == "__main__" : # pragma: no cover
    print("Reduce.py")
    main()
    print("Done.")
