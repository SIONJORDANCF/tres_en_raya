import tkinter as tk
from tkinter import messagebox
import random
import math

# Lógica del juego
# verificacion si alguien gano o empate
def check_winner(board):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for cond in win_conditions:
        a, b, c = cond
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Empate"
    return None

# Algoritmo Minimax puro (IA perfecta)
#un algoritmo que simula la posibles jugadas y evalua el mejor movimineto para ganar o empatar
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    elif winner == "Empate":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score
#mejor jugada de la IA usando el algoritmo minimax
#la IA siempre jugara de manera perfecta, no comete errores
def best_move_minimax(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
# Movimiento aleatorio de la IA
# la IA jugara de manera aleatoria, cometiendo errores
# esto es para simular una IA menos inteligente
def random_ai_move(board):
    available = [i for i in range(9) if board[i] == " "]
    return random.choice(available)

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
            btn = tk.Button(frame_board, text=" ", font=("Arial", 24), width=4, height=2,
                            command=lambda i=i: self.player_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

        # Botón de reinicio
        tk.Button(root, text="Reiniciar", command=self.reset_game).pack(pady=5)

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
            move = best_move_minimax(self.board)
        self.board[move] = "X"
        self.update_buttons()
        winner = check_winner(self.board)
        if winner:
            self.show_winner(winner)

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
