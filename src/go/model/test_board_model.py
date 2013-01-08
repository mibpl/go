# coding=utf-8
import unittest
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



if __name__ == '__main__':
    unittest.main()
