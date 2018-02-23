# -----------
# Wed, 31 Jan
# -----------

"""
exceptions
exercises
"""

"""
Java
"""

int i = 2;
int j = 2;
s.o.p(i == j); # true

Integer i = new Integer(2);
Integer j = new Integer(2);
s.o.p(i == j);              # false, identity check
s.o.p(i.equals(j));         # true,  content  check

class A {}

x = new A();
y = new A();
s.o.p(x == y);      # false
s.o.p(x.equals(y)); # false, equals() is inherited from object

"""
Python
"""

x = 2
y = 2
print(x is y) # true

x = fact(100)
y = fact(100)
print(x is y) # false, identity check
print(x == y) # true,  content  check

"""
small ints are defined to be in the range -5 to 256
"""

x = [2, 3, 4]
y = [2, 3, 4]
print(x is y) # false
print(x == y) # true

class A :
    pass

x = A()
y = A()
print(x is y) # false
print(x == y) # false, == is inherited from object

x = [2, 3]
print(type(x)) # list
x = [2]
print(type(x)) # list
x = []
print(type(x)) # list

x = (2, 3)
print(type(x)) # tuple
x = (2)
print(type(x)) # int
x = (2,)
print(type(x)) # tuple
x = ()
print(type(x)) # tuple

"""
Java:   exceptions have to extend the Throwable
Python: exceptions have to extend BaseException
"""
