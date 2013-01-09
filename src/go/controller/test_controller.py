# coding=utf-8
import unittest
import mock
from .controller import Controller
from ..model.moves import PlaceStoneMove, PassMove

class MockHistory:
    def __init__(self, state):
        self.moves = 0
        self.state = state

    def append_move(self, move):
        self.moves += 1

    def get_num_moves(self):
        return self.moves

    def get_state_after_move(self, time):
        return self.state

def mock_move(*args, **kwargs):
    move = mock.Mock()
    move.validate = mock.MagicMock(return_value=True)
    return move

class TestBoardModel(unittest.TestCase):

    def test_click(self):
        mock_state = mock.Mock()
        game_history_mock = mock.Mock(wraps=MockHistory(mock_state))
        view_mock = mock.Mock()
        move = mock_move()

        controller = Controller(game_history_mock, place_stone_move=lambda *args, **kwargs: move)
        controller.set_view(view_mock)
        controller.click(4, 4)

        self.assertEqual(1, controller.get_time())
        move.assert_called_once()
        move.validate.assert_called_once()
        game_history_mock.append_move.assert_called_with(move)
        view_mock.set_game_state.assert_called_with(mock_state)

    def test_do_pass(self):
        mock_state = mock.Mock()
        game_history_mock = mock.Mock(wraps=MockHistory(mock_state))
        view_mock = mock.Mock()
        move = mock_move()

        controller = Controller(game_history_mock, pass_move=lambda *args, **kwargs: move)
        controller.set_view(view_mock)
        controller.do_pass()

        self.assertEqual(1, controller.get_time())
        move.assert_called_once()
        move.validate.assert_called_once()
        game_history_mock.append_move.assert_called_with(move)
        view_mock.set_game_state.assert_called_with(mock_state)

if __name__ == '__main__':
    unittest.main()
