import traceback

class pluto():
    def metodo_pluto(self):
        p=pippo()
        p.metodo()

class pippo():
    def metodo(self):
        print 'ciao'
        print traceback.print_stack()

if __name__ == '__main__':
    p=pluto()
    p.metodo_pluto()

