from src.constants import CIRCLE
from src.constants import EMPTY, LABELS
from src.game import Game
from src.player import Player
from src.menace import Menace


def ask_play_against_menace():
    while True:
        answer = input("Play against MENACE? [y] Yes / [n] No (default): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("", "n", "no"):
            return False
        print("Please enter y or n.")


def run():
    print("Welcome to:")
    print("""
▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄      ▄▄▄▄             ▄▄▄▄▄▄▄▄     ▄▄        ▄▄▄▄             ▄▄▄▄▄▄▄▄    ▄▄▄▄    ▄▄▄▄▄▄▄▄ 
▀▀▀██▀▀▀   ▀▀██▀▀    ██▀▀▀▀█            ▀▀▀██▀▀▀    ████     ██▀▀▀▀█            ▀▀▀██▀▀▀   ██▀▀██   ██▀▀▀▀▀▀ 
   ██        ██     ██▀                    ██       ████    ██▀                    ██     ██    ██  ██       
   ██        ██     ██                     ██      ██  ██   ██                     ██     ██    ██  ███████  
   ██        ██     ██▄        █████       ██      ██████   ██▄        █████       ██     ██    ██  ██       
   ██      ▄▄██▄▄    ██▄▄▄▄█               ██     ▄██  ██▄   ██▄▄▄▄█               ██      ██▄▄██   ██▄▄▄▄▄▄ 
   ▀▀      ▀▀▀▀▀▀      ▀▀▀▀                ▀▀     ▀▀    ▀▀     ▀▀▀▀                ▀▀       ▀▀▀▀    ▀▀▀▀▀▀▀▀ 
    """)

    if ask_play_against_menace():
        game = Game(player_o=Player(CIRCLE), player_x=Menace())
    else:
        game = Game()

    while not game.game_over():
        print(game.board)
        game.turn()
    else:
        winner = game.board.winner()
        for player in game.players.values():
            player.learn(winner)
        print(game.board)

    if game.board.winner() != EMPTY:
        print(f"Congrats the player {LABELS[game.board.winner()]} won the game!")
    else:
        print("The game ended in a draw!")

if __name__ == "__main__":
    run()
