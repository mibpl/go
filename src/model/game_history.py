class GameHistory(object):
    def __init__(self):
        self._moves = []

    def append_move(self, move):
        """
        Appends move if it is valid. Returns True on success.
        """
        cur_state = self.get_state_after_move(self.get_num_moves())
        if move.validate(cur_state):
            _moves.append(move)
            return True
        else:
            return False

    def get_num_moves(self):
        return len(self._moves)

    def get_state_after_move(self, move_id):
        assert 0 <= move_id and move_id <= len(self._moves)
        state = GameState() #TODO: how to initialize game state?
        for move in self._moves[:move_id]:
            move.make(state)
        return state

