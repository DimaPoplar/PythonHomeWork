from copy import deepcopy
import view
import game

table = game.Game(view.Visual.table())


def game_process():
    while True:
        index = view.Visual.menu_choice()
        main_table = deepcopy(table)
        match index:
            case 1:  # Player to Player
                position = view.Visual.choice_sign()
                begin = view.Visual.chose_position()
                for move in range(begin, 9 + begin):
                    if move % 2 == 0:
                        if move < 2:
                            main_table.print_table()
                        main_table.player_turn(position)
                    else:
                        main_table.player_turn(position)
                    view.Visual.publication_move(index, position)
                    position = main_table.queue(position)
                    main_table.print_table()
                    sign = main_table.search_winner()
                    if sign:
                        view.Visual.define_winner(sign)
                        break
                    if move == 8 + begin:
                        print("У вас ничья!")
            case 2:  # Player to Bot
                position = view.Visual.choice_sign()
                begin = view.Visual.chose_position()
                position_bot = table.queue(position)
                for move in range(begin, 9 + begin):
                    if move % 2 == 0:
                        if move < 2:
                            main_table.print_table()
                        main_table.player_turn(position)
                        view.Visual.publication_move(index, position, begin, move)
                    else:
                        main_table.bot_turn(position_bot, position)
                        view.Visual.publication_move(index, position_bot, begin, move)
                    main_table.print_table()
                    sign = main_table.search_winner()
                    if sign:
                        view.Visual.define_winner(sign)
                        break
                    if move == (8 + begin):
                        print("У вас ничья!")
            case 3:  # Bot to Bot
                position_1 = "X"
                position_2 = "O"
                for move in range(9):
                    if move % 2 == 0:
                        main_table.bot_turn(position_1, position_2)
                    else:
                        main_table.bot_turn(position_1, position_2)
                    view.Visual.publication_move(index, position_1)
                    main_table.print_table()
                    position_1 = table.queue(position_1)
                    position_2 = table.queue(position_2)
                    sign = main_table.search_winner()
                    if sign:
                        view.Visual.define_winner(sign)
                        break
                    if move == 8:
                        print("У ботов ничья!")
            case 4:  # Exit game
                break
