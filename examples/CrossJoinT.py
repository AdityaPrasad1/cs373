#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------
# CrossJoinT.py
# -------------

# http://en.wikipedia.org/wiki/Cartesian_product

from typing   import Dict, Iterable, Iterator
from unittest import main, TestCase

def cross_join_yield (
        r: Iterable[Dict[str, int]],
        s: Iterable[Dict[str, int]]) \
        -> Iterator[Dict[str, int]]  :
    for u in r :
        for v in s :
            yield {**u, **v}

def cross_join_generator (
        r: Iterable[Dict[str, int]],
        s: Iterable[Dict[str, int]]) \
        -> Iterator[Dict[str, int]]  :
    return ({**u, **v} for u in r for v in s)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            cross_join_yield,
            cross_join_generator]

        self.r = [
            {"A" : 1, "B" : 4},
            {"A" : 2, "B" : 5},
            {"A" : 3, "B" : 6}]

        self.s = [
            {"C" : 2, "D" : 7},
            {"C" : 3, "D" : 5},
            {"C" : 3, "D" : 6},
            {"C" : 4, "D" : 6}]

    def test1 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(self.r, self.s)
                self.assertEqual(
                    list(x),
                    [{'A': 1, 'B': 4, 'C': 2, 'D': 7},
                     {'A': 1, 'B': 4, 'C': 3, 'D': 5},
                     {'A': 1, 'B': 4, 'C': 3, 'D': 6},
                     {'A': 1, 'B': 4, 'C': 4, 'D': 6},
                     {'A': 2, 'B': 5, 'C': 2, 'D': 7},
                     {'A': 2, 'B': 5, 'C': 3, 'D': 5},
                     {'A': 2, 'B': 5, 'C': 3, 'D': 6},
                     {'A': 2, 'B': 5, 'C': 4, 'D': 6},
                     {'A': 3, 'B': 6, 'C': 2, 'D': 7},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 5},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 6},
                     {'A': 3, 'B': 6, 'C': 4, 'D': 6}])
                self.assertEqual(list(x), [])

if __name__ == "__main__" :
    main()
