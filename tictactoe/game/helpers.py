import random


def is_move_valid(board, x, y, winner):
    # validate that the move is made on a space that is within the board and is available
    return 0 <= x < 3 and 0 <= y < 3 and board[x][y] == '' and winner is None


def make_move(board):
    # the computer makes a random move based on a random available spot in the board
    availables_moves = [(i, j) for i in range(3)
                        for j in range(3) if board[i][j] == '']
    if availables_moves:
        return random.choice(availables_moves)
    return None


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # check columns
            return True
    # check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
