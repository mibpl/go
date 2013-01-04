import gtk
import cairo

class BoardView(gtk.DrawingArea):

    def __init__(self, parent):
        super(BoardView, self).__init__()
        self.connect("expose-event", self.expose)
        self.board = None

    def expose(self, widget, event):
        if self.board is None:
            return

        cr = widget.window.cairo_create()

        width = self.allocation.width
        height = self.allocation.height

        size = min(width, height)
        cr.translate((width - size) / 2, (height - size) / 2)
        
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

