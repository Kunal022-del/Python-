import random
import tkinter as tk
from tkinter import messagebox, simpledialog


class Password:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x500")
        self.root.configure(bg="#ADD8E6")

        self.site_label = tk.Label(
            root, text="Enter the site:", bg="#ADD8E6", font=("Times New Roman", 16)
        )
        self.site_label.pack(pady=10)

        self.site_entry = tk.Entry(root, width=30)
        self.site_entry.pack(pady=10)

        self.user_label = tk.Label(
            root, text="Enter your name:", bg="#ADD8E6", font=("Times New Roman", 16)
        )
        self.user_label.pack(pady=10)
        self.user_entry = tk.Entry(root, width=30)
        self.user_entry.pack(pady=10)
        self.generate_button = tk.Button(
            root, text="Generate Password", command=self.generate_password
        )
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(
            root, text="Save Password", command=self.save_password
        )
        self.save_button.pack(pady=10)

        self.password = " "

    def generate_password(self):
        site = self.site_entry.get()
        user = self.user_entry.get()
        if not site or not user:
            messagebox.showerror("Error", "Please enter both site and user name.")
            return

        length = simpledialog.askinteger(
            "Input", "Enter the length of the password:", minvalue=1, maxvalue=100
        )
        if length is None:
            return

        self.password = self.create_password(length)
        messagebox.showinfo(
            "Password", f"Generated Password for {user} at {site}: {self.password}"
        )

    def create_password(self, length):
        password = ""
        for _ in range(length):
            random_num = random.randint(33, 125)
            password += chr(random_num)
        return password

    def save_password(self):
        site = self.site_entry.get()
        user = self.user_entry.get()
        if not site or not user or not self.password:
            messagebox.showerror("Error", "No password to save.")
            return
        with open("password_1.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if f"User: {user}" in line and f"Site: {site}" in line:
                    messagebox.showerror(
                        "Error", "Password for this site and user already exists."
                    )
                    return

        with open("password_1.txt", "a+") as file:
            file.write(f"User: {user}\nSite: {site}\nPassword: {self.password}\n\n")
        messagebox.showinfo("Saved", "Password saved successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Password(root)
    root.mainloop()
