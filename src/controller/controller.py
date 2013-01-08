from .model.game_history import GameHistory
from .model.moves import PlaceStoneMove

class Controller(object):
    def __init__(self):
        self._history = GameHistory()
        self._time = 0
        self._view = None

    def set_view(self, view):
        self._view = view
        self._update_view()

    def click(self, row, column):
        player = 'black' if self._time % 2 == 0 else 'white'  # dirty hack, fix
        move = PlaceStoneMove(row, column, player)
        # TODO: validate move
        self._history.append_move(move)
        self._time += 1
        self._update_view()

    def _update_view(self):
        if self._view is not None:
            state = self._history.get_state_after_move(self._time)
            self._view.set_board(state.board)

