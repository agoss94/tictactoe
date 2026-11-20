from src.board import Board
from src.symmetry import e
from src.constants import CROSS

def all_positions(key = e):
    positions = {}
    def collect(board, symbol):
        next_positions = []
        if board.game_over():
            positions.setdefault(key(board), [])
            return
        for empty_field in board.empty_fields():
            next_position = board.set(empty_field, symbol)
            next_positions.append(next_position)
            collect(next_position, -1 * symbol)

        positions.setdefault(key(board), next_positions)

    collect(Board(), CROSS)
    return positions
