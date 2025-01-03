
import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="white")
        self.result = ""
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(
            self.root,
            textvariable=self.result_var,
            font=("Arial", 20),
            bd=10,
            relief="sunken",
            justify="right",
            bg="white",
            fg="black",
        )
        self.display.grid(row=0, column=0, columnspan=4)
        buttons = [
            ("1", 1, 0),
            ("2", 1, 1),
            ("3", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("7", 3, 0),
            ("8", 3, 1),
            ("9", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("+", 4, 2),
            ("=", 4, 3),
            ("C", 5, 0),
            ("(", 5, 1),
            (")", 5, 2),
            ("%", 5, 3)
        ]
        for text, row, col in buttons:
            tk.Button(
                self.root,
                text=text,
                font=("Arial", 20),
                width=5,
                height=2,
                command=lambda t=text: self.on_button_click(t),
                bg="chocolate",
                fg="white",
            ).grid(row=row, column=col)

    def on_button_click(self, char):
        if char == "=":
            try:
                self.result = str(eval(self.result))
                self.display.config(bg="white", fg="black")
            except ZeroDivisionError:
                self.result = "Error: Division by zero"
                self.display.config(bg="red", fg="white")
                messagebox.showerror("Error", "Cannot divide by zero.")
            except Exception as e:
                self.result = f"Error: {str(e)}"
                self.display.config(bg="red", fg="white")
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        elif char == "C":
            self.result = ""
            self.display.config(bg="white", fg="black")
        else:
            self.result += str(char)
            self.display.config(bg="white", fg="black")
        self.result_var.set(self.result)


def calculator_main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


calculator_main()
