#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# ------------
# Coverage1.py
# ------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(1), 1)

if __name__ == "__main__" : # pragma: no cover
    main()

""" #pragma: no cover
% which coverage
/usr/local/bin/coverage



% coverage --version
Coverage.py, version 4.4.2 with C extension
Documentation at https://coverage.readthedocs.io



% coverage --help
...



% coverage run --branch Coverage1.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% coverage report -m
Name           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------
Coverage1.py      16      4      4      1    61%   20-24, 19->20
"""
