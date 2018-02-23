#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# StrCmpT.py
# ----------

from unittest import main, TestCase

def strcmp (s: str, t: str) -> int :
    return (s > t) - (s < t)

class MyUnitTests (TestCase) :
    def test1 (self) :
        self.assertEqual(strcmp("",    ""),    0)

    def test2 (self) :
        self.assertEqual(strcmp("abc", "abc"), 0)

    def test3 (self) :
        self.assertGreater(strcmp("abc", "ab"),  0)

    def test4 (self) :
        self.assertGreater(strcmp("abc", "aba"), 0)

    def test5 (self) :
        self.assertLess(strcmp("ab",  "abc"), 0)

    def test6 (self) :
        self.assertLess(strcmp("aba", "abc"), 0)

if __name__ == "__main__" : # pragma: no cover
    main()
