# coding=utf-8

class AreaScoring(object):
    """Scoring according to the rules in:
    http://en.wikipedia.org/wiki/Rules_of_Go#Area_scoring
    """

    def __init__(self, komi=5.5):
        self._komi = komi

    def score(self, game_state):
        scores = {
                "black": 0,
                "white": 0.5 if game_state.handicaps_placed > 0 else self._komi
                }
        visited = set()
        board = game_state.board
        n = board.get_size()
        for row in range(n):
            for column in range(n):
                if (row, column) in visited:
                    continue
                visited.add((row, column))
                token = board.get_token(row, column)
                if token == 'empty':
                    group, neighbours = board.get_group(row, column)
                    for field in group:
                        visited.add(field)
                    if len(neighbours) == 1:
                        scores[neighbours[0]] += len(group)
                else:
                    scores[token] += 1
        return scores


