#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# Project.py
# ----------

# http://en.wikipedia.org/wiki/Projection_(relational_algebra)

def test1 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    assert                    \
        list(project(r, "D")) \
        ==                    \
        [{}, {}, {}]

def test2 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    assert                    \
        list(project(r, "B")) \
        ==                    \
        [{'B': 4},
         {'B': 5},
         {'B': 6}]

def test3 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    assert                         \
        list(project(r, "A", "C")) \
        ==                         \
        [{'A': 1, 'C': 3},
         {'A': 2, 'C': 2},
         {'A': 3, 'C': 1}]

def main () :
    for n in range(3) :
        eval("test" + str(n + 1) + "()")

if __name__ == "__main__" : # pragma: no cover
    print("Project.py")
    main()
    print("Done.")
