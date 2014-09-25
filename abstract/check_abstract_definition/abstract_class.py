import abc
from six import add_metaclass


class Pippo():
    __metaclass__ = abc.ABCMeta


    def metodo_concreto(self):
	print 'implementazione'

    
class Topolino(Pippo):
    def topolino():
	print 'ciao'
    
    def metodo_astratto(self):
	print 'metodo astratto Topolino'

if __name__ == "__main__":
    print 'main'

    p=Topolino()
    p.metodo_concreto()

    p=Pippo()
    p.metodo_concreto()
    
