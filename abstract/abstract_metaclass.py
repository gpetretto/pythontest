import abc
from six import add_metaclass


class Pippo():
    __metaclass__ = abc.ABCMeta

#    @abc.abstractmethod
#    def metodo_astratto(self):
#	"""metodo astratto"""

    def metodo_astratto(self):
	print 'Pippo'

#@add_metaclass(abc.ABCMeta)
class MetaclasseAstratta(type):
    __metaclass__ = abc.ABCMeta

    def __new__(cls, clsname, bases, dct):
	print 'MetaclasseAstratta'
	return type.__new__(cls, clsname, bases, dct)
    
class Pluto():
    __metaclass__ = MetaclasseAstratta
    def metodo_astratto2(self):
        print 'Pluto'

class Topolino(Pluto):
#class Topolino(Pippo):
    def topolino():
	print 'ciao'
    

if __name__ == "__main__":
    print 'main'
    p=Pluto()
    print Pluto.__class__
    print Pluto.__class__.__class__  
    print Pluto.__class__.__class__.__class__ 
    #p=Topolino()
    #p.metodo_astratto()

    
