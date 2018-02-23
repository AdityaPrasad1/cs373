#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------
# Factorial.py
# ------------

# https://docs.python.org/3.6/library/math.html

from math import factorial

def test1 () :
    assert factorial(0) == 1

def test2 () :
    assert factorial(1) == 1

def test3 () :
    assert factorial(2) == 2

def test4 () :
    assert factorial(3) == 6

def test5 () :
    assert factorial(4) == 24

def test6 () :
    assert factorial(5) == 120

def main () :
    print("Factorial.py")
    for i in range(6) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
