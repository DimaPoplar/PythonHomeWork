# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и кол-во элементов нужно ввести с клавиатуры.
a_1 = int(input("Введите 1 член арифметической прогрессии: "))
d = int(input("Введите разность арифметической прогрессии: "))
n = int(input("Введите кол-во элементов арифметической прогрессии: "))

def fill_list(a_1: int, d: int , n: int) -> list:
    result_list = []
    for num in range(1, n + 1):
        a_n = a_1 + (num - 1) * d
        result_list.append(a_n)
    return result_list
print(fill_list(a_1,d,n))