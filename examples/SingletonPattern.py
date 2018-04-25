#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------------------
# SingletonPattern.py
# -------------------

class A :
    pass

def test1 () :
    x = A()
    y = A()
    assert x != y





def singleton_function (c) :
    x = c()
    return lambda : x

@singleton_function
class B :
    pass

def test2 () :
    x = B()
    y = B()
    assert x == y




class singleton_class :
    def __init__ (self, c) :
        self.x = c()

    def __call__ (self) :
        return self.x

@singleton_class
class C :
    pass

def test3 () :
    x = C()
    y = C()
    assert x == y





def main () :
    for n in range(3) :
        eval("test" + str(n + 1) + "()")

if __name__ == "__main__" : # pragma: no cover
    print("SingletonPattern.py")
    main()
    print("Done.")
