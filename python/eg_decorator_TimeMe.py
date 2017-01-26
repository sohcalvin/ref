from time import sleep, time
class TimeMe(object):

    def __init__(self, mess):
        self.message = mess

    def __call__(self, function_to_be_decorated, *args, **kwargs):
        def new_func(*args, **kwargs):
            mark = time()
            result = function_to_be_decorated(*args, **kwargs)
            print("Elapsed time {0} : {1}".format(self.message, time() - mark))
            return result
        return new_func

@TimeMe("Total time of sleepFunction")
def sleepFunction():
    print("Start sleeping")
    sleep(3)
    print("End sleeping")



sleepFunction()



