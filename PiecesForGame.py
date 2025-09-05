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