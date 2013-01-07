from board_model import BoardModel

class GameState(object):
    def __init__(self):
        self._board = BoardModel(19)

    def get_board(self):
        return self._board

    def get_current_player(self):
        pass

    def get_stage(self):
        """
        It might be one of `stone placing` or `dead stones removing` stages.
        """
        pass

    def get_captives_count(self, player):
        pass

    def get_consecutive_passes(self):
        pass

# fields instead of getters?
