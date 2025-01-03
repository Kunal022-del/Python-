import random


class Game:
    def __init__(self):
        self.choices = ["r", "p", "s"]
        self.choice_names = {"r": "Rock", "p": "Paper", "s": "Scissors"}

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_user_choice(self):
        while True:
            choice = input("Your Turn: Rock(r), Paper(p) or Scissors(s)? ").lower()
            if choice in self.choices:
                return choice
            else:
                print("Invalid choice! Please choose 'r', 'p', or 's'.")

    def determine_winner(self, comp, you):
        if comp == you:
            return "tie"
        elif (
            (comp == "r" and you == "s")
            or (comp == "s" and you == "p")
            or (comp == "p" and you == "r")
        ):
            return "lose"
        else:
            return "win"

    def play_game(self):
        print("Comp Turn: Rock(r), Paper(p) or Scissors(s)")
        comp = self.get_computer_choice()
        you = self.get_user_choice()
        result = self.determine_winner(comp, you)
        print(f"Computer chose: {self.choice_names[comp]}")
        print(f"You chose: {self.choice_names[you]}")
        if result == "tie":
            print("The game is a tie!")
        elif result == "win":
            print("You Win!")
        else:
            print("You Lose!")


game = Game()
game.play_game()
