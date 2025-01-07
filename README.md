# Python Projects Collection

Welcome to my collection of Python projects! These projects cover a variety of interactive applications, ranging from games to utilities, and more. Feel free to explore, try them out, and adapt them to your needs.

## Table of Contents

1. [Rock, Paper, Scissors Game](https://github.com/Kunal022-del/Python-/tree/main/Project%201)  
2. [Central Library Management System](https://github.com/Kunal022-del/Python-/tree/main/Project%203)  
3. [OrderFood System](https://github.com/Kunal022-del/Python-/tree/main/Project%204)  
4. [Simple Calculator using Tkinter](https://github.com/Kunal022-del/Python-/tree/main/Project%205%20)  
5. [Password Generator Application](https://github.com/Kunal022-del/Python-/tree/main/Project%206)  
6. [Currency Converter](https://github.com/Kunal022-del/Python-/tree/main/Project%202)

---
### Rock, Paper, Scissors Game

This is a simple Python implementation of the classic "Rock, Paper, Scissors" game, where you play against the computer.

## Features

- Randomized computer choices for fairness.
- Input validation to ensure proper gameplay.
- A clear and easy-to-read output to determine the winner.

## How to Run

1. Make sure you have Python installed on your system.
2. Copy the script into a file, e.g., `rock_paper_scissors.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is located.
5. Run the game with the command:
   ```bash
   python rock_paper_scissors.py
   ```

## Gameplay Instructions

- When prompted, type:
  - `r` for Rock
  - `p` for Paper
  - `s` for Scissors
- The computer will also make a choice.
- The game will announce the winner based on the following rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- If both players choose the same item, the game is a tie.

## Example Interaction

```
Comp Turn: Rock(r), Paper(p) or Scissors(s)
Your Turn: Rock(r), Paper(p) or Scissors(s)? r
Computer chose: Paper
You chose: Rock
You Lose!
```
---
# Central Library Management System

This Python script implements a simple Library Management System where users (students) can borrow and return books from the library.

## Features

- Displays the list of available books.
- Allows students to request a book to borrow.
- Allows students to return a borrowed book.
- Prevents borrowing books that are not available.
- Simple and interactive user interface.

## How to Run

1. Make sure you have Python installed on your system.
2. Copy the script into a file, e.g., `library_management.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is located.
5. Run the program with the command:
   ```bash
   python library_management.py
   ```

## Usage Instructions

1. **List all the Books**: Displays all books currently available in the library.
2. **Request a Book**: Borrow a book by entering its name when prompted. If the book is not available, the system will inform you.
3. **Add/Return a Book**: Return a previously borrowed book by entering its name.
4. **Exit the Library**: Exit the system.

## Example Interaction

```
----- Welcome to Central Library -----
    Please choose an option:
    1. List all the Books
    2. Request a Book
    3. Add/Return a Book
    4. Exit the Library

Enter a choice: 1

Books present in this library are:
1. Algorithms
2. Django
3. Clrs
4. Node js
5. PHP
6. Python
7. C++ Sharp

Enter a choice: 2
Enter the name of the Book you want to borrow: Django
You have been issued Django. Please keep it safe and return it within 15 days

Enter a choice: 1

Books present in this library are:
1. Algorithms
2. Clrs
3. Node js
4. PHP
5. Python
6. C++ Sharp

Enter a choice: 3
Enter the name of the Book you want to return: Django
Thanks for returning this Book! Hope you enjoyed reading it.

Enter a choice: 4
Thanks for choosing Central Library. Have a great day ahead!

```
----

# OrderFood System

## Overview

OrderFood is a Python-based restaurant management system designed to enhance the ordering experience. It features a menu with categories for appetizers, desserts, and cold drinks, allowing users to view options, place orders, manage items, and receive a detailed receipt.

The system is interactive, intuitive, and user-friendly, making it an excellent solution for small-scale restaurant operations or learning projects.

## Features

- **Menu Display**: Showcases a categorized menu with item names and prices.
- **Order Placement**: Allows users to select items from different categories to create an order.
- **Order Management**: Enables users to remove items from their order.
- **Receipt Generation**: Provides a summary of the order, including items and total payment.
- **Interactive Interface**: Continuous prompts ensure an engaging experience.

---

## Installation

1. Ensure Python 3.6 or above is installed on your system.
2. Download or copy the `OrderFood` script to your local machine.

---

## How to Use

1. Run the program using the command:
   ```bash
   python order_food.py
   ```
2. Follow the prompts:
   - View the menu categories.
   - Select items by entering the corresponding number.
   - Manage your order by adding or removing items.
   - View the receipt and confirm payment.

## Code Description

### Key Components:
1. **Menu Initialization**:
   - The menu is organized into categories with items and their prices.

2. **Order Management**:
   - Users can add or remove items from their order dynamically.

3. **Receipt Display**:
   - Summarizes the order with itemized costs and the total payment.

4. **Main Flow**:
   - Repeatedly prompts the user to interact with the system until the process is completed.

---

## Example Output
Welcome to the Hotel Management System!

Appetizers:
 - Spring Rolls: $5.00
 - Garlic Bread: $3.00

Desserts:
 - Ice Cream: $3.50
 - Chocolate Cake: $4.00

Cold Drinks:
 - Coke: $2.00
 - Sprite: $2.00

Enter the category {appetizer, dessert, cold drinks} or 'done': appetizer

1. Spring Rolls - $5.000
2. Garlic Bread - $3.000

Enter the number of the item you want to order from Appetizer: 1
Spring Rolls has been added to your order!

--- Receipt ---<br>
Spring Rolls: $5.00 </br>
Total Payment: $5.00

---

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

# Password Generator Application

The Password Generator application is a Python-based desktop tool built using the `tkinter` library. It allows users to generate strong passwords for specific websites and save them for future use. The application ensures user convenience and security by checking for duplicate entries.

---

## Features
- **Generate Passwords:** Create strong passwords of customizable lengths.
- **Save Passwords:** Store generated passwords along with the associated website and user name.
- **Duplicate Check:** Avoid saving passwords for the same website and user multiple times.

---

## How to Run
1. Ensure you have Python installed on your system.
2. Save the script to a file (e.g., `password.py`).
3. Run the script using the command:
   ```
   python password.py
   ```

---

## Sample Output

### 1. Generating a Password
**Input:**
- **Site:** example.com
- **User Name:** Kunal Kundaliya   
- **Password Length:** 12  

**Output:**  
A message box displays:  
```
Generated Password for Kunal Kundaliya at example.com: A$3kLd&7@wT9
```

### 2. Saving a Password
**Input:**
- **Site:** example.com  
- **User Name:** Kunal Kundaliya
- **Generated Password:** A$3kLd&7@wT9  

**Output:**  
A message box displays:  
```
Password saved successfully.
```

**File Content (`password_1.txt`):**  
``` bash
User: Kunal Kundaliya 
Site: example.com
Password: A$3kLd&7@wT9
```

### 3. Duplicate Password Check
**Input:**  
- **Site:** example.com  
- **User Name:** Kunal Kundaliya  

**Output:**  
A message box displays:  
```
Error: Password for this site and user already exists.
```

---

## File Structure
- **password.py**: Main script for the application.
- **password_1.txt**: File where passwords are stored or by setting new filename by changing <strong>`<script filename>`</strong>

---
# Currency Converter

A simple currency converter application built using Python and the Tkinter library. This application allows users to convert an amount from one currency to another based on predefined exchange rates. Additionally, it includes a light/dark mode toggle for enhanced usability.

---

## Features
- Converts currency between multiple supported currencies.
- Predefined exchange rates for quick and offline conversions.
- User-friendly interface with dropdowns for currency selection.
- Input validation with error messages for incorrect inputs.
- Light and dark mode toggling for better user experience.

---

## Prerequisites
Ensure you have Python 3.x installed on your system.

---

## How to Run
1. Clone or download this repository to your local system.
2. Save the script file (`currency_converter.py`) in a desired directory.
3. Open your terminal or command prompt and navigate to the directory where the script is saved.
4. Run the script using the command:
   ```bash
   python currency_converter.py
   ```
5. The application window will appear, ready for use.

---

## Usage
1. Enter the amount to be converted in the "Enter the amount" field.
2. Select the source currency ("From Currency") from the dropdown menu.
3. Select the target currency ("To Currency") from the dropdown menu.
4. Click the "Convert" button to perform the conversion.
5. The result will be displayed below the button.
6. Use the "Switch to Black Theme" or "Switch to White Theme" button to toggle between light and dark themes.

---

## Supported Currencies
- USD (US Dollar)
- EUR (Euro)
- JPY (Japanese Yen)
- GBP (British Pound)
- AUD (Australian Dollar)
- CAD (Canadian Dollar)
- CHF (Swiss Franc)
- CNY (Chinese Yuan)
- SEK (Swedish Krona)
- NZD (New Zealand Dollar)
- INR (Indian Rupee)
- NPR (Nepalese Rupee)
- KRW (South Korean Won)
- SGD (Singapore Dollar)
- MXN (Mexican Peso)
- BRL (Brazilian Real)

---

## File Structure
```batch
currency_converter.py
README.md 
```

---

## Error Handling
- Displays an error message if the amount entered is invalid or negative.
- Prompts the user if invalid currency codes are selected.

---

## Output
### Example 1: Converting USD to EUR
- Input:
  - Amount: 100
  - From Currency: USD
  - To Currency: EUR
- Output:
  ```
  The converted amount is: 93.00 EUR
  ```

### Example 2: Invalid Amount
- Input:
  - Amount: -50
  - From Currency: USD
  - To Currency: INR
- Output:
  ```
  Error: Amount must be greater than zero.
  ```

### Example 3: Unsupported Currency
- Input:
  - Amount: 100
  - From Currency: XYZ
  - To Currency: USD
- Output:
  ```
  Error: Invalid currency code. Please select valid currencies.
  ```

---
## File Structure
```
/rock_paper_scissors.py
/library.py
/order_food.py
/calculator.py
/password.py
/currency_converter.py
```

---

## Error Handling
- **Invalid Inputs**: All projects handle incorrect inputs with user-friendly error messages.
- **Validation**: Each app ensures inputs are correct (e.g., valid numbers, correct currency codes).
- **Error Messages**: In cases like division by zero or invalid currency codes, clear error messages will be shown.

---

## Contact
For any questions or feedback, please reach out to:
**Email**: Kunalsep22@gmail.com
**Number**:XXXXXXX


