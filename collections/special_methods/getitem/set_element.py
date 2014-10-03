class Test():
    def __getitem__(self, item):
        print "getitem"
        return 1

t = Test()

print t['test']

t['test'] = 5
