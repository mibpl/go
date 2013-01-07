from move import Move

class PlaceStoneMove(Move):
    def __init__(self, row, column, token):
        self._row = row
        self._column = column
        self._token

    def validate(self, game_state):
        return True

    def make(self, game_state):
        game_state.get_board().set_token(row, column, token)

