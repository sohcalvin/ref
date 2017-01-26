from time import sleep, time
from functools import wraps
class TimeMe(object):

    def __init__(self, mess):
        self.message = mess

    def __call__(self, function_to_be_decorated, *args, **kwargs):
        @wraps(function_to_be_decorated)
        def wrapper(*args, **kwargs):
            mark = time()
            result = function_to_be_decorated(*args, **kwargs)
            print("Elapsed time {0} : {1}".format(self.message, time() - mark))
            return result
        return wrapper


if __name__ == "__main__":

    @TimeMe("Total time of sleepFunction")
    def sleepFunction():
        """This is a sleep function"""
        print("Start sleeping")
        sleep(1)
        print("End sleeping")
        return 1+2

    print(sleepFunction())
    print(sleepFunction.__name__)
    print(sleepFunction.__doc__)


