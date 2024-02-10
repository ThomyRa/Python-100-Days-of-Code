import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

# Write your code below 👇


def speed_calc_decorator(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        print(f"{f.__name__} run speed: {dt}")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
