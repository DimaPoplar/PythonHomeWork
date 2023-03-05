class Visual:

    @staticmethod
    def menu_choice():
        print(f'''Меню игры: 
    1. Игра друг против друга.
    2. Игра против бота.
    3. Бот против бота.
    4. Выход.''')
        return int(input("Выберите пункт меню: "))

    @staticmethod
    def table():
        main_table = {1: "1", 2: "2", 3: "3",
                      4: "4", 5: "5", 6: "6",
                      7: "7", 8: "8", 9: "9"}
        return main_table


    @staticmethod
    def choice_sign():
        ind = int(input("Выберите за кого хотите играть, 1 - О, 2 - Х: "))
        if ind == 1:
            return "O"
        else:
            return "X"

    @staticmethod
    def define_winner(sign: str):
        print(f"Победил '{sign}'")

    @staticmethod
    def chose_position():
        ind = int(input("Выберите, каким вы хотите делать ход, 1 или 2: "))
        if ind == 1:
            return 0
        if ind == 2:
            return 1

    @staticmethod
    def publication_move(index: int, gamer: str, position: int = 0, move: int = 0):
        match index:
            case 1:
                print(f"Ходит игрок, играющий за '{gamer}'")
            case 2:
                if position == 0:
                    if move % 2 == 0:
                        print(f"Ваш ход за {gamer}")
                    else:
                        print(f"Ход бота за {gamer}")
                else:
                    if move % 2 == 0:
                        print(f"Ход бота за {gamer}")
                    else:
                        print(f"Ваш ход за {gamer}")
            case 3:
                print(f"Ход бота, играющего за {gamer}")

    # @staticmethod
    # def quest_exit():
    #     ind = int(input("""Выберите пунтк меню:
    #     1. Вернуться в главное меню.
    #     2. Выйти."""))
