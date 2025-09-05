from PiecesForGame import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class ChessGame:
    def __init__(self):
        self._board = []
        for row in range(8):
            col = [None, None, None, None, None, None, None, None]
            self._board.append(col)
        self._game_state = 'UNFINISHED'
        self._current_turn = 'WHITE'
        self._sp_starting_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        self._pawn_starting_row = [Pawn]*8
        for row in range(8):
            self._board[0][row] = self._sp_starting_row[row]('BLACK')
            self._board[1][row] = self._pawn_starting_row[row]('BLACK')
            self._board[6][row] = self._pawn_starting_row[row]('WHITE')
            self._board[7][row] = self._sp_starting_row[row]('WHITE')

    def get_game_state(self):
        return self._game_state
    
    def get_current_turn(self):
        return self._current_turn
    
    def get_game(self):
        for row in range(len(self._board)):
            symbols = []
            for col in range(len(self._board[row])):
                if self._board[col][row] is None:
                    symbols.append("□")
                else:
                    symbols.append(self._board[row][col].get_symbol())
            symbol_row = " ".join(symbols)
            print(symbol_row)