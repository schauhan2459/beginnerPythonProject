#Snake Water Gun

import random
import tkinter as tk
from tkinter import messagebox

class SnakeWaterGunGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Water Gun Game")

        self.user_choices = ["snake", "water", "gun"]
        self.user_score = 0
        self.computer_score = 0
        self.round_num = 1
        self.total_rounds = 0

        self.label = tk.Label(root, text="Snake Water Gun Game", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.rounds_entry_label = tk.Label(root, text="Enter number of rounds:")
        self.rounds_entry_label.pack()

        self.rounds_entry = tk.Entry(root)
        self.rounds_entry.pack()

        self.round_label = tk.Label(root, text=f"Round {self.round_num}", font=("Helvetica", 12))
        self.round_label.pack()

        self.choice_label = tk.Label(root, text="Choose snake, water, or gun:")
        self.choice_label.pack()

        self.choice_var = tk.StringVar(root)
        self.choice_var.set(self.user_choices[0])
        self.choice_menu = tk.OptionMenu(root, self.choice_var, *self.user_choices)
        self.choice_menu.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_round)
        self.play_button.pack(pady=10)

    def play_round(self):
        self.total_rounds = int(self.rounds_entry.get())
        user_choice = self.choice_var.get()
        computer_choice = random.choice(self.user_choices)

        result = self.check_result(user_choice, computer_choice)
        self.update_scores(result)
        self.update_ui(user_choice, computer_choice, result)

        if self.round_num > self.total_rounds-1:
            self.show_game_over()

        self.round_num += 1
        self.round_label.config(text=f"Round {self.round_num}")

    def check_result(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "snake" and computer_choice == "water") or \
             (user_choice == "water" and computer_choice == "gun") or \
             (user_choice == "gun" and computer_choice == "snake"):
            return "win"
        else:
            return "lose"

    def update_scores(self, result):
        if result == "win":
            self.user_score += 1
        elif result == "lose":
            self.computer_score += 1

    def update_ui(self, user_choice, computer_choice, result):
        result_text = f"Computer chose {computer_choice}. You {result}!"
        self.result_label = tk.Label(root, text=result_text, font=("Helvetica", 12))
        self.result_label.pack()

        self.score_display = tk.Label(root, text=f"You: {self.user_score} | Computer: {self.computer_score}")
        self.score_display.pack()

    def show_game_over(self):
        game_over_message = "Game Over!\n\n"
        if self.user_score > self.computer_score:
            game_over_message += "Congratulations! You win!"
        elif self.user_score < self.computer_score:
            game_over_message += "Computer wins the game. Better luck next time!"
        else:
            game_over_message += "It's a draw!"

        messagebox.showinfo("Game Over", game_over_message)
        self.root.destroy()

        # Reset the game for a new round of play
        self.user_score = 0
        self.computer_score = 0
        self.round_num = 1
        self.round_label.config(text=f"Round {self.round_num}")

        self.result_label.destroy()
        self.score_display.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeWaterGunGame(root)
    root.mainloop()
