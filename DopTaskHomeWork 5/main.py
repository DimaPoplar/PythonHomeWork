# ------------------ Сравнить числа ------------------------------------
# ---------------Вариант 1-----------------
my_text_1 = int(input("Введите первое число:"))
my_text_2 = int(input("Введите второе число:"))
result = ""
new_text_1 = my_text_1 - my_text_2
new_text_2 = my_text_2 - my_text_1
new_text_1 = str(new_text_1)
new_text_2 = str(new_text_2)
result_text = new_text_1 + new_text_2
result_temp = "-"
max_text = 0
for num in result_text:
    if num in ["-"]:
        if num in [result_text[0]]:
            max_text = my_text_2
        else:
            max_text = my_text_1
for num in range(-(len(result_text) // 2), 0):
    result_temp += result_text[len(result_text) + num]
result = int(result_temp) + max_text
print(result)


# ---------Вариант 2-----------------------------------------------------------------
my_text_1 = int(input("Введите первое число:"))
my_text_2 = int(input("Введите второе число:"))
result = ""
new_text_1 = my_text_1 - my_text_2
new_text_2 = my_text_2 - my_text_1
new_text_1 = str(new_text_1)
new_text_2 = str(new_text_2)
result_text = new_text_1 + new_text_2
for num in result_text:
    if num in ["-"]:
        if num in [result_text[0]]:
            print(my_text_1)
        else:
            print(my_text_2)