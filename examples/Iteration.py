#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = unidiomatic-typecheck

# -------------
# Indexables.py
# -------------

# https://docs.python.org/3.6/tutorial/controlflow.html
# https://docs.python.org/3.6/library/itertools.html

from itertools import count

def test1 () :
    a = [2, 3, 4]
    assert type(a) is list
    assert not hasattr(a, "__next__")
    assert     hasattr(a, "__iter__")
    s = 0
    for v in a :
        s += v
    assert s == 9

def test2 () :
    a = [2, 3, 4]
    for v in a :
        v += 1            # ?
    assert a == [2, 3, 4]

def test3 () :
    a = [[2], [3], [4]]
    for v in a :
        v += (5,)                        # ?
    assert a == [[2, 5], [3, 5], [4, 5]]

def test4 () :
    a = [(2,), (3,), (4,)]
    for v in a :
        v += (5,)                  # ?
    assert a == [(2,), (3,), (4,)]

def test5 () :
    a = ["abc", "def", "ghi"]
    for v in a :
        v += "x"                      # ?
    assert a == ["abc", "def", "ghi"]

def test6 () :
    a = [[2, "abc"], (3, "def"), [4, "ghi"]]
    s = 0
    for u, _ in a :
        s += u
    assert s == 9

def test7 () :
    x = {2, 3, 4}
    assert type(x) is set
    assert not hasattr(x, "__next__")
    assert     hasattr(x, "__iter__")
    s = 0
    for v in x :                      # order not guaranteed
        s += v
    assert s == 9

def test8 () :
    d = {2: "abc", 3: "def", 4: "ghi"} # dict
    assert type(d) is dict
    assert not hasattr(d, "__next__")
    assert     hasattr(d, "__iter__")
    s = 0
    for k in d :                          # order not guaranteed
        s += k
    assert s == 9

def test9 () :
    d = {2: "abc", 3: "def"}
    k1 = d.keys()
    assert str(type(k1)) == "<class 'dict_keys'>"
    assert not hasattr(k1, "__next__")
    assert     hasattr(k1, "__iter__")
    assert set(k1) == {2, 3}
    assert set(k1) == {2, 3}
    k2 = d.keys()
    assert k1 is not k2
    d[4] = "ghi"
    assert d == {2: "abc", 3: "def", 4: "ghi"}
    assert set(k1) == {2, 3, 4}
    assert set(k1) == {2, 3, 4}

def test10 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    v = d.values()
    assert str(type(v)) == "<class 'dict_values'>"
    assert set(v) == {"abc", "def", "ghi"}

def test11 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    kv = d.items()
    assert str(type(kv)) == "<class 'dict_items'>"
    assert set(kv) == {(2, "abc"), (3, "def"), (4, "ghi")}

def test12 () :
    r = range(10)
    assert type(r) is range
    assert not hasattr(r, "__next__")
    assert     hasattr(r, "__iter__")
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test13 () :
    r = range(2, 10)
    assert list(r) == [2, 3, 4, 5, 6, 7, 8, 9]

def test14 () :
    r = range(2, 10, 2)
    assert list(r) == [2, 4, 6, 8]

def test15 () :
    r = range(10, 2, -2)
    assert list(r) == [10, 8, 6, 4]

def test16 () :
    r = range(10)
    assert hasattr(r, "__getitem__")
    assert r[0] == 0
    assert r[9] == 9
    try :
        assert r[10] == 10 # error: out of range
        assert False
    except IndexError :
        pass
    #r[0] = 2              # TypeError: 'range' object does not support item assignment

def test17 () :
    r = range(15)
    s = 0
    for v in r :
        if v == 10 :
            break
        s += v
    else :           # else clause in a for loop
        assert False # executes when the loop terminates normally
    assert s == 45

def test18 () :
    c = count()                          # 0, 1, 2, ...
    assert     hasattr(c, "__next__")
    assert     hasattr(c, "__iter__")
    assert not hasattr(c, "__getitem__")
    assert iter(c) is c
    for v in c :
        assert v >= 0
        if v == 10 :
            break
    for v in c :
        assert v > 10
        if v == 20 :
            break

def test19 () :
    c = count(3, 2) # 3, 5, 7, 9, ...
    for v in c :
        assert v >= 3
        if v > 10 :
            break

def test20 () :
    z = zip([2, 3], [4, 5, 6])
    assert     hasattr(z, "__next__")
    assert     hasattr(z, "__iter__")
    assert not hasattr(z, "__getitem__")
    assert iter(z) is z
    assert list(z) == [(2, 4), (3, 5)]
    assert list(z) == []

def test21 () :
    z = zip([2, 3], count())
    assert list(z) == [(2, 0), (3, 1)]
    assert list(z) == []

def main () :
    print("Iteration.py")
    for i in range(21) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
