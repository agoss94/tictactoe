from src.board import Board

def _chain(*transformers):
    def chained(board):
        for transformer in transformers:
            board = transformer(board)
        return board
    return chained

e = lambda board: Board(board.board)
r = Board.rotate
r2 = _chain(r, r)
r3 = _chain(r, r2)
s = Board.reflect
sr = _chain(r, s)
sr2 = _chain(r2, s)
sr3 = _chain(r3, s)

D4 = (e, r, r2, r3, s, sr, sr2, sr3)

def transform(board1, board2):
    for f in D4:
        if f(board1.board) == board2.board:
            return f
    raise ValueError("The given boards are not inside an orbit")

def orbit(board):
    return (f(board) for f in D4)

def canonical(board):
    return min(orbit(board), key=lambda b : b.board)