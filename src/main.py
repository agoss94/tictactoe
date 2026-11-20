from src.constants import CIRCLE
from src.constants import EMPTY, LABELS
from src.game import Game
from src.player import Player
from src.menace import Menace

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

    answer = input("Do you want to play against menace? [y, N]")
    if answer == "":
        game = Game()
    else:
        game = Game(player_o=Player(CIRCLE), player_x=Menace())

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
