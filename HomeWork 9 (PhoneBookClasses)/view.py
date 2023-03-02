def menu():
    print('''Главное меню:
    1. Открыть фаил 
    2. Сохранить фаил
    3. Показать контакты
    4. Добавить контакты
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')
    while True:
        try:
            choice = int(input("Выберите пункт меню: "))
            if 0 < choice < 9:
                return choice
            else:
                print("Введите число от 1 до 8")
        except:
            print("Вводите цифры!")


def show_contact(phone_book: list):
    print()
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f"{i}. {contact.get('name'):<20} "
                  f"{contact.get('phone'):<20} "
                  f"{contact.get('comment'):<20}")
    else:
        print("\nТелефонная книга не открыта или пуста\n")


def new_contact() -> dict:
    print()
    name = input("Введите имя и фамилию контакта")
    phone = input("Введите телефон")
    comment = input("Введите комментарий")
    return {'name': name,
            'phone': phone,
            'comment': comment}


def input_request(text: str) -> str:
    request = input(f"Введите {text}: ")
    return request


def change_contact(book: list) -> tuple:
    show_contact(book)
    choice = int(input("Выберите контакт, который хотите изменить: "))
    name = input("Введите новое имя или Enter оставить без изменений")
    phone = input("Введите новый телефон или Enter оставить без изменений")
    comment = input("Введите новый комментарий или Enter оставить без изменений")
    return choice - 1, {"name": name if name else book[choice - 1].get('name'),
                        "phone": phone if phone else book[choice - 1].get('phone'),
                        "comment": comment if comment else book[choice - 1].get('comment')}


def select_to_delete(book: list):
    show_contact(book)
    return int(input("Введите номер элемента, который хотите удалить: "))


def goodbye():
    print("Досвидание")

def confirm_changes():
    answer = input("У вас есть несохранёные изменения, хотите их сохранить? y/n: ")
    return True if answer == "y" else False
