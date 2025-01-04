# Simple Calculator in Python using Tkinter

This is a simple calculator application built with Python's Tkinter library. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division. Additionally, it includes features like handling parentheses and decimal points. Error handling is implemented to ensure that invalid operations, such as division by zero, are properly addressed with error messages.

## Features

- **Basic Arithmetic Operations**: Supports addition (+), subtraction (-), multiplication (*), and division (/).
- **Clear Button**: Clears the current input on the display.
- **Error Handling**: Displays error messages for invalid inputs like division by zero or incorrect syntax.
- **Parentheses**: Supports parentheses for complex expressions.
- **Decimal Support**: Allows for decimal point entries.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python in most distributions)

## Installation

If you don't have Python installed, download it from the official website:  
[Python Downloads](https://www.python.org/downloads/)

## How It Works

### GUI
The graphical user interface (GUI) is built using the Tkinter library. The calculator consists of:

- A display at the top where the current input or result is shown.
- A grid of buttons representing digits (0-9), operators (+, -, *, /), and other functions (clear, parentheses, percentage, decimal point, and equals).

### Button Clicks
Each button is linked to a function that handles its action. When a button is clicked:

- The corresponding character (digit, operator, or symbol) is appended to the `result` string.
- The `result` string is updated and displayed in the calculator's text field.

### Evaluation
When the "=" button is pressed:

- The input expression is evaluated using Python's built-in `eval()` function, which processes the mathematical expression.
- If the expression is valid, the result is displayed in the text field.
- If there are errors (such as division by zero or invalid syntax), an error message is shown in a pop-up dialog box, and the display turns red to highlight the error.

### Clear Function
The "C" button resets the display:

- When clicked, the current expression is cleared, and the display is reset to an empty state, allowing the user to input a new expression.

---
## Contact
For any questions or feedback, please reach out at 
```batch
[Kunalsep22@gmail.com].
```
