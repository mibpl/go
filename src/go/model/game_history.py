from copy import deepcopy
from game_state import GameState

class GameHistory(object):
    def __init__(self, initial_state=GameState()):
        self._moves = []
        self._initial_state = deepcopy(initial_state)

    def append_move(self, move):
        assert move.validate(self.get_state_after_move(self.get_num_moves()))
        self._moves.append(move)

    def get_num_moves(self):
        return len(self._moves)

    def get_state_after_move(self, move_id):
        assert 0 <= move_id and move_id <= len(self._moves)
        state = deepcopy(self._initial_state)
        for move in self._moves[:move_id]:
            state = move(state)
        return state
