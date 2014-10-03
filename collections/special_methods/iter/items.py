class Test(dict):
    def __getitem__(self, item):
        print "getitem"
        return super(Test,self).__getitem__(item)

    def __iter__(self):
        print "iter"
        return super(Test,self).__iter__()


t = Test(test=5)

print "items"
for k, v in t.items():
    print k, v

print "iteritems"
for k, v in t.iteritems():
    print k, v

