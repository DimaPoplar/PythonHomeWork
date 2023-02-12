# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
# число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система
# состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий
# модуль, находясь перед некоторым кустом заданной во входном файле грядки.

number_kust = int(input("Введите кол-во кустов: "))

def plant_kust (number: int) -> dict:
    import random
    my_dict = {}
    for key in range(1, number + 1):
        my_dict[key] = my_dict.get(key, random.randint(0, 10))
    return my_dict

def collecting_module (dictionary: dict, number: int) -> int:
    result = 0
    list = []
    for key in dictionary:
        list.append(key)
    last_kust = len(list)
    if number == 1:
        result = dictionary[last_kust] + dictionary[1] + dictionary[2]
    elif number == last_kust:
        result = dictionary[last_kust] + dictionary[1] + dictionary[last_kust - 1]
    else:
        result = dictionary[number] + dictionary[number + 1] + dictionary[number - 1]
    return result

plant = plant_kust(number_kust)
print(plant)

kust_num = int(input("Напишите номер куста: "))

collecting = collecting_module(plant, kust_num)
print(f"Модуль собрал {collecting} ягод")
