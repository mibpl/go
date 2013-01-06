class GameHistory(object):

  def __init__(self):
    self._turns = 0

  def get_turns(self):
    return self._turns

  def get_state_after_turn(self, turn):
    assert 0 <= turn and turn <= self._turns
    return None

