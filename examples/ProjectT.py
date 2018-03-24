#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# ProjectT.py
# -----------

# http://en.wikipedia.org/wiki/Projection_(relational_algebra)

from typing   import Dict, Iterable, Iterator
from unittest import main, TestCase

def project_yield (
        r: Iterable[Dict],
        *t: str)                     \
        -> Iterator[Dict]  :
    for d in r :
        x = {}
        for a in t :
            if a in d :
                x[a] = d[a]
        yield x

def project_comprehension (
        r: Iterable[Dict],
        *t: str)                     \
        -> Iterator[Dict]  :
    for d in r :
        yield {a : d[a] for a in t if a in d}

def project_generator (
        r: Iterable[Dict],
        *t: str)                     \
        -> Iterator[Dict]  :
    return ({a : d[a] for a in t if a in d} for d in r)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            project_yield,
            project_comprehension,
            project_generator]

        self.r = [
            {"A" : 1, "B" : 4, "C" : 3},
            {"A" : 2, "B" : 5, "C" : 2},
            {"A" : 3, "B" : 6, "C" : 1}]

    def test1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, "D")
                self.assertEqual(
                    list(x),
                    [{}, {}, {}])
                self.assertEqual(list(x), [])

    def test2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, "B")
                self.assertEqual(
                    list(x),
                    [{'B': 4},
                     {'B': 5},
                     {'B': 6}])
                self.assertEqual(list(x), [])

    def test3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, "A", "C")
                self.assertEqual(
                    list(x),
                    [{'A': 1, 'C': 3},
                     {'A': 2, 'C': 2},
                     {'A': 3, 'C': 1}])
                self.assertEqual(list(x), [])

if __name__ == "__main__" :
    main()
