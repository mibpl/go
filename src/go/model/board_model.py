# coding=utf-8
from copy import deepcopy

class BoardModel(object):

    TOKENS = ['empty', 'white', 'black']

    @staticmethod
    def from_string(board_string):
        rows = board_string.split('\n')
        board = BoardModel(len(rows))
        for (i, row) in enumerate(rows):
            for (j, field) in enumerate(row.split()):
                for token in BoardModel.TOKENS:
                    if token[0] == field:
                        board.set_token(i, j, token)
        return board

    def __init__(self, size):
        self._size = size
        self._M = [['empty' for i in range(0, size)] for j in range(0, size)]

    def get_size(self):
        return self._size

    def on_board(self, row, column):
        return (0 <= row < self._size
                and 0 <= column < self._size)

    def set_token(self, row, column, token):
        assert token in BoardModel.TOKENS
        assert self.on_board(row, column)
        self._M[row][column] = token

    def get_token(self, row, column):
        assert self.on_board(row, column)
        return self._M[row][column]

    def get_neighbours(self, row, column):
        assert self.on_board(row, column)
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            r, c = row + dr, column + dc
            if self.on_board(r, c):
                yield r, c

    def get_group(self, row, column):
        """Returns group of fields of the same color which occupy given field.

        Additionally, returns tuple of types of fields which are neighbours for
        this group.

        >>> BoardModel.from_string("b w e\\nb w e\\ne b w").get_group(0, 0)
        ([(0, 0), (1, 0)], ('empty', 'white'))
        """
        assert self.on_board(row, column)
        token = self.get_token(row, column)
        queue = [(row, column)]
        visited = set(queue)
        group = set(queue)
        neighbours = set()
        while queue:
            r, c = queue[0]
            queue.pop(0)
            for nr, nc in self.get_neighbours(r, c):
                if not (nr, nc) in visited:
                    tok = self.get_token(nr, nc)
                    if tok == token:
                        group.add((nr, nc))
                        queue.append((nr, nc))
                    else:
                        neighbours.add(tok)
                    visited.add((nr, nc))
        return sorted(group), tuple(sorted(neighbours))

    def is_dead(self, row, column):
        """Checks if stone lying on a given field is dead.

        If the field is empty, returns False."""
        assert self.on_board(row, column)
        token = self.get_token(row, column)
        if token == "empty":
            return False
        _, neighbours = self.get_group(row, column)
        return len(neighbours) == 1

    def remove_group(self, row, column):
        """Removes group of stones to which stone at (row, column) belongs.

        Returns number of removed stones (0 if the field was empty)."""
        if self.get_token(row, column) == "empty":
            return 0
        group, _ = self.get_group(row, column)
        for r, c in group:
            self.set_token(r, c, "empty")
        return len(group)

    def __unicode__(self):
        return u"\n".join([" ".join([f[0] for f in row]) for row in self._M])

    def __str__(self):
        return unicode(self).encode("utf-8")
