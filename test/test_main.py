import pytest

from src.main import ask_play_against_menace, run


def test_run_completes_with_cross_winning(monkeypatch, capsys):
    moves = [0, 3, 1, 4, 2]
    answers = iter(["n", *map(str, moves)])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    run()

    output = capsys.readouterr().out
    assert "Welcome to:" in output
    assert "Congrats the player X won the game!" in output


def test_run_completes_with_a_draw(monkeypatch, capsys):
    moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]
    answers = iter(["", *map(str, moves)])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    run()

    output = capsys.readouterr().out
    assert "Welcome to:" in output
    assert "The game ended in a draw!" in output


@pytest.mark.parametrize("answer", ["y", "Y", "yes", " YES "])
def test_menace_prompt_accepts_yes(monkeypatch, answer):
    monkeypatch.setattr("builtins.input", lambda prompt: answer)

    assert ask_play_against_menace()


@pytest.mark.parametrize("answer", ["", "n", "N", "no", " NO "])
def test_menace_prompt_accepts_no(monkeypatch, answer):
    monkeypatch.setattr("builtins.input", lambda prompt: answer)

    assert not ask_play_against_menace()


def test_menace_prompt_retries_invalid_answer(monkeypatch, capsys):
    answers = iter(["0", "maybe", "y"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    assert ask_play_against_menace()
    assert capsys.readouterr().out.count("Please enter y or n.") == 2
