from metaclass_module import metaclass

class testclass():
    __metaclass__ = metaclass

    def __init__(self):
	print "init testclass"
