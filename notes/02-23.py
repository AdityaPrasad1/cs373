# -----------
# Fri, 23 Feb
# -----------

"""
if a function/method has yield in it
calling it does NOT run it
instead it produces and returns a generator
all generators are iterators
all iterators are not generators
"""

def f () :
    print("abc")
    yield 2
    print("def")
    yield 3
    print("ghi")
    yield 4

p = f()     # <nothing>
v = next(p) # abc
print(v)    # 2

v = next(p) # def
print(v)    # 3

v = next(p) # ghi
print(v)    # 4

v = next(p) # StopIteration

def range_iterator (b, e) :
    while b != e :
        yield b
        b += 1

class range :
    def __init__ (...) :
        ....

    def __iter__ (...) :
//      return range_iterator(self.b, self.e)
        b = self.b
        while b != self.e :
            yield .b
            b += 1

    def __getitem__ (self, i) :
        return self.b + i










