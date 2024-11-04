# Put your function here
def ticTacToe(board):
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2]:  # If all three elements in the row are the same
            if row[0] == 'X':
                return 'X'  # Player X wins
            elif row[0] == 'O':
                return 'O'  # Player O wins

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:  # If all three elements in the column are the same
            if board[0][col] == 'X':
                return 'X'  # Player X wins
            elif board[0][col] == 'O':
                return 'O'  # Player O wins

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2]:  # Top-left to bottom-right diagonal
        if board[0][0] == 'X':
            return 'X'  # Player X wins
        elif board[0][0] == 'O':
            return 'O'  # Player O wins
    
    if board[0][2] == board[1][1] == board[2][0]:  # Top-right to bottom-left diagonal
        if board[0][2] == 'X':
            return 'X'  # Player X wins
        elif board[0][2] == 'O':
            return 'O'  # Player O wins

    return 'TIE'

# testing
board = [['X','O','O'],['O','X','O'],['X','O','X']]
print(ticTacToe(board))