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

--- Receipt ---
Spring Rolls: $5.00
Total Payment: $5.00
