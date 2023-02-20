# Задача 32: Определить индексы элементов массива(списка), значение которых принадлежат данному
# диапазону
import random

num_min = int(input("Введите начало диапазона: "))
num_max = int(input("Введите конец диапазона: "))

my_list = [random.randint(1, 100) for i in range(10)]
print(my_list)

new_list = [i for i in range(num_min, num_max + 1)]
def find_index(list_give: list, list_find: list) -> list:
    result_list = []
    for num in list_give:
        if num in list_find:
            if list_give.index(num) not in result_list:
                result_list.append(list_give.index(num))
    return result_list
print(f"Индексы элементов, которые принадлежат промежутку от {num_min} до {num_max} - {find_index(my_list,new_list)}")
