# note: no overloading in python

class A():
    def method(self):
	print "method A"

class B(A):
    def method(self,a):
	print "method B"

b=B()
b.method(1)
b.method()
