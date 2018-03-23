#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# Select.py
# ---------

# http://en.wikipedia.org/wiki/Selection_(relational_algebra)

def test1 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = select(r, lambda d : False)
    assert list(x) == []

def test2 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = select(r, lambda d : True)
    assert                           \
        list(x)                      \
        ==                           \
        [{"A" : 1, "B" : 4, "C" : 3},
         {"A" : 2, "B" : 5, "C" : 2},
         {"A" : 3, "B" : 6, "C" : 1}]
    assert list(x) == []

def test3 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = select(r, lambda d : d["B"] > 4)
    assert                         \
        list(x)                    \
        ==                         \
        [{'A': 2, 'B': 5, 'C': 2},
         {'A': 3, 'B': 6, 'C': 1}]
    assert list(x) == []

def test4 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = select(r, lambda d : d["A"] > d["C"])
    assert                         \
        list(x)                    \
        ==                         \
        [{'A': 3, 'B': 6, 'C': 1}]
    assert list(x) == []

def main () :
    for n in range(4) :
        eval("test" + str(n + 1) + "()")

if __name__ == "__main__" : # pragma: no cover
    print("Select.py")
    main()
    print("Done.")
