# coding=utf-8
import unittest
from game_state import GameState
from moves import PassMove

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

if __name__ == '__main__':
    unittest.main()

