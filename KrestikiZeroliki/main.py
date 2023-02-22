import copy
my_dict_table = {1: "|_|", 2: "|_|", 3: "|_|",
                 4: "|_|", 5: "|_|", 6: "|_|",
                 7: "|_|", 8: "|_|", 9: "|_|"}


def table(dictionary: dict):  # <--------------print table-------------
    temp_num = 1
    for temp in range(1, 10, 3):
        for _ in range(0 + temp, 3 + temp):
            print(dictionary[_], end=" ")
        print("")
        for _ in range(3):
            print(temp_num, end="   ")
            temp_num += 1
        print("")
    return ""


def hod_chose(dictoinary: dict, number_chose: int) -> dict:  # <--------move players---------
    if dictoinary[number_chose] == "|_|":
        dictoinary[number_chose] = "|*|"
        return dictoinary
    else:
        return hod_chose(my_dict_table, int(input("Данное поле уже занято, выберите другое: ")))


def hod_robot_def(dictionary: dict) -> dict:  # <-----------------Defence and attack prog-----------------
    # Проверка горизонтальных линий на наличие 2-х своих элементов, и заполнение их
    for dop_num in range(0, 9, 3):
        count = 0
        for number in range(1 + dop_num, 4 + dop_num):
            if dictionary[number] == "|0|":
                count += 1
            if count == 2:
                for number_2 in range(1 + dop_num, 4 + dop_num):
                    if dictionary[number_2] == "|_|":
                        dictionary[number_2] = "|0|"
                        return dictionary
    # Проверка вертикальных линий на наличие 2-х своих элементов, и заполнение их
    for dop_num in range(0, 3, 1):
        count = 0
        for number in range(1 + dop_num, 8 + dop_num, 3):
            if dictionary[number] == "|0|":
                count += 1
            if count == 2:
                for number_2 in range(1 + dop_num, 8 + dop_num, 3):
                    if dictionary[number_2] == "|_|":
                        dictionary[number_2] = "|0|"
                        return dictionary
    # Проверка диагональных линий на наличие 2-х своих элементов, и заполнение их
    a_left_right = 0
    b_right_left = 0
    for num_diagonal in range(1, 10, 2):
        if dictionary[num_diagonal] == "|0|":
            if num_diagonal in [1, 5, 9]:
                a_left_right += 1
            if num_diagonal in [3, 5, 7]:
                b_right_left += 1
    if a_left_right == 2:
        for num_diagonal_2 in range(1, 10, 4):
            if dictionary[num_diagonal_2] == "|_|":
                dictionary[num_diagonal_2] = "|0|"
                return dictionary
    if b_right_left == 2:
        for num_diagonal_2 in range(3, 8, 2):
            if dictionary[num_diagonal_2] == "|_|":
                dictionary[num_diagonal_2] = "|0|"
                return dictionary
    #  Проверка горизонтальных линий на наличие 2-х элементов противника, и заполнение их
    for dop_num in range(0, 9, 3):
        count = 0
        for number in range(1 + dop_num, 4 + dop_num):
            if dictionary[number] == "|*|":
                count += 1
            if count == 2:
                for number_2 in range(1 + dop_num, 4 + dop_num):
                    if dictionary[number_2] == "|_|":
                        dictionary[number_2] = "|0|"
                        return dictionary
    # Проверка вертикальных линий на наличие 2-х элементов противника, и заполнение их
    for dop_num in range(0, 3, 1):
        count = 0
        for number in range(1 + dop_num, 8 + dop_num, 3):
            if dictionary[number] == "|*|":
                count += 1
            if count == 2:
                for number_2 in range(1 + dop_num, 8 + dop_num, 3):
                    if dictionary[number_2] == "|_|":
                        dictionary[number_2] = "|0|"
                        return dictionary
    # Проверка диагональных линий на наличие 2-х элементов противника, и заполнение их
    a_left_right_def = 0
    b_right_left_def = 0
    for num_diagonal_player in range(1, 10, 2):
        if dictionary[num_diagonal_player] == "|*|":
            if num_diagonal_player in [1, 5, 9]:
                a_left_right_def += 1
            if num_diagonal_player in [3, 5, 7]:
                b_right_left_def += 1
    if a_left_right_def == 2:
        for num_diagonal_player_2 in range(1, 10, 4):
            if dictionary[num_diagonal_player_2] == "|_|":
                dictionary[num_diagonal_player_2] = "|0|"
                return dictionary
    if b_right_left_def == 2:
        for num_diagonal_player_2 in range(3, 8, 2):
            if dictionary[num_diagonal_player_2] == "|_|":
                dictionary[num_diagonal_player_2] = "|0|"
                return dictionary
    # Вариант с созданием победной позиции уголком
    if a_left_right == 2:
        if dictionary[1] == "|0|" and dictionary[5] == "|0|":
            for dop_el_left_right_1 in range(2, 5, 2):
                if dictionary[dop_el_left_right_1] == "|_|":
                    dictionary[dop_el_left_right_1] = "|0|"
                    return dictionary
        else:
            for dop_el_left_right_2 in range(6, 9, 2):
                if dictionary[dop_el_left_right_2] == "|_|":
                    dictionary[dop_el_left_right_2] = "|0|"
                    return dictionary
    if b_right_left == 2:
        if dictionary[3] == "|0|" and dictionary[5] == "|0|":
            for dop_el_right_left_1 in range(2, 7, 4):
                if dictionary[dop_el_right_left_1] == "|_|":
                    dictionary[dop_el_right_left_1] = "|0|"
                    return dictionary
        else:
            for dop_el_right_left_2 in range(4, 9, 4):
                if dictionary[dop_el_right_left_2] == "|_|":
                    dictionary[dop_el_right_left_2] = "|0|"
                    return dictionary
    # Блокировака большого уголка
    if dictionary[1] == "|*|" and dictionary[9] == "|*|":
        for magic_left_right in range(2, 9, 2):
            if dictionary[magic_left_right] == "|_|":
                dictionary[magic_left_right] = "|0|"
                return dictionary
    if dictionary[3] == "|*|" and dictionary[7] == "|*|":
        for magic_right_left in range(2, 9, 2):
            if dictionary[magic_right_left] == "|_|":
                dictionary[magic_right_left] = "|0|"
                return dictionary
    # Занимает 5 клетку если она свободна, либо 1, 3, 7, 9, (1 ход программы).
    if dictionary[5] == "|_|":
        dictionary[5] = "|0|"
        return dictionary
    else:
        for diag_temp in range(1, 10, 2):
            if dictionary[diag_temp] == "|_|":
                dictionary[diag_temp] = "|0|"
                return dictionary
    return dictionary


def search_winner(dictionary: dict) -> int:
    # Номера
    num_player = 1
    num_program = 2
    # Горизонтальная проверка
    for temp_horizon in range(0, 9, 3):
        count_player = 0
        count_program = 0
        for horizon in range(1 + temp_horizon, 4 + temp_horizon):
            if dictionary[horizon] == "|*|":
                count_player += 1
            if dictionary[horizon] == "|0|":
                count_program += 1
        if count_player == 3:
            return num_player
        if count_program == 3:
            return num_program
    # Вертикальная проверка
    for temp_vertical in range(0, 3, 1):
        count_player = 0
        count_program = 0
        for vertical in range(1 + temp_vertical, 8 + temp_vertical, 3):
            if dictionary[vertical] == "|*|":
                count_player += 1
            if dictionary[vertical] == "|0|":
                count_program += 1
        if count_player == 3:
            return num_player
        if count_program == 3:
            return num_program
    # Диагональная проверка (слева направо)
    count_player = 0
    count_program = 0
    for diagonal_left_right in range(1, 10, 4):
        if dictionary[diagonal_left_right] == "|*|":
            count_player += 1
        if dictionary[diagonal_left_right] == "|0|":
            count_program += 1
    if count_player == 3:
        return num_player
    if count_program == 3:
        return num_program
    # Диагональная проверка (справа налево)
    count_player = 0
    count_program = 0
    for diagonal_right_left in range(3, 8, 2):
        if dictionary[diagonal_right_left] == "|*|":
            count_player += 1
        if dictionary[diagonal_right_left] == "|0|":
            count_program += 1
    if count_player == 3:
        return num_player
    if count_program == 3:
        return num_program

def game():
    new_table = copy.deepcopy(my_dict_table)
    who_begin = int(input("Если вы хотите делать ход первым введите - 1, если вторым - 2: "))
    for hod in range(1, 10):
        if who_begin == 1:
            print(table(new_table))
            if hod % 2 != 0:
                table(hod_chose(new_table, int(input("Ваш ход: "))))
                print("")
            else:
                print("Бот делает ход")
                table(hod_robot_def(new_table))
                print("")
            if search_winner(new_table) == 1:
                print("Вы победили !!!")
                break
            if search_winner(new_table) == 2:
                print("Вы проиграли (")
                break
            if hod == 9:
                print("Ничья")
                break
        if who_begin == 2:
            if hod % 2 == 0:
                table(hod_chose(new_table, int(input("Сделайте ход: "))))
                print("")
            else:
                print("Бот делает ход")
                table(hod_robot_def(new_table))
                print("")
            if search_winner(new_table) == 1:
                print("Вы победили !!!")
                break
            if search_winner(new_table) == 2:
                print("Вы проиграли (")
                break
            if hod == 9:
                print("Ничья")
                break
    vopr = input("Хотите начать новую игру? y/n: ")
    if vopr == "y":
        return game()
    else:
        return print("Спасибо за игру")

game()