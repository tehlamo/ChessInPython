from PiecesForGame import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class ChessGame:
    def __init__(self):
        self._board = []
        for col in range(8):
            row = [None, None, None, None, None, None, None, None]
            self._board.append(row)
        self._game_state = 'UNFINISHED'
        self._current_turn = 'WHITE'
        self._sp_starting_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        self._pawn_starting_row = [Pawn]*8
        for col in range(8):
            self._board[0][col] = self._sp_starting_row[col]('BLACK')
            self._board[1][col] = self._pawn_starting_row[col]('BLACK')
            self._board[6][col] = self._pawn_starting_row[col]('WHITE')
            self._board[7][col] = self._sp_starting_row[col]('WHITE')

    def get_game_state(self):
        return self._game_state
    
    def get_current_turn(self):
        return self._current_turn
    
    def get_game(self):
        for col in range(len(self._board)):
            symbols = []
            for row in range(len(self._board[col])):
                if self._board[col][row] is None:
                    symbols.append("□")
                else:
                    symbols.append(self._board[col][row].get_symbol())
            symbol_col = " ".join(symbols)
            print(symbol_col)

    def make_move(self, from_sq, to_sq):
        from_coord = self._get_indicies(from_sq)
        to_coord = self._get_indicies(to_sq)
        if  self._current_turn == 'WHITE':
            for square in range(len(self._board[6])):
                if (self._board[6][square].get_name() == 'Pawn') and (self._board[6][square].get_color() == self._current_turn):
                    self._board[6][square].set_ep_on = False
        elif self._current_turn == 'BLACK':
            for sqaure in range(len(self.board[4][square])):
                if (self._board[4][square].get_name() == 'Pawn') and (self._board[4][square].get_color() == self._current_turn):
                    self._board[4][sqaure].set_ep_on = False

        if (from_coord is None) or (to_coord is None):
            return False
        else:
            from_row, from_col = from_coord
            to_col, to_row = to_coord
            if self._board[from_row][from_col].get_color() != self._current_turn:
                print("Invalid move, it is currently", self._current_turn, "player's turn.")
                return False
            elif self._board[from_row][from_col] is None:
                print("Invalid move, piece to move doesn't exist.")
                return False

    def _get_indicies(self, coordinate):
        number = int(coordinate[1])
        row = number - 1
        letter = coordinate[0]
        col = ord(letter) - ord('a')
        return row, col