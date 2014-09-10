import abc
from six import add_metaclass
from collections import defaultdict

@add_metaclass(abc.ABCMeta)
class FireTaskBase(defaultdict):
    """
    FireTaskBase is used like an abstract class that defines a computing task
    (FireTask). All FireTasks should inherit from FireTaskBase.

    You can set parameters of a FireTask like you'd use a dict.
    """

    # Specify required parameters with class variable. Consistency will be
    # checked upon init.
    required_params = []

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    @abc.abstractmethod
    def run_task(self, fw_spec):
        """
        This method gets called when the FireTask is run. It can take in a
        FireWork spec, perform some task using that data, and then return an
        output in the form of a FWAction.

        Args:
            fw_spec (dict): A FireWork spec. This comes from the master spec.
                In addition, this spec contains a special "_fw_env" key that
                contains the env settings of the FWorker calling this method.
                This provides for abstracting out certain commands or
                settings. For example, "foo" may be named "foo1" in resource
                1 and "foo2" in resource 2. The FWorker env can specify {
                "foo": "foo1"}, which maps an abstract variable "foo" to the
                relevant "foo1" or "foo2". You can then write a task that
                uses fw_spec["_fw_env"]["foo"] that will work across all
                these multiple resources.

        Returns:
            (FWAction)
        """
        print 'ho modificato!!!!'
        pass


class TestSubclass(FireTaskBase):
    """
    No implementation of the run_task method
    """
    def ciao(self):
	print 'ciao'

if __name__ == "__main__":
    test=TestSubclass()
    test.run_task('test')
