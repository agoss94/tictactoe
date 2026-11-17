import pytest

from src.board import Board
from src.constants import CIRCLE, CROSS, EMPTY
from src.errors import InvalidStateError
from src.game import Game


class FixedMovePlayer:
    def __init__(self, index, symbol):
        self.index = index
        self.symbol = symbol
        self.boards_seen = []

    def move(self, board):
        self.boards_seen.append(board)
        return board.set(self.index, self.symbol)


def test_new_game_starts_with_an_empty_board_and_cross_to_move():
    game = Game()

    assert game.board.board == (EMPTY,) * 9
    assert game.current_player == CROSS
    assert game.players[CROSS].symbol == CROSS
    assert game.players[CIRCLE].symbol == CIRCLE


def test_turn_uses_each_player_in_order_and_updates_the_board():
    player_x = FixedMovePlayer(0, CROSS)
    player_o = FixedMovePlayer(4, CIRCLE)
    game = Game(player_x, player_o)

    game.turn()
    first_board = game.board
    assert first_board.board[0] == CROSS
    assert game.current_player == CIRCLE

    game.turn()
    assert game.board.board[0] == CROSS
    assert game.board.board[4] == CIRCLE
    assert game.current_player == CROSS
    assert player_x.boards_seen[0].board == (EMPTY,) * 9
    assert player_o.boards_seen == [first_board]


@pytest.mark.parametrize(
    "cells",
    [
        (CROSS, CROSS, CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY),
        (CROSS, CIRCLE, CROSS, CROSS, CIRCLE, CIRCLE, CIRCLE, CROSS, CROSS),
    ],
)
def test_turn_rejects_a_finished_game(cells):
    player = FixedMovePlayer(3, CROSS)
    game = Game(player, FixedMovePlayer(4, CIRCLE))
    game.board = Board(cells)

    with pytest.raises(InvalidStateError):
        game.turn()

    assert player.boards_seen == []
