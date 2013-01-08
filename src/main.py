#!/usr/bin/python
# -*- coding: utf-8 -*-

import gtk
import cairo

from go.controller.controller import Controller
from go.model.board_model import BoardModel
from go.view.board_view import BoardView
from go.model.game_history import GameHistory

class MainWindow(gtk.Window):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.set_title("Go")
        self.set_size_request(400, 300)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)

        view = BoardView(self)
        game_history = GameHistory()
        controller = Controller(game_history)
        
        view.set_controller(controller)
        controller.set_view(view)

        self.add(view)
        self.show_all()


if __name__ == "__main__":
    MainWindow()
    gtk.main()

