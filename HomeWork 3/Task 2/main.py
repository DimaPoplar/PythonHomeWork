# Задание 2. В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
my_word = input("Введите слово: ")
my_word_up = my_word.upper()
my_dict = {}
score = 0
list_score_1 = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", # En
                "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"] # Rus
list_score_2 = ["D", "G", # En
                "Д", "К", "Л", "М", "П", "У"] # Rus
list_score_3 = ["B", "C", "M", "P", # En
                "Б", "Г", "Ё", "Ь", "Я"] # Rus
list_score_4 = ["F", "H", "V", "W", "Y", # En
                "Й", "Ы"] # Rus
list_score_5 = ["K", # En
                "Ж", "З", "Х", "Ц", "Ч"] # Rus
list_score_8 = ["J", "X", # En
                "Ш", "Э", "Ю"] # Rus
list_score_10 = ["Q", "Z",
                 "Ф", "Щ", "Ъ"] # Rus
my_dict = {1: list_score_1, 2: list_score_2, 3: list_score_3,
           4: list_score_4, 5: list_score_5, 8: list_score_8,
           10: list_score_10}
for key in my_dict:
    for word in my_word_up:
        for alphabet in my_dict[key]:
            if alphabet.count(word) == 1:
                score += int(key)
print(score)

# for word in my_word_up:
#     print(word)
#     if list_score_1.count(word) == 1:
#         score += 1
#     if list_score_2.count(word) == 1:
#         score += 2
#     if list_score_3.count(word) == 1:
#         score += 3
#     if list_score_4.count(word) == 1:
#         score += 4
#     if list_score_5.count(word) == 1:
#         score += 5
#     if list_score_8.count(word) == 1:
#         score += 8
#     if list_score_10.count(word) == 1:
#         score += 10
# print(score)