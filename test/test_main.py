from src.main import run


def test_run_completes_with_cross_winning(monkeypatch, capsys):
    moves = [0, 3, 1, 4, 2]
    answers = iter(map(str, moves))
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    run()

    output = capsys.readouterr().out
    assert "Welcome to:" in output
    assert "Congrats the player X won the game!" in output


def test_run_completes_with_a_draw(monkeypatch, capsys):
    moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]
    answers = iter(map(str, moves))
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    run()

    output = capsys.readouterr().out
    assert "Welcome to:" in output
    assert "The game ended in a draw!" in output
