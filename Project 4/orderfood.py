class OrderFood:
    def __init__(self):
        self.menu = {
            'appetizer': {
                'Spring Rolls': 5.0,
                'Garlic Bread': 3.0,
                'French Fries': 2.5,
                'Corn Salad': 6.7,
            },
            'dessert': {
                'Ice Cream': 3.5,
                'Chocolate Cake': 4.0,
                'Fruit Salad': 3.0,
            },
            'cold drinks': {
                'Coke': 2.0,
                'Sprite': 2.0,
                'Fanta': 2.0,
                'Chocolate frappichino': 15.5,
            }
        }
        self.order = []  # List to store the ordered items
        self.total_payment = 0.0  # Total amount to be paid

    def display_menu(self):
        print("\nWelcome to the Hotel Management System!")
        for category, items in self.menu.items():
            print(f"\n{category.capitalize()}:")
            for item, price in items.items():
                print(f" - {item}: ${price:.2f}")

    def take_order(self):
        while True:
            category = input("\nEnter the category {appetizer, dessert, cold drinks} or 'done': ").lower()
            if category == 'done':
                break
            if category in self.menu:
                print(f"\nYou selected {category.capitalize()}.")
                item_list = list(self.menu[category].items())
                for i in range(len(item_list)):
                    item, price = item_list[i]
                    print(f"{i + 1}. {item} - ${price:.3f}")
                try:
                    item_choice = int(input(f"\nEnter the number of the item you want to order from {category.capitalize()}: "))
                    selected_item = item_list[item_choice - 1][0]
                    self.order.append((selected_item, self.menu[category][selected_item]))
                    self.total_payment += self.menu[category][selected_item]
                    print(f"{selected_item} has been added to your order!")
                except (ValueError, IndexError):
                    print("\nInvalid choice. Please select a valid item number.")
            else:
                print("\nInvalid category. Please choose from appetizer, dessert, or cold drinks.")

    def remove_order_item(self):
        if self.order:
            print("\nCurrent Order:")
            for i in range(len(self.order)):
                item, price = self.order[i]
                print(f"{i + 1}. {item} - ${price:.2f}")
            try:
                item_to_remove = int(input("\nEnter the number of the item you want to remove from your order: "))
                removed_item, removed_price = self.order.pop(item_to_remove - 1)
                self.total_payment -= removed_price
                print(f"{removed_item} has been removed from your order!")
            except (ValueError, IndexError):
                print("\nInvalid choice. Please select a valid item number.")
        else:
            print("\nNo items in the order to remove.")

    def show_receipt(self):
        if self.order:
            print("\n--- Receipt ---")
            for item, price in self.order:
                print(f"{item}: ${price:.2f}")
            print(f"\nTotal Payment: ${self.total_payment:.2f}")
        else:
            print("\nNo items ordered.")

    def main(self):
        while True:
            self.display_menu()
            self.take_order()
            self.show_receipt()
            remove_item = input("\nWould you like to remove an item? (y/n): ").lower()
            if remove_item == 'y':
                self.remove_order_item()
                self.show_receipt()
            another_order = input("\nWould you like to make another order or anything else? (y/n): ").lower()
            if another_order == 'n':
                print("Thank You Sir!")
                break

order_food = OrderFood()
order_food.main()