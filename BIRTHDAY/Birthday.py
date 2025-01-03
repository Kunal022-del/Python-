import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class BirthdayCardApp:
    def __init__(self, root):  # Corrected the constructor name
        self.root = root
        self.root.title("Birthday Card")
        self.root.geometry("850x900")
        self.root.configure(bg="#f8f9fa")  # Light background color
        # Header label
        header = tk.Label(
            self.root,
            text="Happy Birthday, Papa!",
            font=("Times New Roman", 24, "bold"),  # Changed "Helicha" to "Helvetica"
            fg="Black",
            bg="WHITE",
        )
        header.pack(pady=20)
        # Frame for the image grid
        self.image_frame = tk.Frame(self.root, bg="#ffffff", relief=tk.RIDGE, bd=5)
        self.image_frame.pack(pady=10)
        # Load four images in a 2x2 grid
        self.images = []
        self.image_paths = [
            r"BIRTHDAY/image1.jpg",  # Use raw string literal to avoid escape character issues
            r"BIRTHDAY/image2.jpg",
            r"BIRTHDAY/image3.jpg",
            r"BIRTHDAY/image4.jpg",
        ]
        self.load_images()
        # Frame for the text box
        self.text_frame = tk.Frame(self.root, bg="#FFFFFF", relief=tk.RIDGE, bd=5)
        self.text_frame.pack(pady=20)
        # Text box widget
        self.text_box = tk.Text(
            self.text_frame,
            wrap=tk.WORD,
            font=("Times New Roman", 14),
            height=4,
            width=60,
            fg="white",
            bg="black",
            padx=10,
            pady=10,
            bd=0,
        )
        self.text_box.grid(row=0, column=0)
        # Add scrollbar to the text box
        self.scrollbar = tk.Scrollbar(
            self.text_frame, orient=tk.VERTICAL, command=self.text_box.yview
        )
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.text_box.config(yscrollcommand=self.scrollbar.set)
        # Insert initial text
        self.text_box.insert(
            tk.END,
            "Dear Papa,\n\n"
            "You are my guiding light and my biggest inspiration. "
            "Your love, wisdom, and kindness have shaped my world.\n"
            "Wishing you a day filled with joy and a year ahead full of happiness. "
            "Love you endlessly!\n"
            "I also remember those two days where I had taken money unknowingly so that I could feed my friends during exams, "
            "and the day when I used foul words on a social media app just for fun. I never intended to make you unhappy. "
            "Sorry Papa !.\n\n"
            "With love, always.",
        )
        self.text_box.config(state=tk.DISABLED)  # Make the text box read-only

    def load_images(self):
        try:
            for iteration, img_path in enumerate(self.image_paths):
                img = Image.open(img_path)
                img = img.resize((340, 230))
                photo = ImageTk.PhotoImage(img)
                self.images.append(photo)
                # Create labels for the images
                label = tk.Label(self.image_frame, image=photo, bg="#ffffff")
                label.grid(row=iteration // 2, column=iteration % 2, padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load images: {e}")


root = tk.Tk()
app = BirthdayCardApp(root)
root.mainloop()
