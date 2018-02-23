# -----------
# Fri, 19 Jan
# -----------

"""
Docker
basics of running a Python script
assertions
"""

# Java, a little dynamically typed

int x = 2;

Mammal m;
m = new Mammal();
m = new Tiger();

# Python, completely dynamically typed

x = 2
x = Mammal()
x = Tiger()
x = 2.34

"""
Python script have
    definitions
    code

execute the script directly or import it interactively
    definitions to be defined
    code to be run

import a script from another script
    definitions to be defined
"""

"""
Collatz Conjecture
about 100 years old

take a pos int
if even, divide by 2
else, multiply by 3 and add 1
repeat until 1
"""

5 16 8 4 2 1

"""
cycle length of  5 is 6
cycle length of 10 is 7
"""

"""
Python has two division operators
    /:  true  division, always returns a float
    //: floor division, returns the type of the input
"""

"""
assertions are good for
    preconditions
    postcondions

not good for
    testing,    a better tool will be a unit test framework
    user error, a better tool will be exceptions
"""
