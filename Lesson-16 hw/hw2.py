# Напишите декоратор, который применяет функцию к возвращаемому значению другой функции. То есть декоратор должен
# принять другую функцию как аргумент и применить её к результату той функции, которую он декорирует.


def apply_function(some_function):
    def decorator(original_function):
        def wrapper(*args, **kwargs):
            result = original_function(*args, **kwargs)
            return some_function(result)
        return wrapper
    return decorator


@apply_function(lambda x: x)
def my_function(string):
    return "Hello, " + string + "!"

result = my_function("Michael")
print(result)