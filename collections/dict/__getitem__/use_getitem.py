class TestGetItem():
    def __getitem__(self, item):
        print "function getitem"
        print item
        return 1

#    def __iter__(self):
#        print "__iter__"

t = TestGetItem()

print t['test']

for s in t:
    print "for in"
    print s
    # to prevent infinite loop
    break

#infinite loop
if 'test' in t:
    print "true"

try:
    print t.test
except AttributeError:
    print("AttributeError")
    
