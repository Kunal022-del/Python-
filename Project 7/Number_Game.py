import random

class NumberGuessingGame:
    def __init__(self, filename):
        self.rand_number = random.randint(1, 100)
        self.user_guess = None
        self.guesses = 0
        self.filename = filename
        self.hiscore = self.get_hiscore()

    def get_hiscore(self):
        """Reads the high score from the file."""
        try:
            with open(self.filename, "r") as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return float("inf")  # Default to a high value if the file doesn't exist
        except ValueError:
            return float("inf")  # Default to a high value if the content is invalid

    def update_hiscore(self):
        """Updates the high score if the current attempt is better."""
        if self.guesses < self.hiscore:
            print("You have set a new high score!")
            with open(self.filename, "w") as file:
                file.write(str(self.guesses))
        else:
            if self.hiscore == float("inf"):
                print("There was no previous high score.")
            else:
                print(f"The high score remains {self.hiscore}.")

    def play_game(self):
        """Starts the number guessing game."""
        print("Welcome to the Number Guessing Game!")
        print("Try to guess the number between 1 and 100.")

        while self.user_guess != self.rand_number:
            try:
                self.user_guess = int(input("Enter your guess: "))
                self.guesses += 1

                if self.user_guess == self.rand_number:
                    print(
                        f"Congratulations! You guessed the correct number in {self.guesses} guesses."
                    )
                elif self.user_guess > self.rand_number:
                    print("Too high! Try again.")
                else:
                    print("Too low! Try again.")

            except ValueError:
                print("Invalid input! Please enter a valid number between 1 and 100.")

        self.update_hiscore()

if __name__ == "__main__":
    filename = r"C:\Users\Gateway\Desktop\Python Folder\Project 2\Score.txt"  
    game = NumberGuessingGame(filename)
    game.play_game()
