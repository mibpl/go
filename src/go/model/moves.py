# coding=utf-8
from game_state import GameState

def advance_turn(gs):
    gs.active_player, gs.second_player = gs.second_player, gs.active_player
    return gs

def stone_placing_stage(gs):
    return gs.stage == 'stone placing'


class PlaceStoneMove(object):
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def validate(self, gs):
        return gs.board.get_token(self._row, self._column) == 'empty'

    def __call__(self, gs):
        gs.board.set_token(self._row, self._column, gs.active_player)
        return advance_turn(gs)


class PassMove(object):

    def __call__(self, gs):
        gs.consecutive_passes += 1
        return advance_turn(gs)

    def validate(self, gs):
        return stone_placing_stage(gs) and gs.consecutive_passes < 2


class ClaimStoneDeadMove(object):
    # TODO: implement methods below.
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def __call__(self, gs):
        pass

    def validate(self, gs):
        pass

