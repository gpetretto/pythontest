import abc

class AbstractClass():
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def abstract_method(self):
        print "abstract_method default implementation"

class ImplementingSubclass(AbstractClass):
    def abstract_method(self):
        print "abstract_method implemented"

class NonImplementingSubclass(AbstractClass):
    pass

class UseSuperSubclass(AbstractClass):
    def abstract_method(self):
        print "abstract_method using super"
        super(UseSuperSubclass, self).abstract_method()

impl = ImplementingSubclass()
impl.abstract_method()

try:
    abstract = AbstractClass()
    abstract.abstract_method()
except BaseException as e:
    print str(e)

try:
    non_impl = NonImplementingSubclass()
    non_impl.abstract_method()
except BaseException as e:
    print str(e)

use_super = UseSuperSubclass()
use_super.abstract_method()

