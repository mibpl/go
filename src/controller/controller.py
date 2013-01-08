from .model.moves import PlaceStoneMove

class Controller(object):
    def __init__(self, game_history):
        self._history = game_history
        self._time = 0
        self._view = None

    def set_view(self, view):
        self._view = view
        self._update_view()

    def click(self, row, column):
        state = self._get_current_state()
        player = state.active_player
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

