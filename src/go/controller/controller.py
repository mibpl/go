from ..model.moves import PlaceStoneMove, PassMove

class Controller(object):
    def __init__(self, game_history, place_stone_move=PlaceStoneMove, pass_move=PassMove):
        self._history = game_history
        self._time = 0
        self._view = None
        self._place_stone_move = place_stone_move
        self._pass_move = pass_move

    def set_view(self, view):
        self._view = view
        self._update_view()

    def get_time(self):
        return self._time

    def _is_current(self):
        return self._time == self._history.get_num_moves()

    def _is_start(self):
        return self._time == 0

    def _execute_move(self, move):
        if not self._is_current():
            self._view.display_message(
                "Go to the last state before making a new move.")
            return
        game_state = self._get_current_state()
        if not move.validate(game_state):
            self._view.display_message(
                "This is not a valid move.")
            return
        self._history.append_move(move)
        self._time += 1
        self._update_view()

    def click(self, row, column):
        assert self._view is not None
        self._execute_move(self._place_stone_move(row, column))

    def do_pass(self):
        assert self._view is not None
        self._execute_move(self._pass_move())

    def navigate_prev(self):
        assert self._view is not None
        if self._is_start():
            self._view.display_message(
                "Already in the first state. Cannot go back.")
            return
        self._time -= 1
        self._update_view()

    def navigate_next(self):
        assert self._view is not None
        if self._is_current():
            self._view.display_message(
                "Already in the last state. Cannot go forward.")
            return
        self._time += 1
        self._update_view()

    def _get_current_state(self):
        return self._history.get_state_after_move(self._time)

    def _update_view(self):
        game_state = self._get_current_state()
        self._view.set_game_state(game_state)

