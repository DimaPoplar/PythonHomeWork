# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

my_list_1 = []
my_list_2 = []

number_item_1 = int(input("Введите кол-во элементов в первом наборе: "))
number_item_2 = int(input("Введите кол-во элементов во втором наборе: "))

for _ in range(number_item_1):
    my_list_1.append(random.randint(0,20))
for _ in range(number_item_2):
    my_list_2.append(random.randint(0,20))
print(my_list_1)
print(my_list_2)

def show_similar (list_1: list, list_2: list) -> list:
    result_list = []
    set_1 = set(list_1)
    set_2 = set(list_2)
    for item_1 in set_1:
        if item_1 in set_2:
            result_list.append(item_1)
    return result_list
print(show_similar(my_list_1,my_list_2))