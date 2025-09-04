class Piece:
    def __init__(self, color):
        self._color = color
        self._name = None

    def get_color(self):
        return self._color
    
    def get_name(self):
        return self._name
    
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Pawn'

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Rook'

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Knight'

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Bishop'

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'Queen'

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self._name = 'King'