def yrange(n):
    yield from range(n)

def creator():
    r = yrange(5)
    print "creator", r.next()
    return r

def caller():
    r = creator()
    for i in r:
        print "caller", i

caller()
