def funky():
    print "cheese"

def gen():
    funky()
    yield 1
    i = 0 + 1

g = gen()
print g.next()
