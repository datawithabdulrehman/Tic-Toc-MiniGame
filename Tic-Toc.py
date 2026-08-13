
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("TIC-TAC-TOE")
        self.current_player = "X"
        self.buttons = []
        self.create_widgets()
        self.winner = False

    def create_widgets(self):
        self.label = tk.Label(self.root, text=f"Player {self.current_player}'s Turn", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=(i // 3) + 1, column=i % 3)
            self.buttons.append(button)

    def button_click(self, index):
        if self.buttons[index]["text"] == "" and not self.winner:
            self.buttons[index]["text"] = self.current_player
            if self.check_winner():
                self.label.config(text=f"Player {self.current_player} Wins!")
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} Wins!")
                self.winner = True
                self.root.quit()
            elif self.check_draw():
                self.label.config(text="It's a Draw!")
                messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
                self.root.quit()
            else:
                self.toggle_player()

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for combo in combos:
            if (self.buttons[combo[0]]["text"] == self.buttons[combo[1]]["text"] ==
                self.buttons[combo[2]]["text"] != ""):
                for i in combo:
                    self.buttons[i].config(bg="lightgreen")
                return True
        return False

    def check_draw(self):
        return all(button["text"] != "" for button in self.buttons)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
