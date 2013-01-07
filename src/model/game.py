from model.game_history import GameHistory
class Game(object):

    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2
        self._history = GameHistory()

    def get_history():
        return self._history

    def make_move(self, move):
        " add to history and start if correct else start (so same player, same history) "
        pass

    def start(self):
        "get current player and call get_move with self.make_move callback "
        pass
