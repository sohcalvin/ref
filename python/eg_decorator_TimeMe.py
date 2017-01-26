from time import sleep, time
from functools import wraps

#############################
# Method 1 : By Class
#############################
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

#############################
# Method 2 : By function
#############################
def TimeMeByFuncMethod(mess):
    def wrapper0(function_to_be_decorated) :
        @wraps(function_to_be_decorated)
        def wrapper(*args, **kwargs):
            mark = time()
            result = function_to_be_decorated(*args, **kwargs)
            print("Elapsed time {0} : {1}".format( mess,time() - mark))
            return result
        return wrapper
    return wrapper0




if __name__ == "__main__":

    # When decorator is applied with arg,
    # 1) instantiates with arg, so returns either TimeMe object or TimeMeByFuncMethod's wrapper0
    # 2) Then calls the output of 1 with the "function to be decorated" to get the final decorated function
    # Eg :
    #     ByClass :  tm = TimeMe("xxxx");  final_func = tm(func_tobe_decorated)
    #     ByMethod : wrapper0 = TimeMeByFuncMethod("xxx"); final_func = wrapper0(func_tob_decorated)
    @TimeMeByFuncMethod("Total time of sleepFunction")
    def sleepFunction():
        """This is a sleep function"""
        print("Start sleeping")
        sleep(1)
        print("End sleeping")
        return 1+2

    print(sleepFunction())
    print(sleepFunction.__name__)
    print(sleepFunction.__doc__)


