from positions import all_positions
from symmetry import canonical, orbit


class Menace:

    def __init__(self, symbol):
        self.symbol = symbol
        self.state = all_positions(key=canonical)
        for position in self.state:
            for next_position in self.state[position]:
                next_position.weight = 3

