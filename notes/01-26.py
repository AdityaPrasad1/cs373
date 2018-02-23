# -----------
# Fri, 26 Jan
# -----------

"""
assertions not good for
    testing
    user errors
"""

"""
unit testing
coverage
exercise
"""

class A :
    def f (self) :
        ...

x = A()
y = A()
z = A()

x.f() # self -> x
y.f() # self -> y
z.f() # self -> z

range(2, 5) # -> 2, 3, 4

"""
1. run as is, confirm success
2. fix the tests
3. run, confirm failure
4. fix the code
5. run, confirm success
"""
