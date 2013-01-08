# coding=utf-8
from copy import deepcopy
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

    def _place_stone(self, board, player):
        board.set_token(self._row, self._column, player)

    def _delete_dead_neighbours(self, board, player):
        for r, c in board.get_neighbours(self._row, self._column):
            tok = board.get_token(r, c)
            if  tok not in ("empty", player) and board.is_dead(r, c):
                board.remove_group(r, c)

    def validate(self, gs):
        board = deepcopy(gs.board)
        row, column = self._row, self._column
        if not (stone_placing_stage(gs)
                and board.on_board(row, column)
                and board.get_token(row, column) == 'empty'):
            return False
        self._place_stone(board, gs.active_player)
        # TODO: implement KO rule
        for r, c in board.get_neighbours(row, column):
            tok = board.get_token(r, c)
            if  tok == "empty" or (tok == gs.second_player and board.is_dead(r, c)):
                return True
        return not board.is_dead(row, column)

    def __call__(self, gs):
        board = gs.board
        self._place_stone(board, gs.active_player)
        for r, c in board.get_neighbours(self._row, self._column):
            if board.get_token(r, c) == gs.second_player and board.is_dead(r, c):
                board.remove_group(r, c)
        gs.board = board
        return advance_turn(gs)


class PassMove(object):

    def __call__(self, gs):
        gs.consecutive_passes += 1
        return advance_turn(gs)

    def validate(self, gs):
        return stone_placing_stage(gs) and gs.consecutive_passes < 2


class ClaimDeadStoneMove(object):

    # TODO: implement methods below.
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def __call__(self, gs):
        pass

    def validate(self, gs):
        pass

