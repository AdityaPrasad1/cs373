# -----------
# Mon, 29 Jan
# -----------

"""
black box vs white box testing
meta cache
exceptions
"""

"""
unit tests (white) vs acceptance tests (black)
"""

"""
max cycle lengths
1-1000
1000-2000
2000-3000
3000-4000
....
"""

"""
meta cache
mcl(1500,3500)
compute the cl of 1500-2000
look up 2000-3000
compute the cl of 3000-3500
"""

"""
motivate the use of exceptions
"""

def f (...) :
    ...
    if (<something wrong>)
        return -1
    ...

def g (...) :
    ...
    x = f(...)
    if (x == -1)
        <something wrong>
    ...

h = 0

def f (...) :
    global h
    ...
    if (<something wrong>)
        h = -1
        return ...
    ...

def g (...) :
    global h
    ...
    h = 0
    x = f(...)
    if (h == -1)
        <something wrong>
    ...

def f (..., h2) :
    ...
    if (<something wrong>)
        h2[0] = -1
        return ...
    ...

def g (...) :
    ...
    h = [0]
    x = f(..., h)
    if (h == [-1])
        <something wrong>
    ...

"""
how can functions communicate?
#1: use the return mechanism of a function
#2: use a global variable
#3: use a paramater by reference
"""

# Java

int i = 2;
Integer x;
x = new Integer(0);

def f (...) :
    ...
    if (<something wrong>)
        raise Tiger(...)
    ...

def g (...) :
    ...
    try :
        ...
        x = f(...)
        ...
    except (Tiger as h) :
        <something wrong>
    except (Mammal as e) :
        <something wrong>
    else :
        #1
    finally :
        # always
    ...

...
...g(...)...
...

"""
1. no exception was thrown, no catch block was run
2. an exception was thrown, caught in the caller, only catch code can run next, followed by normal code again
3. an exception was thrown, not caught in the caller, leading us to look for the caller of the caller
"""
