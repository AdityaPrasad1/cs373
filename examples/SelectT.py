#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# SelectT.py
# ----------

# http://en.wikipedia.org/wiki/Selection_(relational_algebra)

from typing   import Callable, Dict, Iterable, Iterator
from unittest import main, TestCase

def select_yield (
        r: Iterable[Dict],
        f: Callable[[Dict], bool]) \
        -> Iterator[Dict]          :
    for d in r :
        if f(d) :
            yield d

def select_generator (
        r: Iterable[Dict],
        f: Callable[[Dict], bool]) \
        -> Iterator[Dict]          :
    return (d for d in r if f(d))

def select_filter (
        r: Iterable[Dict],
        f: Callable[[Dict], bool]) \
        -> Iterator[Dict]          :
    return filter(f, r)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            select_yield,
            select_generator,
            select_filter]

        self.r = [
            {"A" : 1, "B" : 4, "C" : 3},
            {"A" : 2, "B" : 5, "C" : 2},
            {"A" : 3, "B" : 6, "C" : 1}]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, lambda d : False)
                self.assertEqual(list(x), [])
                self.assertEqual(list(x), [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, lambda d : True)
                self.assertEqual(
                    list(x),
                    [{"A" : 1, "B" : 4, "C" : 3},
                     {"A" : 2, "B" : 5, "C" : 2},
                     {"A" : 3, "B" : 6, "C" : 1}])
                self.assertEqual(list(x), [])

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, lambda d : d["B"] > 4)
                self.assertEqual(
                    list(x),
                    [{'A': 2, 'B': 5, 'C': 2},
                     {'A': 3, 'B': 6, 'C': 1}])
                self.assertEqual(list(x), [])

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, lambda d : d["A"] > d["C"])
                self.assertEqual(
                    list(x),
                    [{'A': 3, 'B': 6, 'C': 1}])
                self.assertEqual(list(x), [])

if __name__ == "__main__" :
    main()
