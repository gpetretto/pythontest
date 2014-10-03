class Test(dict):
    def __getitem__(self, item):
        print "getitem"
        return 1

t = Test()

print t['test']

# These won't call __getitem__
t['test'] = 5
t.update(test = 5)
