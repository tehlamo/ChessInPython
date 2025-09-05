from ChessGame import ChessGame

program = True

def play_game():
    game = ChessGame()
    print("Welcome to Chess! Type moves like 'g1 e1' to move pieces. To check the board, type 'get_game.' Type 'get_game_state' to see the game state. Type 'get_current_turn' to see whose turn it is. Type 'quit' to quit. Type 'force_quit' to exit the program.")
    while True:
        user_input = input("Enter command: ").strip().lower()
        if user_input == 'quit':
            print("Quit successful. Type new to create a new game.")
            break
        elif user_input == 'get_game_state':
            print("Game State: ", game.get_game_state())
        elif user_input == 'get_game':
            print("Game Board:")
            game.get_game()
        elif user_input == 'get_current_turn':
            game.get_current_turn()

while program is True:
    print("To start a new game, type 'new.'")
    user_input = input("Enter Command: ")
    if user_input == 'new':
        play_game()
    elif user_input == 'force_quit':
        program = False
        break
    else:
        print("Type 'new' to start the game.")