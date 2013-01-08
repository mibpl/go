# coding=utf-8
import doctest
import unittest
from copy import deepcopy
from board_model import BoardModel

class TestBoardModel(unittest.TestCase):

    def test_get_size(self):
        self.assertEqual(3, BoardModel(3).get_size())
        self.assertEqual(4, BoardModel(4).get_size())

    def test_set_and_get_token(self):
        board  = BoardModel(3)
        board.set_token(0, 0, 'white')
        board.set_token(2, 1, 'black')
        self.assertEqual('black', board.get_token(2, 1))
        self.assertEqual('white', board.get_token(0, 0))
        self.assertEqual('empty', board.get_token(1, 1))

    def test_str_and_unicode(self):
        board = BoardModel(3)
        board.set_token(0, 0, 'white')
        board.set_token(2, 1, 'black')
        board_text = (
                u"w e e\n"
                u"e e e\n"
                u"e b e")
        self.assertEqual(board_text, unicode(board))
        self.assertEqual(board_text, str(board))

    def test_board_from_string(self):
        board_string = (
                "w e e\n"
                "e e e\n"
                "e b e")
        board = BoardModel.from_string(board_string)
        self.assertEqual(board_string, str(board))

    def test_on_board(self):
        board  = BoardModel(3)
        self.assertTrue(board.on_board(0, 0))
        self.assertTrue(board.on_board(2, 1))
        self.assertFalse(board.on_board(-1, 0))
        self.assertFalse(board.on_board(0, 3))
        self.assertFalse(board.on_board(3, 0))
        self.assertFalse(board.on_board(2, -2))

    def test_get_neighbours(self):
        board = BoardModel(3)
        self.assertEqual(
                [(0, 1), (1, 0), (1, 2), (2, 1)],
                sorted(board.get_neighbours(1, 1)))
        self.assertEqual(
                [(0, 1), (1, 0)],
                sorted(board.get_neighbours(0, 0)))

    def test_get_group(self):
        board_string = (
                "b b w e e\n"
                "b w e w e\n"
                "w b b w w\n"
                "e w w w e\n"
                "e e e w e")
        board = BoardModel.from_string(board_string)
        self.assertEqual(([(0, 0), (0, 1), (1, 0)], ("white", )),
                board.get_group(0, 0))
        self.assertEqual(([(2, 0)], ("black", "empty")),
                board.get_group(2, 0))
        self.assertEqual(([(3, 4), (4, 4)], ("white", )),
                board.get_group(4, 4))
        doctest.run_docstring_examples(
                BoardModel.get_group,
                {"BoardModel": BoardModel},
                name="get_group")

    def test_is_dead(self):
        board_string = (
                "b b w e e\n"
                "b w e w e\n"
                "w b b e w\n"
                "e w w b b\n"
                "e e b w w")
        board = BoardModel.from_string(board_string)
        self.assertTrue(board.is_dead(0, 0))
        self.assertFalse(board.is_dead(0, 3))
        self.assertTrue(board.is_dead(4, 4))
        self.assertFalse(board.is_dead(3, 0))

    def test_remove_group(self):
        board_string = (
                "b b w e e\n"
                "b w e w e\n"
                "w b b e w\n"
                "e w w b b\n"
                "e e b w w")
        board = BoardModel.from_string(board_string)
        self.assertEquals(3, deepcopy(board).remove_group(0, 0))
        self.assertEquals(2, deepcopy(board).remove_group(3, 1))
        self.assertEquals(0, deepcopy(board).remove_group(4, 0))
        self.assertEquals(3, board.remove_group(0, 0))
        self.assertEquals((
                "e e w e e\n"
                "e w e w e\n"
                "w b b e w\n"
                "e w w b b\n"
                "e e b w w"), str(board))


if __name__ == '__main__':
    unittest.main()
