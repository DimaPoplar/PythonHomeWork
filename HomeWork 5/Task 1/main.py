# Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии.

def degree(number_A: int, number_B: int) -> int:
    if number_B == 1:
        return number_A
    else:
        return number_A * degree(number_A, number_B - 1)

num_A = int(input('Введите основание: '))
num_B = int(input('Введите степень: '))
print(f"{num_A} в степени {num_B} = {degree(num_A, num_B)}")
