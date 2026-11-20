from src.constants import CROSS
from src.positions import all_positions
from src.symmetry import canonical, transformer
import random


class Menace:

    def __init__(self, symbol=CROSS):
        self.state_space = all_positions(canonical)
        self.history = []
        self.symbol = symbol
        for next_moves in self.state_space.values():
            for move in next_moves:
                move.weight = 3

    def move(self, board):
        canonical_board = canonical(board)
        f = transformer(canonical_board, board)
        next_moves = self.state_space[canonical_board]
        result = random.choices(next_moves, [board.weight for board in next_moves], k=1)[0]
        self.history.append(result)
        return f(result)

    def learn(self, winner):
        if winner == self.symbol:
            adjustment = 3
        elif winner == 0:
            adjustment = 1
        else:
            adjustment = -1
        for move in self.history:
            move.weight = max(1, move.weight + adjustment)
        self.history.clear()


