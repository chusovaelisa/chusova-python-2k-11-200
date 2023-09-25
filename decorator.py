def log_input_output(func):
    def wrapper(*args, **kwargs):
        print(f"Входные параметры: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат выполнения функции: {result}")

        return result 

    return wrapper

@log_input_output
def add(a, b):
    return a + b

@log_input_output
def multiply(x, y):
    return x * y

add_result = add(5, 3)
multiply_result = multiply(4, 6)
