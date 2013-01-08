import gtk
import gtk.gdk
import cairo
import math

class BoardView():

    def __init__(self, parent):
        main_vbox = gtk.VBox(False)
        parent.add(main_vbox)
        
        main_hbox = gtk.HBox(False)
        right_panel = gtk.VBox(True)
        
        b1 = gtk.Button("menu")
        b2 = gtk.Button("b2")
        b4 = gtk.Button("b4")
        
        pass_button = gtk.Button("pass")
        pass_button.add_events(gtk.gdk.BUTTON_PRESS_MASK)
        pass_button.connect("button-press-event", self._do_pass)
        
        
        b5 = gtk.Button("b5")
        
        right_panel.pack_start(pass_button, False)
        right_panel.pack_start(b5, False)
        
        self._image = gtk.DrawingArea()
        main_hbox.pack_start(self._image, True)
        main_hbox.pack_start(right_panel, False)
        
        self._status_bar = gtk.Statusbar()
        self.display_message("Welcome to go")
        
        main_vbox.pack_start(b1, False)
        main_vbox.pack_start(main_hbox, True)
        main_vbox.pack_start(self._status_bar, False)
        
        self._image.add_events(gtk.gdk.EXPOSURE_MASK)
        self._image.connect("expose-event", self.expose)
        self._image.add_events(gtk.gdk.BUTTON_PRESS_MASK)
        self._image.connect("button-press-event", self.boardMousePress)
        self._game_state = None
        self._controller = None

    def set_controller(self, controller):
        self._controller = controller

    def set_game_state(self, game_state):
        #TODO: add some mutex?
        self._game_state = game_state
        self._image.queue_draw()

    def display_message(self, message):
        self._status_bar.push(self._status_bar.get_context_id("info"), message)
    
    def _do_pass(self, widget, event):
        print("pass")
        self._controller.do_pass()
    
    def _get_size(self):
        return min(self._image.allocation.width, self._image.allocation.height)
    

    def boardMousePress(self, widget, event):
        if self._game_state is None:
            return

        size = self._get_size()
        n = self._game_state.board.get_size()
        column = int(math.floor(event.x / size * n))
        row = int(math.floor(event.y / size * n))
        
        if row < n and column < n:
            print row, column
            if self._controller is not None:
                self._controller.click(row, column)

    def expose(self, widget, event):
        if self._game_state is None:
           return        
        
        size = self._get_size()
        board = self._game_state.board
        n = board.get_size()
        rect_size = size / float(n)
        
        cr = widget.window.cairo_create()
        cr.set_source_rgb(0.95, 0.8, 0.5)
        cr.rectangle(0, 0, size, size)
        cr.fill()

        cr.set_source_rgb(0.1, 0.1, 0.1)
        cr.set_line_width(rect_size / 20)
        
        
        for i in range(n):
            x = ((2 * i + 1) * size) / (2 * n)
            cr.move_to(rect_size / 2, x)
            cr.line_to(size - rect_size / 2, x)
            cr.stroke()
            cr.move_to(x, rect_size / 2)
            cr.line_to(x, size - rect_size / 2)
            cr.stroke()
        
        if n == 19:
            r = 0.2 * rect_size
            for i in range(3):
                for j in range(3):
                    cr.arc(
                        rect_size / 2 + 3 * rect_size + i * 6 * rect_size,
                        rect_size / 2 + 3 * rect_size + j * 6 * rect_size,
                        r,
                        0.0,
                        2 * math.pi
                    )
                    cr.fill()
                    
        r = 0.5 * rect_size
        for row in range(n):
            for column in range(n):
                token = board.get_token(row, column)
                if not token == 'empty':
                    if token == 'black':
                        cr.set_source_rgb(0.0, 0.0, 0.0)
                    else:  # 'white'
                        cr.set_source_rgb(1.0, 1.0, 1.0)
                    cr.arc(
                        column * size / n + r,
                        row * size / n + r,
                        r, 0.0, 2 * math.pi)
                    cr.fill()
