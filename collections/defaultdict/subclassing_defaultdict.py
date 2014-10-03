from collections import defaultdict

class Subclass(defaultdict):
    def __init__(self):
        print "Subclass constructor"

def default_function():
    return 1

s = Subclass()

print s.default_factory

try:
    print s['keytest']
except Exception as e:
    print "Exception"

s.default_factory = default_function

print s['keytest']
