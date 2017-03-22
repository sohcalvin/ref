import logging
from functools import wraps

ds_logger = logging.getLogger()

GENERIC_LOGGING_MSG = {
    'INITIATING' : 'Initiating',
    'COMPLETED' : 'Completed',
    'EXCEPTION_ENCOUNTERED' : 'Exception Encountered In'
}

def safe_eval(code_block):
    try:
        result = code_block()
        return result
    except Exception as e:
        return e

def time_it(code_block):
    import timeit
    start_time = timeit.default_timer()
    result = code_block()
    elapsed_sec = timeit.default_timer() - start_time
    return result, elapsed_sec

def get_logger_fun(logger=None, is_warning=False):
    if logger is None:
        log_fun = print
    elif is_warning:
        log_fun = logger.warn
    else:
        log_fun = logger.info
    return log_fun

def profile(code_block, message, logger=None, max_time_sec=0):
    msg = "[{}] {}".format(message, GENERIC_LOGGING_MSG.get('INITIATING'))
    get_logger_fun(logger)(msg)
    result, elapsed = time_it(lambda: safe_eval(code_block))
    exception_status = type(result) == Exception
    status = GENERIC_LOGGING_MSG.get('COMPLETED') if not exception_status else GENERIC_LOGGING_MSG.get('EXCEPTION_ENCOUNTERED')
    msg = "[{}] {} in TIME sec: {} > {}".format(message, status, str(round(elapsed, 2)), max_time_sec)
    get_logger_fun(logger, elapsed > max_time_sec or exception_status)(msg)
    if exception_status:
        raise result
    else:
        return result

def profiler(description, max_time_sec=0):
    def profiler_wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return profile(lambda: f(*args, **kwargs), description, ds_logger, max_time_sec)
        return decorated_function
    return profiler_wrapper

@profiler("xxx")
def runLong() :
    import time
    time.sleep(10)

runLong()
