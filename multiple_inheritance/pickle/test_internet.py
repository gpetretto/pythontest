import pickle

class foo:
    def __init__(self,a,b):
        self.a = a
	self.b = b
	print "init1"

    def __str__(self):
        return str(self.a)

    def __getinitargs__(self):
        print "initargs1"
        return (2,3)


obj = foo(1,1)

with open('junk','wb') as f:
    pickle.dump(obj,f)

class foo:
    def __init__(self,a,b):
        print a,b
        self.a = a
        self.b = b
	print "init2"
    def __str__(self):
        return '%s %s'%(self.a,self.b)

    def __getinitargs__(self):
        print "getinitargs2"
        return (self.a,self.b)

with open('junk','rb') as f:
    obj = pickle.load(f)
    print str(obj)
