import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x500")
window.config(bg="#e0f7fa")

rock_img = tk.PhotoImage(file="rock.png")
paper_img = tk.PhotoImage(file="paper.png")
scissor_img = tk.PhotoImage(file="scissor.png")

user_score = 0
comp_score = 0

choices = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissor": scissor_img
}

result_label = tk.Label(window, text="Choose your move!", font=("Arial", 18), bg="#e0f7fa")
result_label.pack(pady=20)

score_label = tk.Label(window, text="Your Score: 0 | Computer Score: 0",
                       font=("Arial", 14), bg="#e0f7fa")
score_label.pack(pady=10)

display_frame = tk.Frame(window, bg="#e0f7fa")
display_frame.pack(pady=10)

user_choice_label = tk.Label(display_frame, bg="#e0f7fa")
user_choice_label.grid(row=0, column=0, padx=20)

comp_choice_label = tk.Label(display_frame, bg="#e0f7fa")
comp_choice_label.grid(row=0, column=1, padx=20)

def play_game(user_choice):
    global user_score, comp_score

    computer_choice = random.choice(["Rock", "Paper", "Scissor"])

    user_choice_label.config(image=choices[user_choice])
    comp_choice_label.config(image=choices[computer_choice])

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        comp_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {comp_score}")

btn_frame = tk.Frame(window, bg="#e0f7fa")
btn_frame.pack(pady=20)

rock_button = tk.Button(btn_frame, image=rock_img, command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(btn_frame, image=paper_img, command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissor_button = tk.Button(btn_frame, image=scissor_img, command=lambda: play_game("Scissor"))
scissor_button.grid(row=0, column=2, padx=10)

def reset_game():
    result_label.config(text="Choose your move!")
    user_choice_label.config(image="")
    comp_choice_label.config(image="")

reset_button = tk.Button(window, text="Play Again", font=("Arial", 14),
                         command=reset_game, bg="#4dd0e1", fg="white")
reset_button.pack(pady=20)

window.mainloop()
