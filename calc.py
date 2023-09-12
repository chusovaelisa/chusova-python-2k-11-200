history_plus = []
history_minus = []
history_multiply = []
history_divide = []

while True:
    try:
        operand1 = int(input("> "))
        operand2 = int(input("> "))
        operator = input("> ")

        if operator == "+":
            result = operand1 + operand2
            history_plus.append(f"{operand1}+{operand2}={result}")
        elif operator == "-":
            result = operand1 - operand2
            history_minus.append(f"{operand1}-{operand2}={result}")
        elif operator == "*":
            result = operand1 * operand2
            history_multiply.append(f"{operand1}*{operand2}={result}")
        elif operator == "/":
            if operand2 == 0:
                print("Ошибка: Деление на ноль!")
                continue
            result = operand1 / operand2
            history_divide.append(f"{operand1}/{operand2}={result}")
        else:
            print("Ошибка: Неподдерживаемая операция!")
            continue

        print(f"{operand1} {operator} {operand2} = {result}")
        print(f"+ {history_plus}")
        print(f"- {history_minus}")
        print(f"* {history_multiply}")
        print(f"/ {history_divide}")

    except ValueError:
        print("Ошибка: Введите числовые значения!")
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")
        break