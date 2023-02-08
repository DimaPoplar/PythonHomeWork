# Задание 1. Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X. Программа должна вывести в консоль сколько раз встречается
# в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random

my_list = []
for _ in range(15):
    my_list.append(random.randint(1, 100))
print(my_list)
number_x = int(input("Введите искомое число: "))
if 0 < number_x <= 100:
    count = 0
    for _ in my_list:
        if number_x == _:
            count += 1
    if count != 0:
        print(f"Число {number_x} встречается {count} раз")
    else:
        my_list.append(number_x)
        my_list.sort()
        position_number = my_list.index(number_x)
        min_num = (int(my_list[position_number]) - int(my_list[position_number - 1])) ** 2
        max_num = (int(my_list[position_number + 1]) - int(my_list[position_number])) ** 2
        if min_num > max_num:
            print(f"Максимально близкое по значению число из списка = {my_list[position_number + 1]}")
        else:
            print(f"Максимально близкое по значению число из списка = {my_list[position_number - 1]}")
else:
    print("Введите значение Х в промежутке от 1 до 100")
