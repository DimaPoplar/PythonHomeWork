from copy import deepcopy
class PhoneBook:


    def __init__(self, path: str = "phone_db.txt"):
        self.path = path
        self.phone_book = []
        self.new_phone_book = []

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            pb = {}
            new = contact.strip().split(";")
            pb["name"] = new[0]
            pb["phone"] = new[1]
            pb["comment"] = new[2]
            self.phone_book.append(pb)
        print("\nТелефонная книга успешно загружена\n")
        self.new_phone_book = deepcopy(self.phone_book)

    def seif_file(self):
        data = []
        for contact in self.phone_book:
            data.append(";".join(contact.values()))
        data = "\n".join(data)
        with open(self.path, "w", encoding="UTF-8") as file:
            file.write(data)

    def get(self):
        return self.phone_book

    def new_contact(self, contact: dict):
        self.phone_book.append(contact)
        print(f"\nКонтакт {contact.get('name')} успешно записан")

    def search(self, word: str) -> list:
        search_result = []
        for contact in self.phone_book:
            for field in contact.values():
                if word in field:
                    search_result.append(contact)
        return search_result

    def change(self, i: int, new_value: dict):
        self.phone_book[i] = new_value


    def delete(self, i: int ):
        contact = self.phone_book.pop(i)
        print(f'Контакт {contact.get("name")} удалён')

    def save_file(self):
        data = []
        for contact in self.phone_book:
            data.append(";".join(contact.values()))
        data = "\n".join(data)
        with open(self.path, "w", encoding="UTF-8") as file:
            file.write(data)

    def check_changes(self):
        if self.phone_book != self.new_phone_book:
            return True
        else:
            return False
