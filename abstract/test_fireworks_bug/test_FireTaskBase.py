import abc
from fireworks.core.firework import FireTaskBase

class TestSubclass(FireTaskBase):
    """
    No implementation of the run_task method
    """
    def ciao(self):
	print 'ciao'

if __name__ == "__main__":
    test=TestSubclass()
    test.run_task('test')
