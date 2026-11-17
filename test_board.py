from board import Board
from constants import EMPTY, CROSS, CIRCLE

def test_to_string_board():
    board = Board()
    expected = """
           |   |   
        ---+---+---
           |   |   
        ---+---+---
           |   |   
"""
    assert expected == board.__str__()

def test_to_string_board2():
    board = Board((
        0, 0, 1,
        1, -1, -1,
        0, 0, 1
    ))
    expected = """
           |   | X 
        ---+---+---
         X | O | O 
        ---+---+---
           |   | X 
"""
    assert expected == board.__str__()

def test_no_winner():
    board = Board((
        EMPTY, CROSS, CIRCLE,
        EMPTY, EMPTY, EMPTY,
        CIRCLE, CROSS, CROSS
    ))
    assert False == board.winner()

def test_winner_on_horizontal():
    board = Board((
        EMPTY, CROSS, CIRCLE,
        EMPTY, CIRCLE, EMPTY,
        CROSS, CROSS, CROSS
    ))
    assert board.winner()

def test_winner_on_vertical():
    board = Board((
        CIRCLE, CROSS, EMPTY,
        CIRCLE, EMPTY, EMPTY,
        CIRCLE, CROSS, CROSS
    ))
    assert board.winner()

def test_winner_on_diagonal():
    board = Board((
        EMPTY, CROSS, CIRCLE,
        EMPTY, CIRCLE, EMPTY,
        CIRCLE, CROSS, CROSS
    ))
    assert board.winner()

def test_set_symbol():
    board = Board((
        EMPTY, CROSS, CIRCLE,
        EMPTY, CIRCLE, EMPTY,
        CIRCLE, CROSS, CROSS
    ))
    new_board = board.set(0, CROSS)
    expected = (
        CROSS, CROSS, CIRCLE,
        EMPTY, CIRCLE, EMPTY,
        CIRCLE, CROSS, CROSS
    )
    assert expected == new_board.board


def test_empty_fields():
    board = Board((
        EMPTY, CROSS, CIRCLE,
        EMPTY, CIRCLE, EMPTY,
        CIRCLE, CROSS, CROSS
    ))
    expected = {0,3,5}
    assert expected == board.empty_fields()
