from src.positions import all_positions
from src.symmetry import canonical


def test_all_position():
    positions = all_positions()
    assert 5478 == len(positions)

def test_all_positions_symmetries():
    positions = all_positions(key=canonical)
    assert 765 == len(positions)