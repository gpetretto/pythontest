from abc import *


class Foo(object):
    def __getitem__(self, index):
        return 0
    def __len__(self):
        return 0 
    def get_iterator(self):
        print 'Foo get_iterator'
        return iter(self)

class MyIterable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        print 'MyIterable get_iterator'
        return self.__iter__()

    def metodo_prova():
	print 'prova'

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

MyIterable.register(Foo)

assert issubclass(Foo,MyIterable)

f=Foo()
f.get_iterator()
f.metodo_prova()
f.__iter__()
