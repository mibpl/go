class BoardModel(object):

    TOKENS = ['empty', 'white', 'black']

    def __init__(self, size):
        self._size = size
        self._M = [["empty" for i in range(0, size)] for j in range(0, size)]

    def get_size(self):
        return self._size

    def set_token(self, row, column, token):
        assert token in BoardModel.TOKENS
        assert 0 <= row and row < self._size 
        assert 0 <= column and column < self._size
        self._M[row][column] = token

    def get_token(self, row, column):
        assert 0 <= row and row < self._size 
        assert 0 <= column and column < self._size
        return self._M[row][column]

    def __unicode__(self):
        return u'\n'.join([' '.join([f[0] for f in row]) for row in self._M])

    def __str__(self):
        return unicode(self).encode('utf-8')

def test():
    b = BoardModel(3)
    b.set_token(0, 0, "white")
    b.set_token(2, 2, "black")
    assert b.get_token(0, 0) == "white"
    assert b.get_token(1, 1) == "empty"
    assert b.get_token(2, 2) == "black"
