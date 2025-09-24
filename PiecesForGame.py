class Piece:
    def __init__(self, color):
        self._color = color
        self._name = None
        self._symbol = None

    def get_color(self):
        return self._color
    
    def get_name(self):
        return self._name
    
    def get_symbol(self):
        return self._symbol
    
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Pawn'
        self._ep_on = False
        if self._color == 'BLACK':
            self._symbol = '♙'
        elif self._color == 'WHITE':
            self._symbol = '♟'

    def get_ep_on(self):
        return self._ep_on

    def set_ep_on(self, state):
        self._ep_on = state
    
    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        delta_row = to_row - from_row
        delta_col = to_col - from_col
        temp_row = from_row
        temp_col = from_col
        if delta_row > 0:
            step_row = 1
        elif delta_row < 0:
            step_row = -1
        else:
            step_row = 0
        if delta_col > 0:
            step_col = 1
        elif delta_col < 0:
            step_col = -1
        else:
            step_col = 0

        if board[from_row][from_col] == 'WHITE':
            if (delta_row < 0) and (delta_col == 0):
                if (from_row == 7) and (abs(delta_row) == 2) and (self._ep_on is False):
                    self._ep_on == True
                    for square in range (abs(delta_row) - 1):
                        temp_row = temp_row + step_row
                        if (board[temp_row][to_col] is not None):
                            return False
                        else:
                            return True
                elif (from_row != 7) and (self._ep_on is False) and (abs(delta_row) == 1):
                    if (board[to_row][to_col] is not None):
                        return False
                    else:
                        return True
            elif (delta_row == 1) and (abs(delta_col) == 1):
                if board[to_row][to_col] is None:
                    return False
                elif (board[from_row][to_col].get_name() == 'Pawn') and (board[from_row][to_col].get_color() != board[from_row][from_col].get_color()):
                    if board[from_row][to_col].get_ep_on() is True:
                        return True
                    else:
                        return False
                else:
                    if board[to_row][to_col].get_color() == board[from_row][from_col].get_color():
                        return False
                    else:
                        return True
        elif self._color == 'BLACK':
            return False

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Rook'
        if self._color == 'BLACK':
            self._symbol = '♖'
        elif self._color == 'WHITE':
            self._symbol = '♜'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        delta_row = to_row - from_row
        delta_col = to_col - from_col
        temp_row = from_row
        temp_col = from_col
        if delta_row > 0:
            step_row = 1
        elif delta_row < 0:
            step_row = -1
        else:
            step_row = 0
        if delta_col > 0:
            step_col = 1
        elif delta_col < 0:
            step_col = -1
        else:
            step_col = 0

        if ((abs(delta_row) == 0) or (abs(delta_col) == 0)) and (1 <= abs(delta_row) + abs(delta_col)):
            for square in range(abs(delta_row) + abs(delta_col) - 1):
                temp_row = temp_row + step_row
                temp_col = temp_col + step_col
                if (board[temp_row][temp_col] is not None) and (temp_row != to_row and temp_col != to_col):
                    return False
                else:
                    return True
            return True
        else:
            return False

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Knight'
        if self._color == 'BLACK':
            self._symbol = '♘'
        elif self._color == 'WHITE':
            self._symbol = '♞'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        delta_row = to_row - from_row
        delta_col = to_col - from_col

        if (abs(delta_row) == 2 or abs(delta_col) == 2) and (abs(delta_row) == 1 or abs(delta_col) == 1):
            return True
        else:
            return False

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Bishop'
        if self._color == 'BLACK':
            self._symbol = '♗'
        elif self._color == 'WHITE':
            self._symbol = '♝'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        delta_row = to_row - from_row
        delta_col = to_col - from_col
        temp_row = from_row
        temp_col = from_col
        if delta_row > 0:
            step_row = 1
        elif delta_row < 0:
            step_row = -1
        else:
            step_row = 0
        if delta_col > 0:
            step_col = 1
        elif delta_col < 0:
            step_col = -1
        else:
            step_col = 0

        if (abs(delta_row) == abs(delta_col)) and (1 <= abs(delta_row)):
            for square in range(abs(delta_row) - 1):
                temp_row = temp_row + step_row
                temp_col = temp_col + step_col
                if (board[temp_row][temp_col] is not None) and (temp_row != to_row and temp_col != to_col):
                    return False
                else:
                    return True
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Queen'
        if self._color == 'BLACK':
            self._symbol = '♕'
        elif self._color == 'WHITE':
            self._symbol = '♛'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        delta_row = to_row - from_row
        delta_col = to_col - from_col
        temp_row = from_row
        temp_col = from_col
        if delta_row > 0:
            step_row = 1
        elif delta_row < 0:
            step_row = -1
        else:
            step_row = 0
        if delta_col > 0:
            step_col = 1
        elif delta_col < 0:
            step_col = -1
        else:
            step_col = 0

        if (abs(delta_row) == 0 or abs(delta_col) == 0) and (1 <= abs(delta_row) + abs(delta_col)):
            for square in range(abs(delta_row) + abs(delta_col)):
                temp_row = temp_row + step_row
                temp_col = temp_col + step_col
                if (board[temp_row][temp_col] is not None) and (temp_row != to_row and temp_col != to_col):
                    return False
                else:
                    return True
            return True
        elif (abs(delta_row) == abs(delta_col)) and (1 <= abs(delta_row)):
            for square in range(abs(delta_col) - 1):
                temp_row = temp_row + step_row
                temp_col = temp_col + step_col
                if (board[temp_row][temp_col] is not None) and (temp_row != to_row and temp_col != to_col):
                    return False
                else:
                    return True
            return True
        else:
            return False

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'King'
        if self._color == 'BLACK':
            self._symbol = '♔'
        elif self._color == 'WHITE':
            self._symbol = '♚'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        delta_row = to_row - from_row
        delta_col = to_col - from_col
        temp_row = from_row
        temp_col = from_col
        if delta_row > 0:
            step_row = 1
        elif delta_row < 0:
            step_row = -1
        else:
            step_row = 0
        if delta_col > 0:
            step_col = 1
        elif delta_col < 0:
            step_col = -1
        else:
            step_col = 0

        if (abs(delta_row) == 0 or abs(delta_col) == 0) and (1 == abs(delta_row) + abs(delta_col)):
            for square in range(abs(delta_row) + abs(delta_col)):
                temp_row = temp_row + step_row
                temp_col = temp_col + step_col
                if (board[temp_row][temp_col] is not None) and (temp_row != to_row and temp_col != to_col):
                    return False
                else:
                    return True
            return True
        elif (abs(delta_row) == abs(delta_col)) and (1 == abs(delta_row)):
            for square in range(abs(delta_col) - 1):
                temp_row = temp_row + step_row
                temp_col = temp_col + step_col
                if (board[temp_row][temp_col] is not None) and (temp_row != to_row and temp_col != to_col):
                    return False
                else:
                    return True
            return True
        else:
            return False