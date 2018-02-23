#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests1.py
# -------------

# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods

from unittest import main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test1 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test2 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test3 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" : # pragma: no cover
    main()

""" #pragma: no cover
% UnitTests1T.py
FFF
======================================================================
FAIL: test1 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests1.py", line 31, in test1
    self.assertEqual(cycle_length( 1), 1)
  File "UnitTests1.py", line 26, in cycle_length
    assert c > 0
AssertionError

======================================================================
FAIL: test2 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests1.py", line 34, in test2
    self.assertEqual(cycle_length( 5), 6)
AssertionError: 5 != 6

======================================================================
FAIL: test3 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "UnitTests1.py", line 37, in test3
    self.assertEqual(cycle_length(10), 7)
AssertionError: 6 != 7

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)
"""
