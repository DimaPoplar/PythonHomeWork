my_text = input("Введите ряд: ")
print(my_text)
if my_text.isalpha():
    # my_text = "aaaddddssssaaddggeedd"
    my_text_plus_one = my_text.ljust(len(my_text) + 1,"*")
    new_my_text = ""
    i = 0
    count = 1
    while i < len(my_text_plus_one) - 1:
        if my_text_plus_one[i] == my_text_plus_one[i + 1]:
            count += 1
        else:
            new_my_text += str(count) + my_text_plus_one[i]
            count = 1
        i += 1
    print(f"Результат сжатия - {new_my_text}")
else:
    new_my_text = ""
    my_list_num = []
    my_list_word = []
    temp = ""
    for number in my_text:
        if number.isdigit():
            temp += number
        else:
            new_my_text += number * int(temp)
            temp = ""
    print(f"Результат восстановления - {new_my_text}")

# -------------------------Вариант для ряда вида  "e2e"-----------------
# new_my_text = ""
# my_list_num = []
# my_list_word = []
# temp = ""
# mult_num = 1
# for number in my_text:
#     if number.isdigit():
#         temp += number
#         mult_num = int(number)
#     else:
#         new_my_text += number * mult_num
#         temp = ""
# print(f"Результат восстановления - {new_my_text}")

# -------------------------Вариант для ряда вида "e2e" который выдаёт ошибку-----------------
# if my_text[0].isdigit():
#     new_my_text = ""
#     my_list_num = []
#     my_list_word = []
#     temp = ""
#     mult_num = 1
#     for number in my_text:
#         if number.isdigit():
#             temp += number
#             mult_num = int(number)
#         else:
#             new_my_text += number * mult_num
#             temp = ""
#     print(f"Результат восстановления - {new_my_text}")
# else:
#     print("Введите корректный ряд")