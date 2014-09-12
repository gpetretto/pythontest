def decorator(kls):
    def func():
	print "decorator"
	print kls
	return kls()
    return func

class metaclass(type):
    def __new__(cls, clsname, bases, dct):
	print "metaclass __new__"
	return super(metaclass, cls).__new__(cls, clsname, bases, dct)

    def __call__(cls, *args, **kw):
	print "metaclass __call__"
        return super(metaclass, cls).__call__(*args, **kw)

@decorator
class A():
    __metaclass__ = metaclass
    def __init__(self):
	print "init A"

a=A()
