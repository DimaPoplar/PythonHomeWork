# Задание 2.
number_one_x = int(input("Введите результат произведения: "))
number_two_y = int(input("Введите результат сложения: "))

if number_one_x <= 1000 and number_two_y <= 1000:
    result1 = number_one_x / 2
    result2 = number_two_y - result1
    if result1 * result2 == number_one_x and result1 + result2 == number_two_y:
        print(result1)
        print(result2)
    else:
        print("Петя загадал невозможные числа(")
else:
    print("Введите коректные числа")