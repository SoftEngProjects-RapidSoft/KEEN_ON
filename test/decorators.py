# might be used decoraters 

import functools
# preserve the doc identity of decorated function

import time


def debug(func):
    """Debug the decorated function"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug


def waste_time(func):
    """Print runtime of the decorated function as seconds"""

    @functools.wraps(func)
    def wrapper_waste_time(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Finished {func.__name__!r} in {end_time - start_time} secs")
        return value
    return wrapper_waste_time


def slow_down(_func = None, *, sleep_time=1):
    """ Wait a second beforre decorated function execution """
    
    def decorater_slow_down(func):
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(sleep_time)
            return func(*args, **kwargs)
        return wrapper_slow_down

    if _func == None:
        return decorater_slow_down
    else:
        return decorater_slow_down(_func)


def count_calls(func):
    """Print the current call amount of decorated function"""
    
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)

    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls
    

# test - slow_down
@slow_down
def countdown(count = 10):
    if count > 0:
        print(count)
        countdown(count - 1)
    else:
        print("Liftoff !")


# test it
if __name__ == "__main__":
    countdown(10)