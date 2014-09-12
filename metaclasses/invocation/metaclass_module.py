__all__=["metaclass"]


class metaclass(type):
    def __new__(cls, name, bases, nmspc):
	print "new metaclass"
	return super(metaclass,cls).__new__(cls, name, bases, nmspc)

    def __init__(cls, name, bases, nmspc):
	print "init metaclass"
        #return super(metaclass,cls).__init__(cls, name, bases, nmspc)
        return type.__init__(cls, name, bases, nmspc)

