
Simple Calculator in Python using Tkinter
This is a simple calculator application built with Python's Tkinter library. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division. Additionally, it includes features like handling parentheses and decimal points. Error handling is implemented to ensure that invalid operations, such as division by zero, are properly addressed with error messages.

Features
Basic Arithmetic Operations: Supports addition (+), subtraction (-), multiplication (*), and division (/).
Clear Button: Clears the current input on the display.
Error Handling: Displays error messages for invalid inputs like division by zero or incorrect syntax.
Parentheses: Supports parentheses for complex expressions.
Decimal Support: Allows for decimal point entries.
Requirements
Python 3.x
Tkinter (comes pre-installed with Python in most distributions)
Installation
If you don't have Python installed, download it from the official website:
Python Downloads

Once Python is installed, Tkinter should already be available. If not, you can install it via the following command (on Linux-based systems):

bash
Copy code
sudo apt-get install python3-tk
Usage
Clone or download the repository containing the Python script (calculator.py).
Run the script with Python:
bash
Copy code
python calculator.py
The calculator window will pop up, allowing you to perform arithmetic operations.

How It Works
GUI: The graphical user interface is built using the Tkinter library. The calculator consists of a display at the top and a grid of buttons representing digits, operators, and other functions.
Button Clicks: Each button is linked to a function that handles its action. The user input is appended to the result string and displayed on the screen.
Evaluation: When the "=" button is pressed, the expression is evaluated using Python's eval() function. Any errors (such as division by zero) are caught and displayed in a pop-up error box.
Clear Function: The "C" button resets the display.
Code Structure
Calculator Class
This class contains all the logic and widgets for the calculator:

__init__(self, root): Initializes the calculator window and sets up the UI.
create_widgets(self): Creates the display and buttons for the calculator.
on_button_click(self, char): Handles the logic when a button is clicked, updating the display and evaluating the expression.
calculator_main() Function
This function initializes the Tkinter main window and runs the calculator.

Example
Here is a sample input/output session:

makefile
Copy code
Input: 5 + 3 * (2 - 1)
Output: 8
Error Handling
ZeroDivisionError: If a division by zero occurs, an error message is shown, and the display turns red.
Other Errors: Any other errors (e.g., invalid syntax) will also display an error message.
Screenshots
Include screenshots of the calculator window here, if desired.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Tkinter documentation for building the GUI.
Python documentation for built-in libraries like eval() and messagebox.
