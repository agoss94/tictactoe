from board import Board
from constants import EMPTY, CROSS, CIRCLE
from errors import InvalidStateError
from player import Player


class Game:

    def __init__(self, player_x=Player(CROSS), player_o=Player(CIRCLE)):
        self.board = Board()
        self.players = {CROSS: player_x, CIRCLE: player_o}
        self.current_player = CROSS

    def turn(self):
        if self.board.winner() != EMPTY:
            raise InvalidStateError("Cannot make a turn")
        player = self.players[self.current_player]
        self.board = player.move(self.board)
        self.current_player *= -1



