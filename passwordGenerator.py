import tkinter as tk
from tkinter import messagebox
import random
import string

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#f0f0f0")

title = tk.Label(root, text="Password Generator",
                 font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=15)

box = tk.Frame(root, bg="white", bd=2, relief="groove")
box.pack(padx=20, pady=10, fill="both")

password_text = tk.Label(box, text="Password will appear here",
                         font=("Arial", 14), bg="white", fg="gray")
password_text.pack(pady=20)

slider_label = tk.Label(box, text="Select password length:",
                        font=("Arial", 12), bg="white")
slider_label.pack()

length_var = tk.IntVar(value=10)

slider = tk.Scale(box, from_=4, to=30, orient="horizontal",
                  variable=length_var, length=250, bg="white")
slider.pack(pady=10)

def generate_password():
    length = length_var.get()

    letters_and_numbers = string.ascii_letters + string.digits

    password = "".join(random.choice(letters_and_numbers) for _ in range(length))

    password_text.config(text=password, fg="black")

def copy_password():
    password = password_text.cget("text")

    if password == "Password will appear here":
        messagebox.showwarning("Error", "Please generate a password first!")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied!")

def make_button(name, action):
    btn = tk.Button(box, text=name, font=("Arial", 12, "bold"),
                    bg="#4f46e5", fg="white", command=action)
    btn.pack(pady=10, fill="x")

make_button("Generate Password", generate_password)
make_button("Copy Password", copy_password)

root.mainloop()
