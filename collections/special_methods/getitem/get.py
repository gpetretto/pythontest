class Test():
    def __getitem__(self, item):
        print "getitem"
        return super(Test,self).__getitem__(item)

t = Test(test=5)

print t['test']

print t.get('test')
