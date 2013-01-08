# coding=utf-8
import unittest
import player

class TestPlayer(unittest.TestCase):


    def test(self):
        ap = player.Player('black', "Alice")
        self.assertEqual('black', ap.token)
        self.assertEqual("Alice", ap.name)

if __name__ == '__main__':
    unittest.main()
