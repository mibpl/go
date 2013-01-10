# coding=utf-8
import unittest
from score_game import AreaScoring
from game_state import GameState
from board_model import BoardModel

class TestScoring(unittest.TestCase):

    def setUp(self):
        self.score_area = AreaScoring()
        self.game_state = GameState()
        self.game_state.board = BoardModel.from_string(
                "e e w e\n"
                "w e w b\n"
                "b w b e\n"
                "e b e e")
        self.game_state.stage = "dead stones removing"
        self.captives_count = {
                "black": 15,
                "white": 15
                }

    def test_area_scoring(self):
        self.assertEqual({
                "black": 8,
                "white": 7+5.5
                }, self.score_area.score(self.game_state))
        self.assertEqual({
                "black": 8,
                "white": 7+1.5
                }, AreaScoring(1.5).score(self.game_state))
        self.game_state.handicaps_placed = 1
        self.assertEqual({
                "black": 8,
                "white": 7+0.5
                }, AreaScoring(1.5).score(self.game_state))


if __name__ == '__main__':
    unittest.main()
