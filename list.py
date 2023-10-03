input_str = input("Введите список чисел, разделенных пробелами: ")
numbers = input_str.split()

try:
    numbers = [int(num) for num in numbers]
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    negative_numbers = [num for num in numbers if num < 0]

    print("Четные числа:", even_numbers)
    print("Нечетные числа:", odd_numbers)
    print("Числа меньше 0:", negative_numbers)
except ValueError:
    print("-1")


input_str = input("Введите список чисел, разделенных пробелами: ")
numbers = input_str.split()

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

numbers = list(filter(is_integer, numbers))
numbers = list(map(int, numbers))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
negative_numbers = list(filter(lambda x: x < 0, numbers))

print("Четные числа:", even_numbers)
print("Нечетные числа:", odd_numbers)
print("Числа меньше 0:", negative_numbers)
