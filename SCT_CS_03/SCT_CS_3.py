import re
import tkinter as tk
from tkinter import StringVar

def check_password_strength():
    password = entry.get()
    strength = 0
    strength_text = ""

    # Check for length (at least 8 characters)
    if len(password) >= 8:
        strength += 1
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    
    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    
    # Assess strength level
    if strength <= 1:
        strength_text = "Very Weak"
        label_strength.config(fg="red")
    elif strength == 2:
        strength_text = "Weak"
        label_strength.config(fg="orange")
    elif strength == 3:
        strength_text = "Moderate"
        label_strength.config(fg="yellow")
    elif strength == 4:
        strength_text = "Strong"
        label_strength.config(fg="green")
    elif strength == 5:
        strength_text = "Very Strong"
        label_strength.config(fg="darkgreen")

    # Update label text
    strength_var.set(f"Password Strength: {strength_text}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Password Strength Checker")

# Set the window size and background color
root.geometry("400x300")
root.configure(bg="#2c3e50")

# Add some styling to the widgets
style = {
    "bg": "#ecf0f1",
    "fg": "#2c3e50",
    "font": ("Arial", 14),
    "relief": "flat",
    "bd": 2,
}

# Title label
title_label = tk.Label(root, text="Check Your Password Strength", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

# Input field for password
entry = tk.Entry(root, show="*", width=30, font=("Arial", 14), bd=2, relief="flat")
entry.pack(pady=10)

# Button to check password strength
button = tk.Button(root, text="Check Strength", command=check_password_strength, bg="#1abc9c", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=2)
button.pack(pady=10)

# Label to display password strength
strength_var = StringVar()
strength_var.set("Password Strength: ")
label_strength = tk.Label(root, textvariable=strength_var, font=("Helvetica", 14, "bold"), bg="#2c3e50", fg="#ecf0f1")
label_strength.pack(pady=20)

# Footer style
footer = tk.Label(root, text="Developed by Yash Raj Dubey", font=("Arial", 10, "italic"), bg="#2c3e50", fg="#bdc3c7")
footer.pack(side="bottom", pady=10)

# Start the GUI event loop
root.mainloop()
