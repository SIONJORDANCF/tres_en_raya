import tkinter as tk
from tkinter import messagebox

# Interfaz gráfica
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya con IA")
        self.board = [" "] * 9
        self.buttons = []
        self.mode = tk.StringVar(value="difícil")

        # Selector de dificultad
        frame_top = tk.Frame(root)
        frame_top.pack()
        tk.Label(frame_top, text="Dificultad IA:").pack(side="left")
        tk.Radiobutton(frame_top, text="Difícil", variable=self.mode, value="difícil").pack(side="left")
        tk.Radiobutton(frame_top, text="Fácil", variable=self.mode, value="fácil").pack(side="left")

        # Tablero de botones
        frame_board = tk.Frame(root)
        frame_board.pack()
        for i in range(9):
            btn = tk.Button(frame_board, text=" ", font=("Arial", 24), width=4, height=2, command=lambda i=i: self.player_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

        # Botón de reinicio
        tk.Button(root, text="Reiniciar", command=self.reset_game).pack(pady=5)
    '''
    def player_move(self, index):
        if self.board[index] == " ":
            self.board[index] = "O"
            self.update_buttons()
            winner = check_winner(self.board)
            if winner:
                self.show_winner(winner)
            else:
                self.root.after(300, self.ai_move)
    
    def ai_move(self):
        if self.mode.get() == "fácil":
            move = random_ai_move(self.board)
        else:
            move = best_move_with_mistakes(self.board)
        self.board[move] = "X"
        self.update_buttons()
        winner = check_winner(self.board)
        if winner:
            self.show_winner(winner)
    '''
    def update_buttons(self):
        for i in range(9):
            self.buttons[i].config(text=self.board[i])

    def show_winner(self, winner):
        if winner == "Empate":
            messagebox.showinfo("Resultado", "¡Empate!")
        else:
            messagebox.showinfo("Resultado", f"¡Ganó {winner}!")
        self.reset_game()

    def reset_game(self):
        self.board = [" "] * 9
        self.update_buttons()

# Iniciar app
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
