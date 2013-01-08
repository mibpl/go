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
        # TODO: do not make move if we are not at the end of the history.
        # TODO: determine whose turn it is based on game_state.
        player = 'black' if self._time % 2 == 0 else 'white'  # dirty hack, fix
        move = PlaceStoneMove(row, column, player)
        # TODO: validate move
        self._history.append_move(move)
        self._time += 1
        self._update_view()

    def do_pass(self):
        pass

    def navigate_prev(self):
        pass

    def navigate_next(self):
        pass

    def _get_current_state(self):
        return self._history.get_state_after_move(self._time)
        
    def _update_view(self):
        if self._view is not None:
            game_state = self._get_current_state()
            self._view.set_game_state(game_state)

