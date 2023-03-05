import random


class Game:

    def __init__(self, table: dict):
        self.table = table
        self.position = 0

    def player_turn(self, icon_player: str):
        self.position = int(input("Сделайте ход: "))
        if self.table[self.position].isdigit():
            self.table[self.position] = icon_player
        else:
            print("Данная позиция уже занята!\n")
            return Game.player_turn(self, icon_player)

    @staticmethod
    def queue(sign: str):
        if sign == "O":
            return "X"
        else:
            return "O"

    def print_table(self):
        for temp in range(1, 10, 3):
            for el in range(0 + temp, 3 + temp):
                if el == 2 or el == 5 or el == 8:
                    print(f"| {self.table[el]} |", end=" ")
                else:
                    print(self.table[el], end=" ")
            print("")
            if temp != 7:
                print("----------")
        print("")
        return ""

    def search_winner(self):
        # Номера
        sign_gamer_1 = "X"
        sign_gamer_2 = "O"
        # Горизонтальная проверка
        for temp_horizon in range(0, 9, 3):
            gamer_1 = 0
            gamer_2 = 0
            for horizon in range(1 + temp_horizon, 4 + temp_horizon):
                if self.table[horizon] == "X":
                    gamer_1 += 1
                if self.table[horizon] == "O":
                    gamer_2 += 1
            if gamer_1 == 3:
                return sign_gamer_1
            if gamer_2 == 3:
                return sign_gamer_2
        # Вертикальная проверка
        for temp_vertical in range(0, 3, 1):
            gamer_1 = 0
            gamer_2 = 0
            for vertical in range(1 + temp_vertical, 8 + temp_vertical, 3):
                if self.table[vertical] == "X":
                    gamer_1 += 1
                if self.table[vertical] == "O":
                    gamer_2 += 1
            if gamer_1 == 3:
                return sign_gamer_1
            if gamer_2 == 3:
                return sign_gamer_2
        # Диагональная проверка (слева направо)
        gamer_1 = 0
        gamer_2 = 0
        for diagonal_left_right in range(1, 10, 4):
            if self.table[diagonal_left_right] == "X":
                gamer_1 += 1
            if self.table[diagonal_left_right] == "O":
                gamer_2 += 1
        if gamer_1 == 3:
            return sign_gamer_1
        if gamer_2 == 3:
            return sign_gamer_2
        # Диагональная проверка (справа налево)
        gamer_1 = 0
        gamer_2 = 0
        for diagonal_right_left in range(3, 8, 2):
            if self.table[diagonal_right_left] == "X":
                gamer_1 += 1
            if self.table[diagonal_right_left] == "O":
                gamer_2 += 1
        if gamer_1 == 3:
            return sign_gamer_1
        if gamer_2 == 3:
            return sign_gamer_2

    def bot_turn(self, icon_bot: str, icon_enemy: str):
        # Проверка горизонтальных линий на наличие 2-х своих элементов, и заполнение их
        for dop_num in range(0, 9, 3):
            count = 0
            for number in range(1 + dop_num, 4 + dop_num):
                if self.table[number] == icon_bot:
                    count += 1
                if count == 2:
                    for number_2 in range(1 + dop_num, 4 + dop_num):
                        if self.table[number_2].isdigit():
                            self.table[number_2] = icon_bot
                            return self.table
        # Проверка вертикальных линий на наличие 2-х своих элементов, и заполнение их
        for dop_num in range(0, 3, 1):
            count = 0
            for number in range(1 + dop_num, 8 + dop_num, 3):
                if self.table[number] == icon_bot:
                    count += 1
                if count == 2:
                    for number_2 in range(1 + dop_num, 8 + dop_num, 3):
                        if self.table[number_2].isdigit():
                            self.table[number_2] = icon_bot
                            return self.table
        # Проверка диагональных линий на наличие 2-х своих элементов, и заполнение их
        a_left_right = 0
        b_right_left = 0
        for num_diagonal in range(1, 10, 2):
            if self.table[num_diagonal] == icon_bot:
                if num_diagonal in [1, 5, 9]:
                    a_left_right += 1
                if num_diagonal in [3, 5, 7]:
                    b_right_left += 1
        if a_left_right == 2:
            for num_diagonal_2 in range(1, 10, 4):
                if self.table[num_diagonal_2].isdigit():
                    self.table[num_diagonal_2] = icon_bot
                    return self.table
        if b_right_left == 2:
            for num_diagonal_2 in range(3, 8, 2):
                if self.table[num_diagonal_2].isdigit():
                    self.table[num_diagonal_2] = icon_bot
                    return self.table
        #  Проверка горизонтальных линий на наличие 2-х элементов противника, и заполнение их
        for dop_num in range(0, 9, 3):
            count = 0
            for number in range(1 + dop_num, 4 + dop_num):
                if self.table[number] == icon_enemy:
                    count += 1
                if count == 2:
                    for number_2 in range(1 + dop_num, 4 + dop_num):
                        if self.table[number_2].isdigit():
                            self.table[number_2] = icon_bot
                            return self.table
        # Проверка вертикальных линий на наличие 2-х элементов противника, и заполнение их
        for dop_num in range(0, 3, 1):
            count = 0
            for number in range(1 + dop_num, 8 + dop_num, 3):
                if self.table[number] == icon_enemy:
                    count += 1
                if count == 2:
                    for number_2 in range(1 + dop_num, 8 + dop_num, 3):
                        if self.table[number_2].isdigit():
                            self.table[number_2] = icon_bot
                            return self.table
        # Проверка диагональных линий на наличие 2-х элементов противника, и заполнение их
        a_left_right_def = 0
        b_right_left_def = 0
        for num_diagonal_player in range(1, 10, 2):
            if self.table[num_diagonal_player] == icon_enemy:
                if num_diagonal_player in [1, 5, 9]:
                    a_left_right_def += 1
                if num_diagonal_player in [3, 5, 7]:
                    b_right_left_def += 1
        if a_left_right_def == 2:
            for num_diagonal_player_2 in range(1, 10, 4):
                if self.table[num_diagonal_player_2].isdigit():
                    self.table[num_diagonal_player_2] = icon_bot
                    return self.table
        if b_right_left_def == 2:
            for num_diagonal_player_2 in range(3, 8, 2):
                if self.table[num_diagonal_player_2].isdigit():
                    self.table[num_diagonal_player_2] = icon_bot
                    return self.table
        # Вариант с созданием победной позиции уголком
        if a_left_right == 2:
            if self.table[1] == icon_bot and self.table[5] == icon_bot:
                for dop_el_left_right_1 in range(2, 5, 2):
                    if self.table[dop_el_left_right_1].isdigit():
                        self.table[dop_el_left_right_1] = icon_bot
                        return self.table
            else:
                for dop_el_left_right_2 in range(6, 9, 2):
                    if self.table[dop_el_left_right_2].isdigit():
                        self.table[dop_el_left_right_2] = icon_bot
                        return self.table
        if b_right_left == 2:
            if self.table[3] == icon_bot and self.table[5] == icon_bot:
                for dop_el_right_left_1 in range(2, 7, 4):
                    if self.table[dop_el_right_left_1].isdigit():
                        self.table[dop_el_right_left_1] = icon_bot
                        return self.table
            else:
                for dop_el_right_left_2 in range(4, 9, 4):
                    if self.table[dop_el_right_left_2].isdigit():
                        self.table[dop_el_right_left_2] = icon_bot
                        return self.table
        # Блокировака большого уголка
        if self.table[1] == "X" and self.table[9] == icon_enemy:
            for magic_left_right in range(2, 9, 2):
                if self.table[magic_left_right].isdigit():
                    self.table[magic_left_right] = icon_bot
                    return self.table
        if self.table[3] == "X" and self.table[7] == icon_enemy:
            for magic_right_left in range(2, 9, 2):
                if self.table[magic_right_left].isdigit():
                    self.table[magic_right_left] = icon_bot
                    return self.table
        # Занимает 5 клетку если она свободна, либо 1, 3, 7, 9.
        if self.table[5].isdigit():
            self.table[5] = icon_bot
            return self.table
        else:
            temp_list = []
            for diag_temp in range(1, 10, 2):
                if self.table[diag_temp].isdigit():
                    # self.table[diag_temp] = "O"
                    # return self.table
                    temp_list.append(diag_temp)
            if temp_list:
                self.table[random.choice(temp_list)] = icon_bot
                return self.table
        return self.table

    # @staticmethod
    # def exit_or_main_menu(chose: int):
    #     if chose == 2:
    #         return 4