import tkinter as tk
from tkinter import messagebox
import re
import random

# -----------------------------
# Password Strength Checker
# -----------------------------
def analyze_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return

    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Password should be at least 8 characters long")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add at least one uppercase letter")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add at least one lowercase letter")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("• Add at least one number")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("• Add at least one special character")

    strength = (score / 5) * 100

    # Strength Label
    if score <= 2:
        strength_text = "Weak Password"
    elif score <= 4:
        strength_text = "Medium Password"
    else:
        strength_text = "Strong Password"

    result_label.config(
        text=f"{strength_text}\nStrength: {strength:.0f}%"
    )

    if feedback:
        feedback_label.config(text="\n".join(feedback))
    else:
        feedback_label.config(
            text="✓ Excellent Password!"
        )

# -----------------------------
# Generate Strong Password
# -----------------------------
def generate_password():
    suggestions = [
        "Tiger@2026",
        "Dragon#123",
        "Python$456",
        "Secure@789",
        "Strong#Pass1",
        "Cyber@Shield99",
        "Safe#Password7"
    ]

    password_entry.delete(0, tk.END)
    password_entry.insert(0, random.choice(suggestions))

# -----------------------------
# GUI Window
# -----------------------------
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("500x400")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Password Strength Analyzer",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=15)

password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12),
    show="*"
)
password_entry.pack(pady=10)

check_btn = tk.Button(
    root,
    text="Check Password",
    font=("Arial", 11),
    command=analyze_password
)
check_btn.pack(pady=10)

generate_btn = tk.Button(
    root,
    text="Generate Strong Password",
    font=("Arial", 11),
    command=generate_password
)
generate_btn.pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=15)

feedback_label = tk.Label(
    root,
    text="",
    justify="left",
    font=("Arial", 10)
)
feedback_label.pack(pady=10)

root.mainloop()
