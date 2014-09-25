class Simple():
    def __init__(self, a):
        self.a = a

class Eq(Simple):
    def __eq__(self, other):
        print "inside __eq__"
        return self.a == other.a

a = Simple(1)
b = Simple(1)
    
c = Eq(1)
d = Eq(1)

print "a == b"
print a == b

print "c == d"
print c == d

print "a == c"
print a == c

print "c == a"
print c == a

print "a is b"
print a is b

print "c is d"
print c is d

print "a is a"
print a is a

