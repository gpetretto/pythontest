class Test(dict):
    def __getitem__(self, item):
        print "getitem"
        return super(Test,self).__getitem__(item)
 
    def __contains__(self, item):
        print "contains"
        return super(Test, self).__contains__(item)

t = Test()

#print t['test']

print 'test' in t
