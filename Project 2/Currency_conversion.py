import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Currency conversion rates relative to 1 USD it could be modify
# According to converion from any currency and changing the money type 
cont_dic = {
    "USD": 1.0, "EUR": 0.93, "JPY": 110.35, "GBP": 0.77, "AUD": 1.35,
    "CAD": 1.32, "CHF": 0.91, "CNY": 6.95, "SEK": 9.02, "NZD": 1.45,
    "INR": 74.85, "NPR": 120.0, "KRW": 1180.0, "SGD": 1.36, "MXN": 20.0,
    "BRL": 5.25
}

def conversion(number, from_what, to_type):
    return number * cont_dic[to_type] / cont_dic[from_what]

def handle_conversion():
    try:
        number = float(amount_entry.get())
        from_what = from_currency.get()
        to_type = to_currency.get()
        if from_what not in cont_dic or to_type not in cont_dic:
            raise ValueError("Invalid currency code. Please select valid currencies.")
        if number <= 0:
            raise ValueError("Amount must be greater than zero.")
        converted_amount = conversion(number, from_what, to_type)
        result_label.config(text=f"The converted amount is: {converted_amount:.2f} {to_type}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Toggle Theme
def toggle_theme():
    global is_dark_mode
    if is_dark_mode:
        root.config(bg="white")
        header_frame.config(bg="lightgray")
        title_label.config(bg="lightgray", fg="black")
        content_frame.config(bg="white")
        result_label.config(bg="white", fg="black")
        toggle_button.config(text="Switch to Black Theme", bg="white", fg="black")
        is_dark_mode = False
    else:
        root.config(bg="black")
        header_frame.config(bg="darkgray")
        title_label.config(bg="darkgray", fg="white")
        content_frame.config(bg="black")
        result_label.config(bg="black", fg="white")
        toggle_button.config(text="Switch to White Theme", bg="black", fg="white")
        is_dark_mode = True

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")

is_dark_mode = False

# Header
header_frame = tk.Frame(root, bg="chocolate", pady=10)
header_frame.pack(fill=tk.X)
title_label = tk.Label(header_frame, text="Currency Converter", bg="chocolate", fg="white", font=("Arial", 16, "bold"))
title_label.pack()

# Content
content_frame = tk.Frame(root, padx=20, pady=20, bg="white")
content_frame.pack(expand=True, fill=tk.BOTH)

# Widgets
ttk.Label(content_frame, text="Enter the amount:", background="white").grid(column=0, row=0, padx=10, pady=10)
amount_entry = ttk.Entry(content_frame)
amount_entry.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(content_frame, text="From Currency:", background="white").grid(column=0, row=1, padx=10, pady=10)
from_currency = ttk.Combobox(content_frame, values=list(cont_dic.keys()), state="write")
from_currency.grid(column=1, row=1, padx=10, pady=10)
from_currency.set("USD")

ttk.Label(content_frame, text="To Currency:", background="white").grid(column=0, row=2, padx=10, pady=10)
to_currency = ttk.Combobox(content_frame, values=list(cont_dic.keys()), state="write")
to_currency.grid(column=1, row=2, padx=10, pady=10)
to_currency.set("EUR")

convert_button = ttk.Button(content_frame, text="Convert", command=handle_conversion)
convert_button.grid(column=0, row=3, columnspan=2, pady=20)

result_label = tk.Label(content_frame, text="", font=("Arial", 12, "bold"), bg="white", fg="black")
result_label.grid(column=0, row=4, columnspan=2, pady=10)

# Toggle Button
toggle_button = tk.Button(root, text="Switch to Black Theme", command=toggle_theme, bg="white", fg="black")
toggle_button.pack(pady=10)
root.mainloop()
