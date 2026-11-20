from src.board import Board

e = lambda board: Board(board.board)
r = Board.rotate
s = Board.reflect
r2 = lambda board: r(r(board))
r3 = lambda board: r(r2(board))
sr = lambda board: s(r(board))
sr2 = lambda board: s(r2(board))
sr3 = lambda board: s(r3(board))

D4 = {e, r, r2, r3, s, sr, sr2, sr3}

def orbit(board):
    return set(f(board) for f in D4)

def canonical(board):
    return min(orbit(board), key=lambda b: b.board)

def transformer(board1, board2):
    for f in D4:
        if f(board1) == board2:
            return f
    raise ValueError("Boards are not in the same orbit")
