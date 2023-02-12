# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы

def summ_num (number_A: int, number_B: int) -> int:
    if number_B == 0:
        return number_A
    else:
        return summ_num(number_A + 1, number_B - 1)

num_A = input("Введите первое число: ")
num_B = input("Введите второе число: ")

count = 0
for _ in num_A or num_B:
    if _ in ["."]:
        count += 1
if count == 0:
    num_B = int(num_B)
    num_A = int(num_A)
    if num_A > 0 and num_B > 0:
        print(summ_num(num_A, num_B))
    else:
        print("Введите целые не отрицательные числа")
else:
    print("Введите целые не отрицательные числа")