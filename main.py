from ChessGame import ChessGame

program = True

def play_game():
    game = ChessGame()
    print("Welcome to Chess! Type moves like 'g1 e1' to move pieces. To check the board, type 'get_game.' Type 'get_game_state' to see the game state. Type 'get_current_turn' to see whose turn it is. Type 'quit' to quit.")
    while True:
        user_input = input("Enter command: ").strip().lower()
        if user_input == 'quit':
            print("Quit successful. Type new to create a new game.")
            break
        elif user_input == 'get_game_state':
            print("Game State: ", game.get_game_state())
        elif user_input == 'get_current_turn':
            print("Current turn:", game.get_current_turn())
        elif user_input == 'get_game':
            print("Game Board:")
            game.get_game()
        elif user_input == 'commands':
            print("Type moves like 'g1 e1' to move pieces. To check the board, type 'get_game.' Type 'get_game_state' to see the game state. Type 'get_current_turn' to see whose turn it is. Type 'quit' to quit.")
        else:
            valid_command = True
            split_input = user_input.split()
            if len(split_input) == 2:
                if len(split_input[0]) == 2 and len(split_input[1]) == 2:
                    if split_input[0][0].isalpha() is True and split_input[0][1].isdigit() is True:
                        if split_input[1][0].isalpha() is True and split_input[1][1].isdigit() is True:
                            game.make_move(split_input[0], split_input[1])
                        else:
                            valid_command = False
                    else:
                        valid_command = False
                else:
                    valid_command = False
            else:
                valid_command = False
            if valid_command is False:
                print("Command doesn't exist/typo was made for command, please try again. Type commands for the commands.")

while program is True:
    print("To start a new game, type 'new.' To exit the program, type 'force_quit.'")
    user_input = input("Enter Command: ")
    if user_input == 'new':
        play_game()
    elif user_input == 'force_quit':
        program = False
        break
    else:
        print("Type 'new' to start the game. Type 'force_quit' to exit the program.")