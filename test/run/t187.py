def gen():
    funky()
    yield 1
    i = 0 + 1

def funky():
    print "cheese"

g = gen()
print g.next()
