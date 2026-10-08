from time import sleep, time
import random

def time_calculator(func):
    print(f'time_calculator called from {func.__name__}')
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        print(f"function {func.__name__} took {time() - start_time:.4f} seconds to complete.")
        return result
    return wrapper


def treshold(func):
    print(f'treshold called from {func.__name__}')
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 70:
            print(f"Result = {result} is greathern than 70")
            return result
        else:
            print(f"Result = {result} is less than 70")
            return result
    return wrapper


def none_decorator(func):
    print(f"None_decorator called from {func.__name__}")
    def wrapper(*args, **kwargs):
        print("Before function call")
        func(*args, **kwargs)
        print("after function call")
        return print(f"End of wrapper")
    print(f"End of none_decorator")
    return wrapper


# @time_calculator
def half_pauza():
    sleep(2)
    print("out, half_pauza")

# @time_calculator
def all_numbers():
    for i in range(1, 1000000000):
        pass
    print("out, all_numbers")

# @treshold
def random_number():
    return random.randint(1, 100)  

@none_decorator
def none_func():
    print("Inside none_func")