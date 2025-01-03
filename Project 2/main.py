import random
class Project:
    def __init__(self):
        self.randNumber = random.randint(1,100)
        self.userGuess = None
        self.guesses = 0
        self.hiscore = self.get_hiscore()
        self.filename = "score.txt"
    def get_hiscore(self):
        try:
            with open(self.filename, "r") as f:
                return int(f.read())
        except FileNotFoundError:
            return "File not found"

    def update_hiscore(self):
        if self.guesses < self.hiscore:
            print("You have just broken the high score!")
            with open(self.filename, "w") as f:
                f.write(str(self.guesses))
        else:
            print(f"The high score is still {self.hiscore}.")

    def play_game(self):
        while self.userGuess != self.randNumber:
            try:
                self.userGuess = int(input("Enter your guess (between 1 and 100): "))
                self.guesses += 1
                if self.userGuess == self.randNumber:
                    print("You guessed it right!")
                else:
                    if self.userGuess > self.randNumber:
                        print("You guessed it wrong! Enter a smaller number.")
                    else:
                        print("You guessed it wrong! Enter a larger number.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        print(f"You guessed the number in {self.guesses} guesses.")
        self.update_hiscore()

    def guess(self):
        return self.guesses

    def highscore(self):
        return self.hiscore

    def rand(self):
        return self.randNumber


p = Project()
p.play_game()
print(p.guess())
print(p.highscore())
print(p.rand())
