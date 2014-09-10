import pickle

class C():
    def __init__(self):
	print 'init'
    def __getinitargs__(self):
        return ((1,2))


#print C.__mro__
#print D.__mro__

c=C()
#d=D()

pickle.dump(c,open( "c.p", "wb" ))
#pickle.dump(d,open( "d.p", "wb" ))

c=pickle.load( open( "c.p", "rb" ) )
#d=pickle.load( open( "d.p", "rb" ) )

