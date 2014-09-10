import abc
from six import add_metaclass


#@add_metaclass(abc.ABCMeta)
#class AbstractMetaclass(type):
class AbstractMetaclass(abc.ABCMeta):
#    __metaclass__ = abc.ABCMeta

    def __new__(cls, clsname, bases, dct):
	print 'AbstractMetaclass'
	return super(AbstractMetaclass,cls).__new__(cls, clsname, bases, dct)
    
class SupposedToBeAbstractClass():
    __metaclass__ = AbstractMetaclass

    @abc.abstractmethod
    def abstract_method(self):
        pass
        

class ConcreteClass(SupposedToBeAbstractClass):
    
    def abstract_method(self):
	print 'abstract_method ConcreteClass'

if __name__ == "__main__":
    print 'main'
    test=ConcreteClass()
    print ConcreteClass.__class__
    print ConcreteClass.__class__.__class__  
    print ConcreteClass.__class__.__class__.__class__ 

    test.abstract_method()
    
    test=SupposedToBeAbstractClass()
    test.abstract_method()

