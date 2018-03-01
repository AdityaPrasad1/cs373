#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement
# pylint: disable = too-few-public-methods

# --------
# Map1T.py
# --------

# https://docs.python.org/3/library/functions.html#map

from timeit   import timeit
from unittest import main, TestCase
from typing   import Callable, Iterable, Iterator, TypeVar

T = TypeVar("T")

# 651 milliseconds
class map_iterator (Iterator[T]) :
    def __init__ (self, uf: Callable[[T], T], a: Iterable[T]) -> None :
        self.uf = uf
        self.p  = iter(a)

    def __iter__ (self) -> Iterator[T] :
        return self

    def __next__ (self) -> T :
        return self.uf(next(self.p))

# 426 milliseconds
def map_for (uf: Callable[[T], T], a: Iterable[T]) -> Iterator[T] :
    for v in a :
        yield uf(v)

# 412 milliseconds
def map_generator (uf: Callable[[T], T], a: Iterable[T]) -> Iterator[T] :
    return (uf(v) for v in a)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            map_iterator,
            map_for,
            map_generator,
            map]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                m = f(lambda x : x ** 2, [2, 3, 4])
                self.assertEqual(list(m), [4, 9, 16])
                self.assertEqual(list(m), [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                m = f(lambda v : v ** 2, {2, 3, 4})
                self.assertEqual(set(m), {4, 9, 16})
                self.assertEqual(set(m), set())

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                m = f(None, ())
                self.assertEqual(list(m), [])

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                if f.__name__ == "map" :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda x : x ** 2, 10000 * [5]))",
                        "",
                        number = 100)
                else :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda x : x ** 2, 10000 * [5]))",
                        "from __main__ import " + f.__name__,
                        number = 100)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" : # pragma: no cover
    main()

""" #pragma: no cover
% MapT.py
..
map_iterator
651.40 milliseconds

map_for
426.22 milliseconds

map_generator
412.39 milliseconds

map
349.51 milliseconds
.
----------------------------------------------------------------------
Ran 3 tests in 2.061s

OK
"""
