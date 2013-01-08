from ..model.moves import PlaceStoneMove, PassMove

class Controller(object):
    def __init__(self, game_history):
        self._history = game_history
        self._time = 0
        self._current_time = 0
        self._view = None

    def set_view(self, view):
        self._view = view
        self._update_view()

    def _is_current(self):
        return self._current_time == self._time

    def _is_start(self):
        return self._current_time == 0

    def _execute_move(self, move):
        self._history.append_move(move)
        self._time += 1
        self._update_view()

    def click(self, row, column):
        if not self._is_current():
            return
        state = self._get_current_state()
        move = PlaceStoneMove(row, column)
        self._execute_move(move)

    def do_pass(self):
        if not self._is_current():
            return
        move = PassMove()
        self._execute_move(move)

    def navigate_prev(self):
        if self._is_start():
            return
        self._current_time -= 1

    def navigate_next(self):
        if self._is_current():
            return
        self._current_time += 1

    def _get_current_state(self):
        return self._history.get_state_after_move(self._time)

    def _update_view(self):
        if self._view is not None:
            game_state = self._get_current_state()
            self._view.set_game_state(game_state)
