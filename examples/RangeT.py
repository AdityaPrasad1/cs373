#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ---------
# RangeT.py
# ---------

# https://docs.python.org/3/library/functions.html#func-range

from typing   import Iterable, Iterator
from unittest import main, TestCase

class my_range_1 (Iterable[int]) :
    class iterator (Iterator[int]) :
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

    def __init__ (self, b: int, e: int) -> None :
        self.b = b
        self.e = e

    def __getitem__ (self, i) :
        return self.b + i

    def __iter__ (self) -> Iterator[int] :
        return my_range_1.iterator(self.b, self.e)

class my_range_2 (Iterable[int]) :
    def __init__ (self, b: int, e: int) -> None :
        self.b = b
        self.e = e

    def __getitem__ (self, i) :
        return self.b + i

    def __iter__ (self) -> Iterator[int] :
        b = self.b
        while b != self.e :
            yield b
            b += 1

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            my_range_1,
            my_range_2,
            range]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 2)
                a = []
                for v in x :
                    a.append(v)
                self.assertEqual(a, [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 3)
                a = []
                for v in x :
                    a.append(v)
                self.assertEqual(a, [2])

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 4)
                a = []
                for v in x :
                    a.append(v)
                self.assertEqual(a, [2, 3])

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 5)
                self.assertEqual(x[0], 2)
                self.assertEqual(x[1], 3)
                self.assertEqual(x[2], 4)

    def test_5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 5)
                self.assertEqual(list(x), [2, 3, 4])
                self.assertEqual(list(x), [2, 3, 4])

if __name__ == "__main__" : # pragma: no cover
    main()
