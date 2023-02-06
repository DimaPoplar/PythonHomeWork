# Задание 3.
number = input("Введите число N: ")
if number.isdigit():
    temp = 1
    result = 1
    number = int(number)
    while result <= number:
        print(result, end=" ")
        result = 2 ** temp
        temp += 1
else:
    print("Введите коректное число")

