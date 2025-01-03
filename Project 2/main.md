# Number Guessing Game

This Python script implements a number guessing game where the user tries to guess a randomly generated number between 1 and 100. The program keeps track of the user's number of guesses and maintains a high score.

## Features

- Randomly generates a number between 1 and 100.
- Tracks the number of guesses made by the user.
- Updates and stores the high score in a file.
- Input validation ensures only valid numbers are accepted.

## How to Run

1. Make sure you have Python installed on your system.
2. Copy the script into a file, e.g., `main.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is located.
5. Run the game with the command:
   ```bash
   python main.py
   ```

## Gameplay Instructions

- The computer will randomly generate a number between 1 and 100.
- Enter your guess when prompted.
- The program will guide you by indicating whether your guess is too high or too low.
- Keep guessing until you find the correct number.
- Your score (number of guesses) will be compared with the current high score and updated if it is lower.

## Example Interaction

```
Enter your guess (between 1 and 100): 50
You guessed it wrong! Enter a smaller number.
Enter your guess (between 1 and 100): 25
You guessed it wrong! Enter a larger number.
```
