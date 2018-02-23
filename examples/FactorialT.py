#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# FactorialT.py
# -------------

# https://docs.python.org/3.6/library/math.html

from functools import reduce
from math      import factorial
from operator  import mul
from timeit    import timeit
from unittest  import main, TestCase

# recursive procedure
# linear recursive process
# 21 milliseconds
def factorial_recursion (n: int) -> int :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)

# recursive procedure
# linear iterative process
# 29 milliseconds
def factorial_tail_recursion (n: int) -> int :
    assert n >= 0
    def f (n, v) :
        assert n >= 0
        assert v >= 1
        if n < 2 :
            return v
        return f(n - 1 , n * v)
    return f(n, 1)

# iterative procedure
# linear iterative process
# 12 milliseconds
def factorial_while (n: int) -> int :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

# iterative procedure
# linear iterative process
# 7 milliseconds
def factorial_range_for (n: int) -> int :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

# iterative procedure
# linear iterative process
# 16 milliseconds
def factorial_range_iterator (n: int) -> int :
    assert n >= 0
    v = 1
    p = iter(range(1, n + 1))
    try :
        while True :
            i  = next(p)
            v *= i
    except StopIteration :
        pass
    return v

# iterative procedure
# linear iterative process
# 17 milliseconds
def factorial_range_reduce_1 (n: int) -> int :
    assert n >= 0
    return reduce(lambda x, y : x * y, range(1, n + 1), 1)

# iterative procedure
# linear iterative process
# 9 milliseconds
def factorial_range_reduce_2 (n: int) -> int :
    assert n >= 0
    return reduce(mul, range(1, n + 1), 1)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            factorial_recursion,
            factorial_tail_recursion,
            factorial_while,
            factorial_range_for,
            factorial_range_iterator,
            factorial_range_reduce_1,
            factorial_range_reduce_2,
            factorial]

    def test1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(0), 1)

    def test2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(1), 1)

    def test3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(2), 2)

    def test4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(3), 6)

    def test5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(4), 24)

    def test6 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(5), 120)

    def test7 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                t = timeit(
                    f.__name__ + "(100)",
                    "from __main__ import " + f.__name__,
                    number = 1000)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" : # pragma: no cover
    main()

""" #pragma: no cover
% Factorial.py
......
factorial_recursion
21.31 milliseconds

factorial_tail_recursion
28.77 milliseconds

factorial_while
11.89 milliseconds

factorial_range_for
6.75 milliseconds

factorial_range_iterator
15.50 milliseconds

factorial_range_reduce_1
16.49 milliseconds

factorial_range_reduce_2
9.34 milliseconds

factorial
1.03 milliseconds
.
----------------------------------------------------------------------
Ran 7 tests in 0.087s

OK
"""
