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
    def __getinitargs__(self):
        return (1)

class D(B,A):
    pass

