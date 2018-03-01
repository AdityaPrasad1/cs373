# -----------
# Fri, 16 Feb
# -----------

r = reduce(
        <a binary function>
        <an iterable>
        <a seed>)

from operator import add, mul

a = [2, 3, 4]
print(reduce(add, a, 1)) # 10

"""
Java has a closed object model
Python has an open object model

all instances of a Java class have the same set of data members
that's not true of instances of Python classes
Python instances can gain and lose data
"""
