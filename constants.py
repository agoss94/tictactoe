# Constants for player and symbols
EMPTY, CROSS, CIRCLE = 0, 1, -1

# Labels for pretty printing
LABELS = {EMPTY: " ", CROSS: "X", CIRCLE: "O"}

# All Winning lines on a 9-element tuple model for a board
WINNING_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)