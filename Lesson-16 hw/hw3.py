# Создайте декоратор, который отключает функцию, если её выполнение занимает слишком много времени.

import time


def timeout_decorator(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            work_time = end_time - start_time
            if work_time > timeout:
                raise TimeoutError("Function execution timed out")
            return result
        return wrapper
    return decorator


@timeout_decorator(1)
def my_function():
    time.sleep(0)
    return "Hello, world!"

@timeout_decorator(1)
def my_function2():
    time.sleep(2)
    return "Hello, world!"


my_result = my_function()
print(my_result)
my_result2 = my_function2()
print(my_result2)
