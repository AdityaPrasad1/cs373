#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -----------------
# RangeIteratorT.py
# -----------------

from typing   import Iterator
from unittest import main, TestCase

class range_iterator_1 (Iterator[int]) :
    def __init__ (self, b: int, e: int) -> None :
        self.b = b
        self.e = e

    def __iter__ (self) -> Iterator[int] :
        return self

    def __next__ (self) -> int :
        if self.b == self.e :
            raise StopIteration()
        v = self.b
        self.b += 1
        return v

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            range_iterator_1,
            lambda b, e : iter(range(b, e))]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                p = f(2, 2)
                self.assertIs(p, iter(p))
                self.assertRaises(StopIteration, next, p)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                p = f(2, 3)
                self.assertIs(p, iter(p))
                self.assertEqual(next(p), 2)
                self.assertRaises(StopIteration, next, p)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                p = f(2, 4)
                self.assertIs(p, iter(p))
                self.assertEqual(next(p), 2)
                self.assertEqual(next(p), 3)
                self.assertRaises(StopIteration, next, p)

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                p = f(2, 5)
                self.assertIs(p, iter(p))
                a = []
                for v in p :
                    a.append(v)
                self.assertEqual(a, [2, 3, 4])

    def test_5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                p = f(2, 5)
                self.assertIs(p, iter(p))
                self.assertEqual(list(p), [2, 3, 4])
                self.assertEqual(list(p), [])

if __name__ == "__main__" : # pragma: no cover
    main()
