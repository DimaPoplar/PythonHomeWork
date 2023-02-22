# Задание 2: Напишите функцию, которая принимает в качестве аргумента функцию, вычисляющую
# элемент по номеру строки и столбца.
def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(num_rows + 1):
        for y in range(num_columns + 1):
            if operation(3, 3) == 9 or operation(3, 3) == 1:
                if x != 0 and y != 0:
                    print(round(operation(x, y), 1), end=" ")
            else:
                print(operation(x, y), end=" ")
        print()


def operation(string: str):
    if string == "*":
        return lambda x, y: x * y
    if string == "+":
        return lambda x, y: x + y
    if string == "-":
        return lambda x, y: x - y
    if string == "/":
        return lambda x, y: x / y


oper = input("Введите операцию (*,+,-,/): ")
print_operation_table(operation(oper))
