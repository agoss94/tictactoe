from src.board import Board
from src.constants import CIRCLE, CROSS, EMPTY
from src.player import Player


def test_move_places_the_players_symbol(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "4")
    board = Board()

    result = Player(CIRCLE).move(board)

    assert result.board[4] == CIRCLE
    assert board.board == (EMPTY,) * 9


def test_move_retries_after_invalid_input(monkeypatch, capsys):
    answers = iter(["text", "0", "-1", "9", "1"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    board = Board().set(0, CROSS)

    result = Player(CIRCLE).move(board)

    assert result.board[1] == CIRCLE
    assert result.board[0] == CROSS
    assert len(result.board) == 9
    output = capsys.readouterr().out
    assert "Please enter a valid number" in output
    assert "Please choose an empty field" in output
    assert output.count("The number must be between 0-8") == 2
