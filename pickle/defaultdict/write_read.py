import pickle
from collections import defaultdict

class C(dict):
    def __init__(self,a):
	print 'init'

class D(defaultdict):
    def __init__(self,a):
        print 'init'



c=C(1)


pickle.dump(c,open( "c.p", "wb" ))

c=pickle.load( open( "c.p", "rb" ) )


d=D(1)
pickle.dump(d,open( "d.p", "wb" ))
d=pickle.load( open( "d.p", "rb" ) )

