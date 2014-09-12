try:
    import nonexistingmodule
except ImportError:
    print "module does not exist"

class A():
    def method(self):
        if False:
            # try to use module
            nonexistingmodule.method()
        print "A method"

print "class created"

a=A()

print "class instantiated"

a.method()

print "method called"
