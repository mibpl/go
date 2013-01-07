class Move(object):

    def validate(self, game_history):
      pass

    def make(self, game_history):
      """
      First checks if `validate` was called; if not - throws.
      Returns GameState object - result of applying the move to the last state
      kept in game_history.
      """
      pass
