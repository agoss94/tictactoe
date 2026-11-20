from src.constants import CROSS
from src.board import Board

def all_positions():
    positions = {}
    def collect(board, symbol):
        next_moves = []
        if board.game_over():
            positions[board] = next_moves
            return
        for empty_field in board.empty_fields():
            next_board = board.set(empty_field, symbol)
            next_moves.append(next_board)
            collect(next_board, -1 * symbol)
        positions[board] = next_moves
    collect(Board(), CROSS)
    return positions