from gemgem_2 import *
from stage_1 import *


def find_matching_gems(board):
    gems_to_remove = []

    for col in range(BOARDWIDTH):
        for row in range(BOARDHEIGHT):
            if get_gem_at(board, col, row) == get_gem_at(board, col + 1, row) == get_gem_at(board, col + 2, row):
                target_gem = board[col][row]
                offset = 0
                remove_set = []
                while get_gem_at(board, col + offset, row) == target_gem:
                    remove_set.append((col + offset, row))
                    offset += 1
                gems_to_remove.append(remove_set)

            if get_gem_at(board, col, row) == get_gem_at(board, col, row + 1) == get_gem_at(board, col, row + 2):
                target_gem = board[col][row]
                offset = 0
                remove_set = []
                while get_gem_at(board, col, row + offset) == target_gem:
                    remove_set.append((col, row + offset))
                    offset += 1
                gems_to_remove.append(remove_set)

    return gems_to_remove


