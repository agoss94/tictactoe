from constants import EMPTY, CROSS, CIRCLE, WINNING_LINES, LABELS
from errors import InvalidSymbolError, InvalidStateError

class Board:

    def __init__(self, board = (EMPTY,) * 9):
        self.board = board

    def winner(self):
        for a, b, c in WINNING_LINES:
            value = self.board[a]
            if value == self.board[b] ==self.board[c] and value != EMPTY:
                return value
        return 0

    def set(self, index, symbol):
        if symbol not in (CROSS, CIRCLE):
            raise InvalidSymbolError("Can only set CROSS or CIRCLE")
        if self.board[index] != EMPTY:
            raise InvalidStateError("Cannot set on a non-empty field")
        return Board(self.board[:index] + (symbol,) + self.board[index + 1:])

    def empty_fields(self):
        return set((index for index, value in enumerate(self.board) if value == EMPTY))

    def game_over(self):
        return self.winner() != EMPTY or self.empty_fields() == set()

    def __str__(self):
        p = self.board
        return f"""
         {LABELS[p[0]]} | {LABELS[p[1]]} | {LABELS[p[2]]} 
        ---+---+---
         {LABELS[p[3]]} | {LABELS[p[4]]} | {LABELS[p[5]]} 
        ---+---+---
         {LABELS[p[6]]} | {LABELS[p[7]]} | {LABELS[p[8]]} 
"""