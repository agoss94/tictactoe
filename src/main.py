from src.constants import EMPTY, LABELS
from src.game import Game

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
    game = Game()
    while not game.game_over():
        print(game.board)
        game.turn()
    else:
        print(game.board)

    if game.board.winner() != EMPTY:
        print(f"Congrats the player {LABELS[game.board.winner()]} won the game!")
    else:
        print("The game ended in a draw!")

if __name__ == "__main__":
    run()
