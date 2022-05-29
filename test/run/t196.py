def f():
    if 1 == 2:
        yield -1
    else:
        yield 3

print list(f())
