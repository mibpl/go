from move import Move

class PlaceStoneMove(Move):
    def __init__(self, row, column, token):
        self._row = row
        self._column = column
        self._token = token

    def validate(self, game_state):
        return True

    def make(self, game_state):
        game_state.get_board().set_token(self._row, self._column, self._token)

