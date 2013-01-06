class GameState(object):

  def get_board():
    """
    Returns BoardModel object.
    """
    pass

  def get_current_player():
    pass

  def get_stage():
    """
    It might be one of `stone placing` or `dead stones removing` stages.
    """
    pass

  def get_captives_count(self, player):
    pass

  def get_consecutive_passes():
    pass

# fields instead of getters?
