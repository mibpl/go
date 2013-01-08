from game_state import GameState

def advance_turn(gs):
    gs.active_player, gs.second_player = gs.second_player, gs.active_player
    return gs

class PlaceStoneMove(object):
    def __init__(self, row, column, token):
        self._row = row
        self._column = column
        self._token = token

    def validate(self, gs):
        return gs.board.get_token(self._row, self._column) == 'empty' and gs.active_player.token == self._token

    def __call__(self, gs):
        gs.board.set_token(self._row, self._column, self._token)
        return advance_turn(gs)

class Pass(object):
    def __call__(self, gs):
        return advance_turn(gs)
    
    def validate(self, gs):
        return True
