from ..model.moves import PlaceStoneMove, PassMove, ClaimDeadStoneMove, PlaceHandicapStoneMove
from ..model.score_game import AreaScoring

class Controller(object):
    def __init__(self, game_history, place_stone_move=PlaceStoneMove, pass_move=PassMove, claim_dead_stone_move=ClaimDeadStoneMove, handicap_move=PlaceHandicapStoneMove):
        self._history = game_history
        self._time = 0
        self._view = None
        self._place_stone_move = place_stone_move
        self._pass_move = pass_move
        self._claim_dead_stone_move = claim_dead_stone_move
        self._handicap_move = handicap_move
        self.sethandicaps = True

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
        game_state = self._get_current_state()
        if self.sethandicaps:
            self._execute_move(self._handicap_move(row, column))
        elif game_state.stage == 'stone placing':
            self._execute_move(self._place_stone_move(row, column))
        else:
            self._execute_move(self._claim_dead_stone_move(row, column))

    def do_pass(self):
        assert self._view is not None
        self._execute_move(self._pass_move())

    def do_handicaps_done(self):
        assert self._view is not None
        self.sethandicaps = False

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

    def score(self):
        assert self._view is not None
        game_state = self._get_current_state()
        score = AreaScoring().score(game_state)
        black, white = score['black'], score['white']
        if black > white:
            result = "Black wins."
        elif black == white:
            result = "Draw."
        else:  # black < white
            result = "White wins."
        self._view.display_message(
                "Black: " + str(black) + ". White: " + str(white) + ". " + result)

    def _get_current_state(self):
        return self._history.get_state_after_move(self._time)

    def _update_view(self):
        game_state = self._get_current_state()
        self._view.set_game_state(game_state)

