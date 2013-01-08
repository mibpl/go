# coding=utf-8
import unittest
from board_model import BoardModel
from game_state import GameState
from moves import PassMove, PlaceStoneMove

class TestPassMove(unittest.TestCase):

    def setUp(self):
        self.game_state = GameState()
        self.move = PassMove()

    def test_call(self):
        gs = self.move(self.game_state)
        self.assertEqual('white', gs.active_player)
        self.assertEqual(self.game_state.board, gs.board)

    def test_validate(self):
        gs = self.game_state
        move = self.move
        self.assertTrue(move.validate(gs))
        gs = self.move(gs)
        self.assertTrue(move.validate(gs))
        gs = self.move(gs)
        self.assertFalse(move.validate(gs))

    def test_validate_wrong(self):
        self.game_state.stage = 'dead stone removing'
        self.assertFalse(self.move.validate(self.game_state))


class TestPlaceStoneMove(unittest.TestCase):

    def setUp(self):
        self.board_string = (
                "w e e\n"
                "e b e\n"
                "w w b\n")
        self.board = BoardModel.from_string(self.board_string)
        self.game_state = GameState()
        self.game_state.board = self.board

    def test_not_allowed_move(self):
        self.assertFalse(PlaceStoneMove(2, 1).validate(self.game_state))


if __name__ == '__main__':
    unittest.main()

