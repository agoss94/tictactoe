import pytest

from src.board import Board
from src.constants import EMPTY, CROSS, CIRCLE
from src.errors import InvalidStateError, InvalidSymbolError

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


def test_set_returns_a_new_board_without_changing_the_original():
    original = Board()

    changed = original.set(4, CIRCLE)

    assert original.board == (EMPTY,) * 9
    assert changed.board[4] == CIRCLE
    assert len(changed.board) == 9


@pytest.mark.parametrize("symbol", [EMPTY, 2, "X"])
def test_set_rejects_invalid_symbols(symbol):
    with pytest.raises(InvalidSymbolError):
        Board().set(0, symbol)


def test_set_rejects_occupied_field():
    board = Board().set(0, CROSS)

    with pytest.raises(InvalidStateError):
        board.set(0, CIRCLE)


@pytest.mark.parametrize("index", [-1, 9])
def test_set_rejects_out_of_range_fields(index):
    with pytest.raises(IndexError):
        Board().set(index, CROSS)


@pytest.mark.parametrize(
    ("cells", "expected"),
    [
        ((CROSS, CROSS, CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY), CROSS),
        ((CIRCLE, CROSS, EMPTY, CIRCLE, CROSS, EMPTY, CIRCLE, EMPTY, EMPTY), CIRCLE),
    ],
)
def test_winner_returns_the_winning_symbol(cells, expected):
    assert Board(cells).winner() == expected


def test_game_over_for_open_won_and_drawn_boards():
    open_board = Board()
    won_board = Board((CROSS, CROSS, CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY))
    drawn_board = Board((CROSS, CIRCLE, CROSS, CROSS, CIRCLE, CIRCLE, CIRCLE, CROSS, CROSS))

    assert not open_board.game_over()
    assert won_board.game_over()
    assert drawn_board.winner() == EMPTY
    assert drawn_board.game_over()
