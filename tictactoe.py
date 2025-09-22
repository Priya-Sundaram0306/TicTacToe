import tkinter as tk
from tkinter import messagebox
import math, random

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

# Game state
gameBoard = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
starter = tk.StringVar(value="Player")   # Dropdown-controlled starter
difficulty = tk.StringVar(value="Hard")  # Dropdown-controlled difficulty
scores = {"Player": 0, "CPU": 0, "Draws": 0}

# ---------- Game Logic Functions ----------

def checkForWinner():
    for i in range(3):
        if gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2] != " ":
            return gameBoard[i][0]
        if gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i] != " ":
            return gameBoard[0][i]
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] != " ":
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] != " ":
        return gameBoard[0][2]
    return None

def isMovesLeft():
    return any(cell == " " for row in gameBoard for cell in row)

def evaluate():
    winner = checkForWinner()
    if winner == "O": return +10
    if winner == "X": return -10
    return 0

def minimax(depth, isMaximizing):
    score = evaluate()
    if score == 10: return score - depth
    if score == -10: return score + depth
    if not isMovesLeft(): return 0
    if isMaximizing:  # CPU turn
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if gameBoard[i][j] == " ":
                    gameBoard[i][j] = "O"
                    best = max(best, minimax(depth + 1, False))
                    gameBoard[i][j] = " "
        return best
    else:  # Player turn
        best = math.inf
        for i in range(3):
            for j in range(3):
                if gameBoard[i][j] == " ":
                    gameBoard[i][j] = "X"
                    best = min(best, minimax(depth + 1, True))
                    gameBoard[i][j] = " "
        return best

def bestMove():
    bestVal, move = -math.inf, (-1, -1)
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == " ":
                gameBoard[i][j] = "O"
                moveVal = minimax(0, False)
                gameBoard[i][j] = " "
                if moveVal > bestVal:
                    move, bestVal = (i, j), moveVal
    return move

# ---------- Game Actions ----------

def updateScoreboard():
    player_label.config(text=f"Player (X): {scores['Player']}")
    cpu_label.config(text=f"CPU (O): {scores['CPU']}")
    draw_label.config(text=f"Draws: {scores['Draws']}")

def endGame(winner):
    if winner == "X":
        messagebox.showinfo("Game Over", "🎉 You win!")
        scores["Player"] += 1
    elif winner == "O":
        messagebox.showinfo("Game Over", "💻 CPU wins!")
        scores["CPU"] += 1
    else:
        messagebox.showinfo("Game Over", "🤝 It's a draw!")
        scores["Draws"] += 1
    updateScoreboard()
    disableBoard()

def disableBoard():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

def enableBoard():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="normal", text=" ")

def resetGame():
    global gameBoard
    gameBoard = [[" " for _ in range(3)] for _ in range(3)]
    enableBoard()
    if starter.get() == "CPU":
        cpuTurn()

def cpuTurn():
    if difficulty.get() == "Easy":
        available = [(i, j) for i in range(3) for j in range(3) if gameBoard[i][j] == " "]
        row, col = random.choice(available)
    else:
        row, col = bestMove()
    gameBoard[row][col] = "O"
    buttons[row][col].config(text="O", state="disabled")
    winner = checkForWinner()
    if winner: endGame(winner)
    elif not isMovesLeft(): endGame(None)

def playerTurn(i, j):
    if gameBoard[i][j] == " ":
        gameBoard[i][j] = "X"
        buttons[i][j].config(text="X", state="disabled")
        winner = checkForWinner()
        if winner: endGame(winner)
        elif not isMovesLeft(): endGame(None)
        else: cpuTurn()

# ---------- UI Setup ----------

# Create buttons for grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=("Arial", 24),
                                  width=5, height=2,
                                  command=lambda i=i, j=j: playerTurn(i, j))
        buttons[i][j].grid(row=i, column=j)

# Dropdown controls (inside window)
controls_frame = tk.Frame(root)
controls_frame.grid(row=3, column=0, columnspan=3, pady=10)

# Starter dropdown
starter_label = tk.Label(controls_frame, text="Who Starts:")
starter_label.pack(side="left", padx=5)
starter_menu = tk.OptionMenu(controls_frame, starter, "Player", "CPU")
starter_menu.pack(side="left", padx=5)

# Difficulty dropdown
difficulty_label = tk.Label(controls_frame, text="Difficulty:")
difficulty_label.pack(side="left", padx=5)
difficulty_menu = tk.OptionMenu(controls_frame, difficulty, "Easy", "Hard")
difficulty_menu.pack(side="left", padx=5)

# Restart and Exit buttons
restart_button = tk.Button(controls_frame, text="🔄 Restart", command=resetGame, bg="lightblue")
restart_button.pack(side="left", padx=10)
exit_button = tk.Button(controls_frame, text="❌ Exit", command=root.destroy, bg="salmon")
exit_button.pack(side="left", padx=10)

# Scoreboard
score_frame = tk.Frame(root)
score_frame.grid(row=4, column=0, columnspan=3, pady=10)

player_label = tk.Label(score_frame, text=f"Player (X): {scores['Player']}", font=("Arial", 12))
player_label.pack(side="left", padx=10)
cpu_label = tk.Label(score_frame, text=f"CPU (O): {scores['CPU']}", font=("Arial", 12))
cpu_label.pack(side="left", padx=10)
draw_label = tk.Label(score_frame, text=f"Draws: {scores['Draws']}", font=("Arial", 12))
draw_label.pack(side="left", padx=10)

# Run the game
root.mainloop()
