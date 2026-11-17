import pytest

from src.main import run


@pytest.mark.parametrize(
    ("moves", "ending"),
    [
        ([0, 3, 1, 4, 2], "Congrats the player X won the game!"),
        ([0, 1, 2, 4, 3, 5, 7, 6, 8], "The game ended in a draw!"),
    ],
)
def test_run_completes_a_game(monkeypatch, capsys, moves, ending):
    answers = iter(map(str, moves))
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    run()

    output = capsys.readouterr().out
    assert "Welcome to:" in output
    assert ending in output
