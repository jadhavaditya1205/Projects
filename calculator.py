import tkinter as tk

BG = "#f3f4f6"
SCREEN_BG = "#111827"
BTN = "#4f46e5"
BTN_HOVER = "#4338ca"
BTN_TEXT = "#ffffff"

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("350x520")
root.resizable(False, False)
root.configure(bg=BG)

expression = ""

def update_display(value):
    global expression
    expression += value
    display.config(text=expression)

def clear_display():
    global expression
    expression = ""
    display.config(text="")

def delete_last():
    global expression
    expression = expression[:-1]
    display.config(text=expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.config(text=result)
        expression = result
    except:
        display.config(text="Error")
        expression = ""

display = tk.Label(
    root,
    text="",
    bg=SCREEN_BG,
    fg="#00ff7f",
    font=("Segoe UI", 28, "bold"),
    anchor="e",
    padx=15,
    pady=40
)
display.pack(fill="both")

def make_button(parent, text, command):
    btn = tk.Label(
        parent, text=text,
        bg=BTN, fg=BTN_TEXT,
        font=("Segoe UI", 16, "bold"),
        width=6, height=2,
        cursor="hand2"
    )
    btn.pack(side="left", padx=7, pady=7, expand=True)

    btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN))
    btn.bind("<Button-1>", lambda e: command())

    return btn

def make_row():
    frame = tk.Frame(root, bg=BG)
    frame.pack(fill="x")
    return frame

row1 = make_row()
make_button(row1, "C", clear_display)
make_button(row1, "⌫", delete_last)
make_button(row1, "%", lambda: update_display("%"))
make_button(row1, "/", lambda: update_display("/"))

row2 = make_row()
make_button(row2, "7", lambda: update_display("7"))
make_button(row2, "8", lambda: update_display("8"))
make_button(row2, "9", lambda: update_display("9"))
make_button(row2, "*", lambda: update_display("*"))

row3 = make_row()
make_button(row3, "4", lambda: update_display("4"))
make_button(row3, "5", lambda: update_display("5"))
make_button(row3, "6", lambda: update_display("6"))
make_button(row3, "-", lambda: update_display("-"))

row4 = make_row()
make_button(row4, "1", lambda: update_display("1"))
make_button(row4, "2", lambda: update_display("2"))
make_button(row4, "3", lambda: update_display("3"))
make_button(row4, "+", lambda: update_display("+"))

row5 = make_row()
make_button(row5, "0", lambda: update_display("0"))
make_button(row5, ".", lambda: update_display("."))
make_button(row5, "=", calculate)

root.mainloop()
