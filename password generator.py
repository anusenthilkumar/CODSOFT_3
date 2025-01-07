import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters.")
            return

        # Define the character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Ensure the password includes at least one of each character type
        all_chars = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(symbols)

        # Fill the rest of the password length with a mix of all character types
        all_chars += ''.join(random.choices(lower + upper + digits + symbols, k=length - 4))

        # Shuffle the characters to ensure randomness
        password = ''.join(random.sample(all_chars, len(all_chars)))

        # Display the generated password
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

# Create the GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Add GUI elements
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

length_label = tk.Label(frame, text="Enter the desired password length:")
length_label.grid(row=0, column=0, pady=5)

length_entry = tk.Entry(frame, width=10)
length_entry.grid(row=0, column=1, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="", fg="blue", wraplength=300)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
