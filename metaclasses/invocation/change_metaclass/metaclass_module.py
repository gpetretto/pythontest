__all__=["metaclass"]

param=10

class metaclass(type):
    def __new__(cls, name, bases, nmspc):
	print "new metaclass", param
	return super(metaclass,cls).__new__(cls, name, bases, nmspc)

    def __init__(cls, name, bases, nmspc):
	print "init metaclass",param
        #return super(metaclass,cls).__init__(cls, name, bases, nmspc)
        return type.__init__(cls, name, bases, nmspc)

