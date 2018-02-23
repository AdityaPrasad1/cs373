# -----------
# Fri,  2 Feb
# -----------

# Java

int i = 2;

String s = new String()
String t = "abc"

class A {}

"""
results in the creation of an instance of class class
that describes class A
"""

class T {
    public static void main (...) {
        A x = new A();
        Class c = x.getClass();

        A y = new A();
        Class d = y.getClass();

        s.o.p(c == d); # True

        Class e = A.class;
        s.o.p(c == e); # True

# Python

x = [2, 3, 4]
print(type(x))    # list
print(type(list)) # type
print(type(type)) # type

x = [2, 3, 4]
# add many more elements to it
# resulting in 100 elements
x += [5]

"""
adding to the back is amortized const
cost of adding to the front or the middle
always linear

removing the back always const
removing from the front or the middle always linear
"""

x = [2]
print(type(x)) # list

x = (2)
print(type(x)) # int

x = (2,)
print(type(x)) # tuple

"""
what does immutability mean for tuples
    can't change the size
    can't change the elements
"""

x = (2, 3, 4)

x = [2, 3, 4]
y = (5, x, 6)
print(len(y)) # 3
print(y)      # (5, [2, 3, 4], 6)
x += [7]
print(x)      # [2, 3, 4, 7]
print(y)      # (5, [2, 3, 4, 7], 6)

# sets can't have duplicates

print([2, 2, 2]) # [2, 2, 2]
print({2, 2, 2}) # {2}

# Python's set is hash based

x = {2, 3, 4}

"""
what does immutability mean for set
    can't change the keys
"""

"""
what does immutability mean for frozenset
    can't change the size
    can't change the keys
"""

"""
what does immutability mean for dict
    can't change the keys
"""

"""
in Python the mutables are NOT hashable
    list
    set
    dict
and therefore can NOT be in a set, frozenset, dict

The immutables are hashable
    int
    bool
    float
    str
    tuple
    frozen set
"""



