import pickle

class metaA(type):
    def __call__(self):
        print 'call metaA'
        return super(metaA,self).__call__()

class metaB(type):
    def __call__(self):
        print 'call metaB'
        return super(metaB,self).__call__()

class metaAB(metaA):
    def __call__(self):
	print 'call metaAB'
        return super(metaAB,self).__call__()

class A():
    __metaclass__ = metaA
    def __init__(self):
        print 'init A'

class B():
    __metaclass__ = metaAB
    def __init__(self):
        print 'init B'

class C(A,B):
    pass

class D(B,A):
    pass

print C.__mro__
print D.__mro__

c=C()
d=D()

pickle.dump(c,open( "c.p", "wb" ))
pickle.dump(d,open( "d.p", "wb" ))
