# -----------
# Fri,  9 Feb
# -----------

"""
l-values vs. r-values

review of operators
in C, C++, Java, Python

specifics about some Python operators
"""

# Java

int i = 2;
i = 3;
2 = 3; # not ok

"""
valid on the left-hand-side of assignment, you're an l-value
if not, you're an r-value

i is an l-value
2 is an r-value
"""

int i = 2;
int j = 3;
int k;
k = (i + j);
k = (2 + 3);

i + j; # not ok

"""
+ takes two r-values
+ is an expression, can not stand alone
"""

i += j;
i += 2;
3 += 2; # not ok

"""
+= takes an l-value on the left, an r-value on the right
+= is a statement, can stand alone
"""

k = (i <<= j); # C, C++, Java: ok; Python: not ok

(i <<= j) = k; # C, Java, Python: not ok; C++: ok

++(i <<= j);

"""
+= in Python return nothing
+= in C and Java returns an r-value
+= in C++ returns an l-value
"""

int i = 2;
int j = ++i; # new value

int i = 2;
int j = i++; # old value

++i;
i++;

f(++i);
f(i++); # has to make a copy and is more expensive

for (T i = 0; i != s; ++i)

"""
a higher-order function is a function that can take functions as arguments
or return a function
"""

"""
list's += is not symmetric
list's += takes an iterable on the right
"""

"""
list's + is symmetric
list's + takes another list
"""

"""
tuple's += is symmetric
tuple's += takes another tuple
"""

"""
tuple's + is symmetric
tuple's + takes another tuple
"""

x += y
# is the same for immutable:s int, float, str, tuple
x = x + y

x += y
# is not the same for mutables: list
x = x + y
