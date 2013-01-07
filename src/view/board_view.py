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
        self.board = None
        self.stones = []

    def mousePress(self, widget, event):
        width = self.allocation.width
        height = self.allocation.height
        size = min(width, height)
        n = self.board.get_size()
        i = math.floor(event.x / size * n)
        j = math.floor(event.y / size * n)

        print(i, j)
        self.stones.append((i, j))
        self.queue_draw()

    def expose(self, widget, event):
        if self.board is None:
            return

        cr = widget.window.cairo_create()

        width = self.allocation.width
        height = self.allocation.height

        size = min(width, height)

        cr.set_source_rgb(0.95, 0.8, 0.5)
        cr.rectangle(0, 0, size, size)
        cr.fill()

        cr.set_source_rgb(0.1, 0.1, 0.1)

        n = self.board.get_size()
        for i in range(n):
            x = ((2 * i + 1) * size) / (2 * n)
            cr.move_to(0, x)
            cr.line_to(size, x)
            cr.stroke()
            cr.move_to(x, 0)
            cr.line_to(x, size)
            cr.stroke()

        r = 0.5 * size / n
        for i, j in self.stones:
            cr.arc(i / n * size + r, j / n * size + r, r, 0.0, 2 * math.pi)
            cr.fill()
