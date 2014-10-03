from collections import defaultdict

def default_function():
    return 1

d = defaultdict()

print d.default_factory

try:
    print d['keytest']
except Exception as e:
    print "Exception"

d.default_factory = default_function

print d['keytest']
