# -----------
# Wed, 28 Feb
# -----------

a  = [2, 3, 4, 5]
a += [5]

class map :
    def __init__ (self, uf, a) :
        self.uf = uf
        self.p  = iter(a)

    def __next__ (self):
        return self.uf(next(self.p))

    def __iter__ (self):
        return self

def map (uf, a) :
    for v in a :
        yield uf(v) -> yield uf.__call__(v)

def map (uf, a) :
    return (uf(v) for v in a)

# JavaScript

x = Foo()     # function    invocation
y = new Foo() # constructor invocation
