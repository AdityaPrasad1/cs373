// -----------
// Wed, 25 Apr
// -----------

i = 2
print(type(i))    # int
print(type(int))  # type
print(type(type)) # type

def f1 (n) :
    return n + 1

print(f1(2)) # 3

def fd (f) :
    def g (n) :
        print("input", n)
        m = f(n)
        print("output", m)
        return m
    return g

f2 = fd(f1)

print(f2(2)) # input 2 output 3 3

f1 = fd(f1)

print(f1(2)) # input 2 output 3 3

@fd
def f3 (n) :
    return n + 1

print(f3(2)) # input 2 output 3 3

class A1 :
    pass

x1 = A1()
y1 = A1()
print(x1 == y1) # false

print(type(A1)) # type
print(type(x1)) # A1

def cd (c) :
    x = c()
    return lambda : x # closure

A2 = cd(A1)

x2 = A2()
y2 = A2()
print(x2 == y2) # true

print(type(A2)) # FunctionType
print(type(x2)) # A1

A1 = A2

x3 = A1()
y3 = A1()
print(x3 == y3) # true

print(type(A1)) # FunctionType
print(type(x3)) # <instance of <addr>>

@cd
class A3 :
    pass

x4 = A3()
y4 = A3()
print(x4 == y4) # true

print(type(A3)) # FunctionType
print(type(x4)) # <addr>
