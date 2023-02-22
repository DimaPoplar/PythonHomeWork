# text = "Пара-ра-рам рам-пам-папам па-ра-пада"
text = input("Введите текст: ")

def find_rutm(string: str):
    glas_words = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
    new_text = string.split(" ")
    score = []
    for fraz in new_text:
        temp = 0
        for i in fraz:
            if i in glas_words:
                temp += 1
        score.append(temp)
    if score.count(score[1]) == len(score):
        print("Парам пам-пам")
    else:
        print("Пам парам")


find_rutm(text)