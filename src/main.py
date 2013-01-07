#!/usr/bin/python
# -*- coding: utf-8 -*-

import gtk
import cairo

from model.board_model import BoardModel
from view.board_view import BoardView
from model.player import Player
from model.game import Game

class MainWindow(gtk.Window):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.set_title("Go")
        self.set_size_request(400, 300)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)

        model = BoardModel(19)
        view = BoardView(self)
        view.board = model

        self.add(view)
        self.show_all()

	player1 = Player()
	player2 = Player()
	game = Game(player1, player2)
	game.start()

if __name__ == "__main__":
    MainWindow()
    gtk.main()

