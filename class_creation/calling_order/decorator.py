def decorator(kls):
    def func():
	print "decorator"
	print kls
	return kls()
    return func

@decorator
class A():
    def __init__(self):
	print "init A"

a=A()
