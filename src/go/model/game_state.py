from copy import copy
from board_model import BoardModel

class GameState(object):
    def __init__(self, board=BoardModel(19)):
        self.board = board
        self.active_player = 'black'
        self.second_player = 'white'
        self.stage = 'stone placing'  # or 'dead stones removing'
        self.consecutive_passes = 0
        self.captives_count = {'black': 0, 'white': 0}
        self.ko = None
