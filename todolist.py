import tkinter as tk
from tkinter import messagebox

BG = "#f3f4f6"
CARD = "#ffffff"
BTN = "#4f46e5"
BTN_HOVER = "#4338ca"
TEXT = "#111827"

root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("500x600")
root.config(bg=BG)

tk.Label(root, text="📝 To-Do List", font=("Segoe UI", 22, "bold"),
         bg=BG, fg=TEXT).pack(pady=20)

card = tk.Frame(root, bg=CARD)
card.pack(fill="both", padx=25, pady=10)

task_entry = tk.Entry(card, font=("Segoe UI", 14), bd=0)
task_entry.pack(fill="x", padx=20, pady=15)

tk.Frame(card, height=2, bg="#d1d5db").pack(fill="x", padx=20)

task_list = tk.Listbox(card,
                       font=("Segoe UI", 14),
                       bg=CARD, fg=TEXT,
                       bd=0, highlightthickness=0,
                       selectbackground="#e0e7ff",
                       height=12)
task_list.pack(fill="both", padx=20, pady=20)


def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Empty", "Type a task first.")
        return
    task_list.insert(tk.END, "• " + task)
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        task_list.delete(task_list.curselection())
    except:
        messagebox.showwarning("Select", "Choose a task to delete.")

def clear_all():
    if messagebox.askyesno("Clear All", "Delete all tasks?"):
        task_list.delete(0, tk.END)


def make_button(text, command):
    b = tk.Label(card, text=text, bg=BTN, fg="white",
                 font=("Segoe UI", 12, "bold"),
                 pady=10, cursor="hand2")
    b.pack(pady=8, fill="x")

    b.bind("<Enter>", lambda e: b.config(bg=BTN_HOVER))
    b.bind("<Leave>", lambda e: b.config(bg=BTN))
    b.bind("<Button-1>", lambda e: command())
    return b


make_button("Add Task ➕", add_task)
make_button("Delete Selected Task ❌", delete_task)
make_button("Clear All 🗑", clear_all)

root.mainloop()
