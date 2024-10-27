import tkinter as tk
import random

def play():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = choice_var.get()

    if user_choice == computer_choice:
        result.set("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result.set("You win!")
    else:
        result.set("You lose!")

    computer_choice_label.config(text=f"The computer chose: {computer_choice}")

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("300x400")

root.configure(bg="#2E2E2E")
font_style = ("Helvetica", 14)

choice_var = tk.StringVar(value="rock")
result = tk.StringVar()

header = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 20), bg="#2E2E2E", fg="#FFFFFF")
header.pack(pady=20)

tk.Radiobutton(root, text="Rock", variable=choice_var, value="rock", font=font_style, bg="#2E2E2E", fg="#FFFFFF", selectcolor="#4CAF50").pack(anchor=tk.W, padx=20, pady=5)
tk.Radiobutton(root, text="Paper", variable=choice_var, value="paper", font=font_style, bg="#2E2E2E", fg="#FFFFFF", selectcolor="#4CAF50").pack(anchor=tk.W, padx=20, pady=5)
tk.Radiobutton(root, text="Scissors", variable=choice_var, value="scissors", font=font_style, bg="#2E2E2E", fg="#FFFFFF", selectcolor="#4CAF50").pack(anchor=tk.W, padx=20, pady=5)

play_button = tk.Button(root, text="Play!", command=play, font=font_style, bg="#4CAF50", fg="#000000", padx=10, pady=10)
play_button.pack(pady=30)

tk.Label(root, textvariable=result, font=font_style, bg="#2E2E2E", fg="#FFFFFF").pack(pady=20)

computer_choice_label = tk.Label(root, text="", font=font_style, bg="#2E2E2E", fg="#FFFFFF")
computer_choice_label.pack(pady=10)

root.mainloop()
