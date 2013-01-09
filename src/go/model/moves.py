# coding=utf-8
from copy import deepcopy
from game_state import GameState

def advance_turn(gs):
    gs._move_count += 1
    gs.active_player, gs.second_player = gs.second_player, gs.active_player
    return gs

def stone_placing_stage(gs):
    return gs.stage == 'stone placing'

def dead_stones_removing_stage(gs):
    return gs.stage == 'dead stones removing'

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
                and board.get_token(row, column) == 'empty'
                and gs.ko != (row, column)):
            return False
        self._place_stone(board, gs.active_player)
        for r, c in board.get_neighbours(row, column):
            tok = board.get_token(r, c)
            if  tok == "empty" or (tok == gs.second_player and board.is_dead(r, c)):
                return True
        return not board.is_dead(row, column)

    def __call__(self, gs):
        board = gs.board
        row, column = self._row, self._column
        self._place_stone(board, gs.active_player)
        captives_count = 0
        captive = None
        for r, c in board.get_neighbours(row, column):
            if board.get_token(r, c) == gs.second_player and board.is_dead(r, c):
                captives_count += board.remove_group(r, c)
                captive = (r, c)
        gs.captives_count[gs.active_player] += captives_count
        gs.ko = None
        if captives_count == 1:
            new_board = deepcopy(board)
            new_board.set_token(*captive, token=gs.second_player)
            if (new_board.is_dead(row, column)
                    and len(new_board.get_group(row, column)[0]) == 1):
                gs.ko = captive
        gs.board = board
        gs.consecutive_passes = 0
        return advance_turn(gs)


class PassMove(object):

    def __call__(self, gs):
        gs._move_count += 1
        gs.consecutive_passes += 1
        if gs.consecutive_passes >= 2:
            gs.stage = 'dead stones removing'
        return advance_turn(gs)

    def validate(self, gs):
        return stone_placing_stage(gs) and gs.consecutive_passes < 2


class ClaimDeadStoneMove(object):

    def __init__(self, row, column):
        self._row = row
        self._column = column

    def __call__(self, gs):
        gs.board.remove_group(self._row, self._column)
        return gs

    def validate(self, gs):
        row, column = self._row, self._column
        return (dead_stones_removing_stage(gs)
                and gs.board.on_board(row, column)
                and gs.board.get_token(row, column) != 'empty')

class PlaceHandicapStoneMove(object):

    def __init__(self, row, column):
        self._r = row
        self._c = column

    def validate(self, gs):
        return gs.board.get_size() == 19 and gs._move_count == 0 and gs.handicaps_placed < 9 \
            and gs.board.on_board(self._r, self._c) and gs.board.get_token(self._r, self._c) == 'empty'

    def __call__(self, gs):
        gs.board.set_token(self._r, self._c, 'black')
        gs.handicaps_placed += 1
        gs.active_player = 'white'
        gs.second_player = 'black'
        return gs
