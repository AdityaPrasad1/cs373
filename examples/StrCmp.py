#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# StrCmp.py
# ---------

def test1 () :
    assert strcmp("",    "")    == 0

def test2 () :
    assert strcmp("abc", "abc") == 0

def test3 () :
    assert strcmp("abc", "ab")  >  0

def test4 () :
    assert strcmp("abc", "aba") >  0

def test5 () :
    assert strcmp("ab",  "abc") <  0

def test6 () :
    assert strcmp("aba", "abc") <  0

def main () :
    print("StrCmp.py")
    for i in range(6) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
