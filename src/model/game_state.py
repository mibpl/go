from copy import copy
from board_model import BoardModel
from player import Player

class GameState(object):
    def __init__(self, board=BoardModel(19), active_player=Player('black'), second_player=Player('white')):
        self.board = board
        self.active_player = active_player
        self.second_player = second_player
