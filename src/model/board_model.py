class BoardModel(object):

    def __init__(self, size):
        self._size = size

    def get_size(self):
        return self._size

    def get_token(self, row, column):
        assert 0 <= row and row < self._size 
        assert 0 <= column and column <= self._size
        return None

