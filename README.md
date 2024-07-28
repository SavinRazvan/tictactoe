# Tic-Tac-Toe AI Project

## Project Description
This project involves the creation of an AI that plays Tic-Tac-Toe using the Minimax algorithm. The AI is designed to ensure that it either wins or draws every game, demonstrating optimal decision-making throughout the gameplay.

## Objectives
- **Implement Game Logic:** Develop functions to manage the game state, determine possible actions, and apply those actions.
- **Optimal Decision Making:** Use the Minimax algorithm to compute the best possible move for the AI.
- **End Game Conditions:** Implement checks to determine when the game has ended and the winner, if any.

## Key Components
1. **player(board):** Identifies the current player (X or O).
2. **actions(board):** Lists all possible moves on the board.
3. **result(board, action):** Returns the new board state after a move.
4. **winner(board):** Determines if there's a winner.
5. **terminal(board):** Checks if the game is over.
6. **utility(board):** Assigns a value to the final board state (+1 for X win, -1 for O win, 0 for a tie).
7. **minimax(board):** Computes the optimal move for the current player.

## Installation and Usage
1. **Setup:**
   - Ensure you have Python installed.
   - Download and unzip the project files.
   - Install required dependencies: `pip3 install -r requirements.txt`.

2. **Run the Game:**
   - Start the game using the command: `python runner.py`.

## How It Works
- The game uses the Pygame library to provide a graphical interface.
- Players can choose to play as X or O.
- The AI calculates the best possible move using the Minimax algorithm, ensuring it plays optimally.
- The game continues until there's a winner or a tie, with the AI always making the optimal move.

## AI Implementation Details
- **Minimax Algorithm:** The AI uses the Minimax algorithm to evaluate all possible moves and select the one that maximizes its chances of winning or minimizing its chances of losing.
- **Game State Management:** Functions are implemented to manage the game state, check for winners, and determine possible actions.
- **Optimal Play:** The AI ensures that it never loses by playing the optimal move at every turn.

## Conclusion
This project demonstrates a robust implementation of an unbeatable Tic-Tac-Toe AI, showcasing key AI and algorithmic principles. The use of the Minimax algorithm ensures that the AI always plays optimally, providing a challenging opponent for any player.
