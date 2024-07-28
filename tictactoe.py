"""
Tic Tac Toe Player
"""

import copy
import random
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Check if board is empty
    count_x = 0
    count_o = 0
    # Check every list in board (every "row" in our case)
    for row in range(len(board)):
        # We take every list to check for X and Y
        for col in range(len(board[row])):
            # Count every X and Y found in board
            if board[row][col] == X:
                count_x += 1
            if board[row][col] == O:
                count_o += 1

    # If game is not over:
    if not terminal(board):
        if count_x > count_o:
            return O
        elif count_x == count_o:
            return X
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Iterate through each cell of the board, if it's empty, add it to possible_actions
    possible_actions = set()
    # Board is 3x3, verify row
    for i in range(len(board)):
        # j corespond with the cell (verify every cell on column)
        for j in range(len(board[i])):
            # check possible moves
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    # return tuple with possible_actions
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Return error if there is a mistake and someone try to use an Used Cell,
    # just use our possible actions
    if action not in actions(board):
        raise ValueError("Not a valid action.")

    row, col = action
    # print(action)
    # print(f"row is: {row}, and col is: {col}")

    # Create a deep copy of the board to avoid modifying the original board
    board_update = copy.deepcopy(board)
    board_update[row][col] = player(board)

    return board_update


def check_rows_winner(board, player):
    """
    Helper function to check if there's a winner in any row for the given player
    """
    for row in range(len(board)):
        # Check for winner on horizontal
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def check_columns_winner(board, player):
    """
    Helper function to check if there's a winner in any column for the given player
    """
    for col in range(len(board)):
        # Check for winner on vertical
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False


def check_diagonals_winner(board, player):
    # Helper function to check if there's a winner in any diagonal for the given player
    if player == board[0][0] == board[1][1] == board[2][2]:
        return True
    elif player == board[0][2] == board[1][1] == board[2][0]:
        return True
    else:
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check if X wins
    if check_rows_winner(board, X) or check_columns_winner(board, X) or check_diagonals_winner(board, X):
        return X
    # Check if O wins
    elif check_rows_winner(board, O) or check_columns_winner(board, O) or check_diagonals_winner(board, O):
        return O
    # If no winner, return None
    else:
        None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if X wins
    if winner(board) == X:
        return True
    # Check if O wins
    if winner(board) == O:
        return True

    for row in board:
        # Verify every cell in the column
        for cell in row:
            # Check if cell is empty
            if cell == EMPTY:
                return False

    # If no empty cells, it's a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # X wins the game
    if winner(board) == X:
        return 1
    # O wins the game
    elif winner(board) == O:
        return -1
    # Tie
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the game is over, stop
    if terminal(board):
        return None
    # Check if the board is at the start and give a random position for X
    elif board == [[EMPTY] * 3] * 3:
        return (random.randint(0, 2), random.randint(0, 2))

    # If it's X's (maximizer) turn to make a move
    elif player(board) == X:
        # Initialize the best value (v) as negative infinity, representing the worst possible value for X (maximizer).
        v = -math.inf
        # Initialize chosen_cell as None, which will store the optimal move found for X.
        chosen_cell = None

        # Loop through all possible actions (available cells) on the board.
        for action in actions(board):
            # Call the min_value function to get the minimum evaluation score for the given action.
            maxEvaluation = min_value(result(board, action))
            # If the new evaluation score is greater than the current best value (v) for X,  update v and store the action as chosen_cell, which is the current best move for X.
            if maxEvaluation > v:
                v = maxEvaluation
                chosen_cell = action

    # If it's O's (minimizer) turn to make a move
    elif player(board) == O:
        # Initialize the best value (v) as positive infinity, representing the worst possible value for O (minimizer).
        v = math.inf
        # Initialize chosen_cell as None, which will store the optimal move found for O.
        chosen_cell = None

        # Loop through all possible actions (available cells) on the board.
        for action in actions(board):
            # Call the max_value function to get the maximum evaluation score for the given action.
            minEvaluation = max_value(result(board, action))
            # If the new evaluation score is smaller than the current best value (v) for O, update v and store the action as chosen_cell, which is the current best move for O.
            if minEvaluation < v:
                v = minEvaluation
                chosen_cell = action

    # Return the chosen_cell, which represents the optimal move for the current player (either X or O).
    return chosen_cell


def max_value(board):
    """
    Helper function for the maximizer (X)
    """
    v = -math.inf
    if terminal(board):
        return utility(board)

    # Loop through all possible actions (available cells) on the board.
    for action in actions(board):
        # Call the min_value function to get the minimum evaluation score for the given action.
        v = max(v, min_value(result(board, action)))
        # print(f"this is action: {action}")
        # print(f"this is v: {v}")

    # Return the maximum value found (best move) for X (maximizer) among all possible actions.
    return v


def min_value(board):
    """
    Helper function for the minimizer (O)
    """
    v = math.inf
    if terminal(board):
        return utility(board)

    #  Loop through all possible actions (available cells) on the board.
    for action in actions(board):
        # Call the max_value function to get the maximum evaluation score for the given action.
        v = min(v, max_value(result(board, action)))
        # print(f"this is action: {action}")
        # print(f"this is v: {v}")

    # Return the minimum value found (best move) for O (minimizer) among all possible actions.
    return v
