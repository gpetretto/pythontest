class A():
    def __init__(self):
        print 'init A'

class B():
    def __init__(self):
        print 'init B'

class C(A,B):
    pass

class D(B,A):
    pass

c=C()
d=D()
