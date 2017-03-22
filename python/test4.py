# def funcA(f, *args, **kwargs):
#
#     def wrapper():
#         print("funcA")
#         f()
#     return wrapper
#
# @funcA
# def funcB() :
#     print("funcB")




# ----------------------------------------------------------------------
from functools import wraps
from time import time,sleep
def TimeMeByFunc(function_to_be_decorated):
    def wrapper0(function_to_be_decorated) :
        @wraps(function_to_be_decorated)
        def wrapper(*args, **kwargs):
            mark = time()
            result = function_to_be_decorated(*args, **kwargs)
            print("Elapsed time {0} : {1}".format( "",time() - mark))
            return result
        return wrapper
    return wrapper0




# ----------------------------------------------------------------------
@TimeMeByFunc("SlowFunc")
# @TimeMeByFunc
def slow_function():
    sleep(1)
    return 2

# slow_function()
# print(slow_function.__name__)

print(" "[0:-1] + "<<")