from src.constants import CROSS
from src.board import Board
from src.symmetry import e, canonical

def all_positions(key_function = e):
    positions = {}
    def collect(board, symbol):
        next_moves = []
        if board.game_over():
            if key_function(board) == board:
                positions[board] = next_moves
            return
        for empty_field in board.empty_fields():
            next_board = board.set(empty_field, symbol)
            next_moves.append(next_board)
            collect(next_board, -1 * symbol)
        if key_function(board) == board:
            positions[board] = next_moves
    collect(Board(), CROSS)
    return positions