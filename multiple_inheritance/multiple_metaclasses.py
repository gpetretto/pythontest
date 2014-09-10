class metaA(type):
    def __call__(self):
        print 'call metaA'

class metaB(type):
    def __call__(self):
        print 'call metaB'

class metaAB(metaA):
    def __call__(self):
	print 'call metaAB'

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

c=C()
d=D()
