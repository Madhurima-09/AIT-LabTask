def is_safe(board, row, col):
    for i in range(col):
        # Check left row, upper-left diagonal, and lower-left diagonal
        if board[i] == row or abs(board[i] - row) == col - i:
            return False
    return True

def solve(board, col):
    if col == 4:
        return True
    for row in range(4):
        if is_safe(board, row, col):
            board[col] = row
            if solve(board, col + 1):
                return True
    return False

# board[col] = row position of queen in that column
board = [-1] * 4
solve(board, 0)

# Print grid
for r in range(4):
    print(" ".join("Q" if board[c] == r else "." for c in range(4)))
