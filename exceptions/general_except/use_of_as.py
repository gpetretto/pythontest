
class MyError(Exception):
    def test_method(self):
        print "test method"


try:
    raise MyError()
except MyError as e:
    e.test_method()

try:
    raise MyError()
except BaseException as e:
    e.test_method()


