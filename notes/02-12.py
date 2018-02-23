# -----------
# Mon, 12 Feb
# -----------

"""
factorial
    iteratively
    recursively
"""

# Java
ArrayList x = new ArrayList(...);
# <put stuff in it>
s.o.p(x.get(100))

# Java
LinkedList x = new LinkedList(...);
# <put stuff in it>
s.o.p(x.get(100))

# Java
TreeSet x = new TreeSet(...);
# <put stuff in it>
s.o.p(x.get(0)) # not ok
Iterator p = x.iterator();
s.o.p(p.next());
s.o.p(p.hasNext());

# Python
a = [2, 3, 4]
print(type(a)) # list
print(a[0])

a = {2, 3, 4}
print(type(a)) # set
p = iter(a)
print(type(p)) # set iterator
print(next(p)) # maybe 2
print(next(p)) # maybe 3
print(next(p)) # maybe 4
print(next(p)) # raise StopIteration

a = range(2, 5)
print(type(a)) # range
p = iter(a)
print(type(p)) # range iterator
print(next(p)) # 2
print(next(p)) # 3
print(next(p)) # 4
print(next(p)) # raise StopIteration
