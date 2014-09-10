import abc
from six import add_metaclass
from collections import defaultdict

class Superclass():
    """
    empty
    """
    __metaclass__ = abc.ABCMeta
   
    @abc.abstractmethod
    def test_method(self):
        """metodo astratto"""


class Implementation(Superclass):
    def test_method(self):
	print 'test_method' 

class Pippo(Implementation):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def metodo_astratto(self):
	"""metodo astratto"""

#    def metodo_astratto(self):
#	print 'Pippo'
    
class Topolino(Pippo):
    def topolino():
	print 'ciao'
    
    def metodo_astratto(self):
	print 'metodo astratto Topolino'

    

class Pluto(Pippo):
    a=5

if __name__ == "__main__":
    print 'main'
#    print Topolino.__class__
#    print Topolino.__class__.__class__

    p=Topolino()
    p.metodo_astratto()

    p=Pluto() 
    p.metodo_astratto()

    p=Pippo()
    p.metodo_astratto()
