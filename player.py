from errors import InvalidStateError

class Player:

    def __init__(self, symbol):
        self.symbol = symbol

    def move(self, board):
        while True:
            try:
                index = int(input(f"Choose an empty field {board.empty_fields()}: "))
                return board.set(index, self.symbol)
            except ValueError:
                print("Please enter a valid number")
                continue
            except InvalidStateError:
                print("Please choose an empty field")
                continue
            except IndexError:
                print("The number must be between 0-8")
