
This project is a Tic Tac Toe game built using Python with Tkinter for the graphical interface. Instead of playing in the console with text input and output, you play in a real game window with buttons. You are Player X, and the computer is O. The game lets you control who starts first (Player or CPU) and the difficulty (Easy or Hard) using dropdown menus.

In Easy mode, the CPU plays random moves. In Hard mode, the CPU uses the Minimax algorithm, which makes it unbeatable.

How the code works:

1. A 3x3 grid of buttons is created with Tkinter. Each button corresponds to a cell in the game board. When you click a button, it places your X in that cell and disables it. Then it checks for a winner or a draw. If the game is not over, it calls the CPU’s turn.

2. On the CPU’s turn, if the difficulty is Easy it picks a random empty cell. If the difficulty is Hard it uses the Minimax algorithm to calculate the best possible move. It places O in that cell and checks if there is a winner or draw.

3. After every move, the program checks rows, columns, and diagonals to see if X or O has won. If the board is full and no one has won, it is a draw.

4. The scoreboard tracks the number of Player wins, CPU wins, and draws. It updates after every game.

5. The controls include dropdown menus for starter and difficulty, a Restart button to clear the board and start again, and an Exit button to close the game window.



   The Minimax algorithm is what makes the CPU unbeatable in Hard mode. Minimax is a decision-making algorithm used in two-player games. The idea is that the Player (X) tries to minimize the CPU’s chances of winning, while the CPU (O) tries to maximize its own chances. The algorithm explores all possible moves until the game ends and chooses the best possible outcome.
    
    During the CPU’s turn (maximizer), it tries all available moves, simulates the rest of the game recursively, and chooses the move with the highest score. During the Player’s turn (minimizer), it assumes the player will try to minimize the CPU’s score and picks the move with the lowest score.
    
    At every recursive call, the algorithm checks base cases. If CPU wins, it returns +10. If Player wins, it returns -10. If it’s a draw, it returns 0. Depth adjustment is applied so faster wins are scored better and losses are delayed as long as possible.
    
    The CPU checks all possible moves, uses minimax to evaluate them, and picks the move with the best score. For example, if the board has only two moves left, the algorithm simulates both and chooses the one that guarantees a win or avoids losing.
    
    Because Minimax checks every possible outcome, assumes the player also plays optimally, and always chooses the path that guarantees at least a draw, the CPU cannot be beaten. In Hard mode, the best the player can achieve is a draw.
    
    
