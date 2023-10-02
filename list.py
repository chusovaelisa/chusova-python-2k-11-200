input_str = input("Введите список чисел, разделенных пробелами: ")
input_list = input_str.split()

def check_number(num_str):
    try:
        num = int(num_str)
        if num % 2 == 0:
            return ("Четное", num)
        else:
            return ("Нечетное", num)
    except ValueError:
        return ("Не число", -1)

results = list(map(check_number, input_list))
even_numbers = list(filter(lambda x: x[0] == "Четное", results))
odd_numbers = list(filter(lambda x: x[0] == "Нечетное", results))
negative_numbers = list(filter(lambda x: x[1] < 0, results))

print("Четные числа:", [result[1] for result in even_numbers])
print("Нечетные числа:", [result[1] for result in odd_numbers])
print("Отрицательные числа:", [result[1] for result in negative_numbers])
