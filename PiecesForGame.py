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
        if self._color == 'BLACK':
            self._symbol = '♙'
        elif self._color == 'WHITE':
            self._symbol = '♟'

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
                elif (board[temp_row][temp_col] is not None) and (temp_row == to_row and temp_col == to_col):
                    if board[temp_row][temp_col].get_color() == self._color:
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

        if (self._color == 'BLACK') and (from_row == 2) and (1 == abs(delta_row) or abs(delta_row) == 2) and (delta_row < 0):
            for square in range(abs(delta_row + delta_col) - 1):
                temp_row = temp_row + step_row
                temp_col = temp_col + step_col
                if (board[temp_row][temp_col] is not None) and (temp_row != to_row and temp_col != to_col):
                    return False
                elif (board[temp_row][temp_col] is not None) and (temp_row == to_row and temp_col == to_col):
                    if board[temp_row][temp_col].get_color() == self._color:
                        return False
                    else:
                        return True
            return True
        elif (self._color == 'WHITE') and (from_row == 7) and (abs(delta_row) == 1 or abs(delta_row) == 2) and (delta_row > 0):
            for square in range(abs(delta_row + delta_col) - 1):
                temp_row = temp_row + step_row
                temp_col = temp_col + step_col
                if (board[temp_row][temp_col] is not None) and (temp_row != to_row and temp_col != to_col):
                    return False
                elif (board[temp_row][temp_col] is not None) and (temp_row == to_row and temp_col == to_col):
                    if board[temp_row][temp_col].get_color() == self._color:
                        return False
                    else:
                        return True
            return True
        elif (self._color == 'BLACK') and (from_row != 2 and from_row != 5) and (abs(delta_row) == 1) and (delta_row < 0):
            if (board[to_row][to_col] is not None) and (board[temp_row][temp_col].get_color() == self._color):
                return False
            else:
                return True
        elif  (self._color == 'WHITE') and (from_row != 7 and from_row != 4) and (abs(delta_row) == 1) and (delta_row > 0):
            if (board[to_row][to_col] is not None) and (board[temp_row][temp_col].get_color() == self._color):
                return False
            else:
                return True
        elif (self._color == 'BLACK') and (from_row == 5):
            if (board[from_row][from_col + 1].get_name() == 'Pawn') and (delta_row > 0) and (abs(delta_row) == abs(delta_col)):
                

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
                elif (board[temp_row][temp_col] is not None) and (temp_row == to_row and temp_col == to_col):
                    if board[temp_row][temp_col].get_color() == self._color:
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
                elif (board[temp_row][temp_col] is not None) and (temp_row == to_row and temp_col == to_col):
                    if board[temp_row][temp_col].get_color() == self._color:
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
                elif (board[temp_row][temp_col] is not None) and (temp_row == to_row and temp_col == to_col):
                    if board[temp_row][temp_col].get_color() == self._color:
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
                elif (board[temp_row][temp_col] is not None) and (temp_row == to_row and temp_col == to_col):
                    if board[temp_row][temp_col].get_color() == self._color:
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
                elif (board[temp_row][temp_col] is not None) and (temp_row == to_row and temp_col == to_col):
                    if board[temp_row][temp_col].get_color() == self._color:
                        return False
                    else:
                        return True
            return True
        else:
            return False