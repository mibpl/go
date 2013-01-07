class Move(object):
    def validate(self, game_state):
        """
        Returns true iff this is a valid move for a given game state.
        """
        pass

    def make(self, game_state):
        """
        Applies this move to game_state. Assumes this is a valid move.
        """
        pass

    def validate_and_make(self, game_state):
        if not self.validate(game_state):
            return False
        else:
            self.make(game_state)
            return True
