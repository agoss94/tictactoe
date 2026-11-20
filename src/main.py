from src.constants import EMPTY, LABELS, CIRCLE, CROSS
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

def train_menace():
    while True:
        try:
            training_games = int(input("How many games should menace train? "))
            index = 0
            menace_x = Menace(CROSS)
            menace_o = Menace(CIRCLE)
            while index < training_games:
                game = Game(menace_x, menace_o)
                while not game.game_over():
                    game.turn()
                menace_o.learn(game.winner())
                menace_x.learn(game.winner())
                index += 1
            return menace_x
        except ValueError:
            print("Invalid number close program")



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
        menace = train_menace()
        game = Game(player_o=Player(CIRCLE), player_x=menace)
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
