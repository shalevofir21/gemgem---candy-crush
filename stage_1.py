from gemgem_1 import *


def get_gem_at(board, col, row):
    if row < 0 or col < 0 or row >= BOARDHEIGHT or col >= BOARDWIDTH:
        return None
    else:
        return board[col][row]
