from collections import defaultdict
import pickle

class A(defaultdict):
    def __init__(self):
	print "init A noargs"

a=A()

pickle.dump(a,open( "a.p", "wb" ))
pickle.load( open( "a.p", "rb" ))

