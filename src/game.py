from src.board import Board
from src.constants import CROSS, CIRCLE
from src.errors import InvalidStateError
from src.player import Player


class Game:

    def __init__(self, player_x=Player(CROSS), player_o=Player(CIRCLE)):
        self.board = Board()
        self.players = {CROSS: player_x, CIRCLE: player_o}
        self.current_player = CROSS

    def turn(self):
        if self.board.game_over():
            raise InvalidStateError("Cannot make a turn")
        player = self.players[self.current_player]
        self.board = player.move(self.board)
        self.current_player *= -1

    def game_over(self):
        return self.board.game_over()

    def winner(self):
        return self.board.winner()



