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

## Contact

For any questions or feedback, please reach out at
```batch
[Kunalsep22@gmail.com].
```

