from gemgem_3 import *
from stage_2 import *


def check_patterns(board, row, col, patterns):
    for pattern in patterns:
        # check each possible pattern of "match in next move" to
        # see if a possible move can be made.
        if (get_gem_at(board, row + pattern[0][0], col + pattern[0][1]) ==
                get_gem_at(board, row + pattern[1][0], col + pattern[1][1]) ==
                get_gem_at(board, row + pattern[2][0], col + pattern[2][1]) is not None):
            return True  # return True the first time you find a pattern
    return False


def can_make_move(board):
    patterns = (((0, 1), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 0)),
                ((0, 1), (1, 0), (2, 1)),
                ((0, 0), (1, 0), (2, 1)),
                ((0, 0), (1, 1), (2, 1)),
                ((0, 0), (0, 2), (0, 3)),
                ((0, 0), (0, 1), (0, 3)),
                ((1, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (0, 2)),
                ((0, 0), (1, 1), (0, 2)),
                ((1, 0), (0, 1), (1, 2)),
                ((0, 0), (0, 1), (1, 2)),
                ((0, 0), (1, 1), (1, 2)),
                ((0, 0), (2, 0), (3, 0)),
                ((0, 0), (1, 0), (3, 0)))

    for row in range(BOARDWIDTH):
        for col in range(BOARDHEIGHT):
            if check_patterns(board, row, col, patterns):
                return True
    return False
