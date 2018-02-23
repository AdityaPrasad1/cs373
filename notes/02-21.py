# -----------
# Wed, 21 Feb
# -----------

# Python

iter(p) -> p.__iter__()
next(p) -> p.__next__()

class RangeIterator :
    def __init__ (...) :
        ...

    def __iter__ (...) :
        ...

    def __next__ (...) :
        ...

# JavaScript

class RangeIterator {
    constructor (...) {
        ...}

    [Symbol.iterator] () {
        ...}

    next (...) {
        ...}
