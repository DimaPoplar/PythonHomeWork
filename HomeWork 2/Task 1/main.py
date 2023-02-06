# Задание 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

number_coin = int(input("Введите кол-во монеток: "))
gerb = 0
reshka = 0
for _ in range(number_coin):
    coin = random.randint(0, 1)
    print(coin, end=" ")
    if coin == 0:
        gerb += 1
    else:
        reshka += 1
print()
if gerb > reshka:
    print(f"Минимальное число монеток = {reshka}")
else:
    print(f"Минимальное число монеток = {gerb}")
