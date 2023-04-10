# Создайте декоратора, который принимает функцию в качестве аргумента и гарантирует, что она всегда вернёт пол. число.

def ensure_num(original_function):
    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        try:
            return float(result) if float(result) > 0 else ValueError('U r entered the invalid value')
        except (ValueError, TypeError):
            raise ValueError("Function did not return a valid value")
    return wrapper


@ensure_num
def my_function(num):
    return num


result1 = my_function(10)
print(result1)

result2 = my_function("20.5")
print(result2)

result3 = my_function(-3)
print(result3)
