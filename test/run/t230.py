def f(n):
    yield from range(n)
g = f(5)
print g.next()
print g.next()
print g.next()
print g.next()
