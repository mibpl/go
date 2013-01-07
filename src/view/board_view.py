import gtk
import gtk.gdk
import cairo
import math

class BoardView(gtk.DrawingArea):

    def __init__(self, parent):
        super(BoardView, self).__init__()
        self.add_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.connect("expose-event", self.expose)
        self.connect("button-press-event", self.mousePress)
        self._board = None
        self._controller = None

    def set_board(self, board):
        #TODO: add some mutex
        self._board = board
        self.queue_draw()

    def set_controller(self, controller):
        self._controller = controller

    def mousePress(self, widget, event):
        if self._board is None:
            return

        width = self.allocation.width
        height = self.allocation.height
        size = min(width, height)
        n = self._board.get_size()
        column = int(math.floor(event.x / size * n))
        row = int(math.floor(event.y / size * n))

        print row, column
        if self._controller is not None:
            self._controller.click(row, column)

    def expose(self, widget, event):
        if self._board is None:
            return

        cr = widget.window.cairo_create()

        width = self.allocation.width
        height = self.allocation.height

        size = min(width, height)

        cr.set_source_rgb(0.95, 0.8, 0.5)
        cr.rectangle(0, 0, size, size)
        cr.fill()

        cr.set_source_rgb(0.1, 0.1, 0.1)

        n = self._board.get_size()
        for i in range(n):
            x = ((2 * i + 1) * size) / (2 * n)
            cr.move_to(0, x)
            cr.line_to(size, x)
            cr.stroke()
            cr.move_to(x, 0)
            cr.line_to(x, size)
            cr.stroke()

        r = 0.5 * size / n
        for row in range(n):
            for column in range(n):
                token = self._board.get_token(row, column)
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

