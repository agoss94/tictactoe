from src.constants import EMPTY, CROSS, CIRCLE
from src.positions import all_positions
from src.symmetry import canonical
from src.board import Board

def test_all_positions_len():
    positions = all_positions()
    assert len(positions) == 5478

def test_next_moves():
    positions = all_positions()
    board = Board((
        EMPTY, CROSS, CIRCLE,
        CROSS, CROSS, CIRCLE,
        EMPTY, CIRCLE, CROSS
    ))
    next_moves = positions[board]
    assert set(next_moves) == { Board((
        CIRCLE, CROSS, CIRCLE,
        CROSS, CROSS, CIRCLE,
        EMPTY, CIRCLE, CROSS
    )), Board((
        EMPTY, CROSS, CIRCLE,
        CROSS, CROSS, CIRCLE,
        CIRCLE, CIRCLE, CROSS
    ))}

def test_all_positions_canonical():
    positions = all_positions(canonical)
    assert len(positions) == 765
