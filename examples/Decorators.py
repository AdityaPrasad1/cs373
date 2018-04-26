#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------------
# Decorators.py
# -------------

print("Decorators.py")

def f1 (n) :
    return n + 1

def test1 () :
    assert f1(2) == 3





def debug_function (f) :
    def g (n) :
        print(f.__name__, ":", end=" ")
        print("input =", n, ";", end=" ")
        m = f(n)
        print("output =", m, ";")
        return m
    return g

@debug_function
def f2 (n) :
    return n + 1

def test2 () :
    assert f2(2) == 3 # f2 : input = 2 ; output = 3 ;





class debug_class :
    def __init__ (self, f) :
        self.f = f

    def __call__ (self, n) :
        print(self.f.__name__, ":", end=" ")
        print("input =", n, ";", end=" ")
        m = self.f(n)
        print("output =", m, ";")
        return m

@debug_class
def f3 (n) :
    return n + 1

def test3 () :
    assert f3(2) == 3 # f3 : input = 2 ; output = 3 ;





def main () :
    for n in range(3) :
        eval("test" + str(n + 1) + "()")

if __name__ == "__main__" : # pragma: no cover
    print("Decorators.py")
    main()
    print("Done.")
