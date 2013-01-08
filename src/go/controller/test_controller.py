# coding=utf-8
import unittest
import mock
from .controller import Controller
from ..model.moves import PlaceStoneMove, PassMove

class TestBoardModel(unittest.TestCase):

    def test_click(self):
        game_history_mock = mock.Mock()
        view_mock = mock.Mock()
        controller = Controller(game_history_mock)
        controller.set_view(view_mock)
        controller.click(4, 4)
        game_history_mock.append_move.assert_called()
        view_mock.set_game_state.assert_called()

    def test_do_pass(self):
        game_history_mock = mock.Mock()
        view_mock = mock.Mock()
        controller = Controller(game_history_mock)
        controller.set_view(view_mock)
        controller.do_pass()
        game_history_mock.append_move.assert_called(PassMove())
        view_mock.set_game_state.assert_called()

if __name__ == '__main__':
    unittest.main()
