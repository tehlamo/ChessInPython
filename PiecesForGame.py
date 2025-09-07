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

    def is_valid_move(self, from_col, from_row, to_col, to_row, board):
        delta_col = to_col - from_col
        delta_row = to_row - from_row
        temp_col = from_col
        temp_row = from_row
        if delta_col > 0:
            step_col = 1
        elif delta_col < 0:
            step_col = -1
        else:
            step_col = 0
        if delta_row > 0:
            step_row = 1
        elif delta_row < 0:
            step_row = -1
        else:
            step_row = 0

        if ((abs(delta_col) == 0) or (abs(delta_row) == 0)) and (1 <= abs(delta_col) + abs(delta_row)):
            for square in range(abs(delta_col) + abs(delta_row) - 1):
                temp_col = temp_col + step_col
                temp_row = temp_row + step_row
                if board[temp_col][temp_row] is not None and temp_col != to_col and temp_row != to_row:
                    return False
                elif board[temp_col][temp_row] is not None and temp_col == to_col and temp_row == to_row:
                    if board[temp_col][temp_row].get_color() == self._color:
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

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Bishop'
        if self._color == 'BLACK':
            self._symbol = '♗'
        elif self._color == 'WHITE':
            self._symbol = '♝'

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Queen'
        if self._color == 'BLACK':
            self._symbol = '♕'
        elif self._color == 'WHITE':
            self._symbol = '♛'

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'King'
        if self._color == 'BLACK':
            self._symbol = '♔'
        elif self._color == 'WHITE':
            self._symbol = '♚'