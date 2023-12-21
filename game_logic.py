import random
from decouple import config


class CasinoGame:
    def __init__(self):
        self.money = int(config("MY_MONEY", default=1000))
        self.slots = list(range(1, 31))

    def play(self):
        while True:
            print(f"Your current money: ${self.money}")
            bet = int(input("Place your bet on a slot (1-30): "))

            if bet not in self.slots:
                print("Invalid slot. Try again.")
                continue

            winning_slot = random.choice(self.slots)
            print(f"Winning slot is: {winning_slot}")

            if bet == winning_slot:
                print(f"You won! Your bet is doubled.")
                self.money += bet
            else:
                print("You lost! Your bet is taken.")
                self.money -= bet

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                break

        print(f"Game over. Your final money: ${self.money}")

