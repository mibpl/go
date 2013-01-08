# coding=utf-8
import unittest
from board_model import BoardModel
from game_history import GameHistory
from game_state import GameState
import moves

class TestGameHistory(unittest.TestCase):
    def test1(self):
        h = GameHistory(GameState(BoardModel(3)))
        m = [moves.PassMove('black'), moves.PlaceStoneMove(0, 0, 'white'), moves.PlaceStoneMove(2, 1, 'black')]
        for x in m:
            h.append_move(x)
        board_text = (
                u"w e e\n"
                u"e e e\n"
                u"e b e")
        self.assertEqual(3, h.get_num_moves())
        g = h.get_state_after_move(3)
        b = g.board
        self.assertEqual(board_text, unicode(b))
        
        g = h.get_state_after_move(3)
        b = g.board
        self.assertEqual(board_text, unicode(b))
        
        self.assertFalse(m[-1].validate(g))


if __name__ == '__main__':
    unittest.main()
