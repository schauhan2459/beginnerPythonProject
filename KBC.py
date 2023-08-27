#kbc 

import tkinter as tk
from tkinter import messagebox

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")

        self.questions = [
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3),
            ("What is your name?", "ram", "sham", "laxmn", "None", 3)
        ]

        self.prize_levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

        self.current_question = 0
        self.money = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 12), command=lambda i=i: self.answer_question(i))
            self.buttons.append(button)
            button.pack(pady=10, padx=20, fill=tk.X)

        self.quit_button = tk.Button(root, text="Quit", font=("Helvetica", 12), command=self.quit_game)
        self.quit_button.pack(pady=10, padx=20, fill=tk.X)

        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            question, *options, correct_option = self.questions[self.current_question]
            self.question_label.config(text=f"Question {self.current_question + 1} (Prize: Rs. {self.prize_levels[self.current_question]}):\n{question}")
            for i, option in enumerate(options):
                self.buttons[i].config(text=option)
        else:
            self.show_final_result()

    def answer_question(self, selected_option):
        question, *options, correct_option = self.questions[self.current_question]
        
        if selected_option == correct_option - 1:
            self.money = self.prize_levels[self.current_question]
            
            # if self.current_question == 4:
            #     self.money = 10000
            if 4 <= self.current_question <= 9:
                self.money = 10000
            elif 10 <= self.current_question < 14:
                self.money = 320000
            elif self.current_question==14:
                self.money=1000000
                
            self.current_question += 1
            self.update_question()
            if self.current_question == len(self.questions):
                self.show_final_result()
        else:
            self.show_final_result()

    def show_final_result(self):
        messagebox.showinfo("Game Over", f"Game Over! You have won Rs. {self.money}")
        self.root.destroy()

    def quit_game(self):
        if self.current_question > 0:
            previous_prize = self.prize_levels[self.current_question - 1]
            messagebox.showinfo("Quit", f" You won Rs. {previous_prize}.")
        else:
            messagebox.showinfo("Quit", " You won nothing.")
        self.root.destroy()
    def final(self):
        if self.current_question ==14:
            messagebox.showinfo("Congratulations!!\n", f" You won Rs. {self.money}.")
        self.root.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = KBCGame(root)
    root.mainloop()
