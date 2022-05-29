def yrange(n):
    yield from range(n)

def zrange(n):
    yield from yrange(n)

print list(zrange(5))
