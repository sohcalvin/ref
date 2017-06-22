from concurrent.futures import as_completed, ThreadPoolExecutor, wait, FIRST_COMPLETED
import random
from time import sleep, time
from functools import wraps

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

def processRecord(row) :
    st = random.randint(1,5)
    st = 2
    sleep(st)
    print(row,") slept for ", st, "seconds")

@TimeMeByFuncMethod("xxx")
def poolExecution(record_processor,threads= 5) :

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures_map ={}
        for i in range(20) :
            if (len(futures_map) < threads):
                print("submitted at ", i, " less than 2")
                f = executor.submit(record_processor, i)
                futures_map[f] = 1
            else :
                done, not_done = wait(futures_map.keys(), return_when=FIRST_COMPLETED)
                for d in done :
                    futures_map.pop(d)
                    print("======popped",d)
                print("submitted at ", i)
                f = executor.submit(record_processor, i)
                futures_map[f] = 1


poolExecution(processRecord, worker=20 )

