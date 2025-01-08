# Number Guessing Game

This Python script implements a fun and interactive number guessing game. The objective is to guess a randomly generated number between 1 and 100 in as few attempts as possible. The program keeps track of your number of guesses and maintains a high score to challenge yourself or others.

## Features

- **Random Number Generation:** The computer generates a random number between 1 and 100.
- **Guess Tracking:** The program counts how many guesses you make to find the correct number.
- **High Score Management:** Keeps track of the lowest number of guesses required to win and saves it to a file.
- **Input Validation:** Ensures only valid numeric inputs within the range are accepted.
- **User Feedback:** Provides guidance if your guess is too high or too low.

## How to Run the Game

1. Ensure Python is installed on your computer.
2. Save the script to a file named `Number_game.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where the `Number_game.py` file is located.
5. Run the script using the command:

   ```bash
   python Number_game.py
   ```

## Gameplay Instructions

1. **Start the Game:** When the game begins, it will generate a random number between 1 and 100.
2. **Make a Guess:** Enter your guess when prompted.
3. **Receive Feedback:**
   - If your guess is too high, the program will ask you to try a smaller number.
   - If your guess is too low, it will prompt you to try a larger number.
4. **Win the Game:** Once you guess the correct number, the program will display your total number of guesses.
5. **High Score:** If you beat the current high score (i.e., guess the number in fewer attempts), the program will congratulate you and update the high score.

## Example Interaction

```
Welcome to the Number Guessing Game!
Try to guess the number between 1 and 100.
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Congratulations! You guessed the correct number in 3 guesses.
You have set a new high score!
```

## High Score Management

The program saves the high score to a file named `score.txt` in the same directory as the script. Ensure that this file is writable, or the program will create it automatically if it does not exist.

## Customization

You can customize the game by modifying the following:
- **Number Range:** Change the range of numbers by updating the random number generation logic in the script.
- **File Name:** Update the name of the high score file if desired.

## Troubleshooting

- If you encounter an error, ensure the `score.txt` file is accessible and not corrupted and not overwrited with some unethical contents.
- If the game does not start, check that Python is installed and the script is saved correctly.



## Conclusion

The Number Guessing Game is a simple yet engaging program to test your intuition and improve your guessing skills. Challenge your friends and family to see who can guess the number with the fewest attempts. Enjoy the game!