import gtk

class PlayerView():
    def __init__(self, widget, player):
        assert player in ("black", "white")

        vbox = gtk.VBox(True)
        widget.add(vbox)

        self.player = player
        player_label = gtk.Label("player %s" % player)
        vbox.add(player_label)

        self._captives_label = gtk.Label("test")
        vbox.add(self._captives_label)

    def set_game_state(self, game_state):
        self._captives_label.set_text("killed stones: %s" % game_state.captives_count[self.player]) 



