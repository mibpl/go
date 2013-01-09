# coding=utf-8
import unittest
from board_model import BoardModel
from game_state import GameState
from moves import ClaimDeadStoneMove, PassMove, PlaceStoneMove, PlaceHandicapStoneMove

class TestPassMove(unittest.TestCase):

    def setUp(self):
        self.game_state = GameState()
        self.move = PassMove()

    def test_call(self):
        gs = self.move(self.game_state)
        self.assertEqual('white', gs.active_player)
        self.assertEqual(self.game_state.board, gs.board)
        gs = self.move(gs)
        self.assertEqual('dead stones removing', gs.stage)

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


class TestHandicapMove(unittest.TestCase):

    def setUp(self):
        self.game_state = GameState()
        self.move = PlaceHandicapStoneMove(0, 0)

    def test_v(self):
        gs = self.move(self.game_state)
        self.assertEqual('white', gs.active_player)
        self.assertEqual('black', gs.board.get_token(0, 0))

    def test_call(self):
        self.assertTrue(self.move.validate(self.game_state))
        gs = self.move(self.game_state)
        self.assertEqual('white', gs.active_player)
        self.assertEqual('black', gs.board.get_token(0, 0))
        self.assertFalse(self.move.validate(gs))

class TestPlaceStoneMove(unittest.TestCase):

    def setUp(self):
        self.board_string = (
                "w e e\n"
                "e b e\n"
                "w w b")
        self.board = BoardModel.from_string(self.board_string)
        self.game_state = GameState()
        self.game_state.board = self.board

    def test_validate_not_allowed_move(self):
        self.assertFalse(PlaceStoneMove(2, 1).validate(self.game_state))
        self.assertFalse(PlaceStoneMove(-1, 1).validate(self.game_state))

    def test_validate_normal_move(self):
        self.assertTrue(PlaceStoneMove(0, 1).validate(self.game_state))

    def test_validate_wrong_stage(self):
        self.game_state.stage = 'dead stone removing'
        self.assertFalse(PlaceStoneMove(0, 1).validate(self.game_state))

    def test_validate_dead_stone(self):
        self.game_state.board = BoardModel.from_string(
                "e w e\n"
                "w w w\n"
                "e b b")
        self.assertFalse(PlaceStoneMove(2, 0).validate(self.game_state))

    def test_call_normal_move(self):
        game_state = PlaceStoneMove(0,1)(self.game_state)
        self.assertEquals((
                "w b e\n"
                "e b e\n"
                "w w b"), str(game_state.board))
        game_state = PlaceStoneMove(0,2)(game_state)
        self.assertEquals((
                "w b w\n"
                "e b e\n"
                "w w b"), str(game_state.board))

    def test_ko(self):
        board = BoardModel.from_string((
                "e e e e\n"
                "e b w e\n"
                "b w e w\n"
                "e b w e"))
        self.game_state.board = board
        game_state = self.game_state
        move = PlaceStoneMove(2, 2)
        self.assertTrue(move.validate(game_state))
        game_state = move(game_state)
        move = PlaceStoneMove(2, 1)
        self.assertFalse(move.validate(game_state))
        move = PlaceStoneMove(0, 1)
        self.assertTrue(move.validate(game_state))
        game_state = move(game_state)
        move = PlaceStoneMove(2, 1)
        self.assertTrue(move.validate(game_state))

    def test_clear_consecutive_passes_count(self):
        self.game_state.consecutive_passes = 1
        game_state = PlaceStoneMove(0, 2)(self.game_state)
        self.assertEqual(0, game_state.consecutive_passes)


class TestClaimDeadStoneMove(unittest.TestCase):

    def setUp(self):
        self.board_string = (
                "w e e\n"
                "w b e\n"
                "w w b")
        self.board = BoardModel.from_string(self.board_string)
        self.game_state = GameState()
        self.game_state.board = self.board
        self.game_state.stage = "dead stones removing"

    def test_validate_wrong_stage(self):
        self.game_state.stage = "stone placing"
        self.assertFalse(ClaimDeadStoneMove(0, 0).validate(self.game_state))

    def test_validate_empty_field(self):
        self.assertFalse(ClaimDeadStoneMove(0, 1).validate(self.game_state))

    def test_validate_ok(self):
        move = ClaimDeadStoneMove(0, 0)
        self.assertTrue(move.validate(self.game_state))
        game_state = move(self.game_state)
        self.assertEqual((
                "e e e\n"
                "e b e\n"
                "e e b"), str(game_state.board))

if __name__ == '__main__':
    unittest.main()

