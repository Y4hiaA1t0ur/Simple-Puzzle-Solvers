def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def print_board(board):
    n = len(board)
    border_line = "  " + "+----" * n + "+"
    column_headers = "     " + "    ".join(str(i + 1) for i in range(n))

    print(column_headers)
    print(border_line)
    for row in range(n):
        line = f"{row + 1} |"
        for col in range(n):
            if board[row] == col:
                line += " ♛ |"
            else:
                line += "    |"
        print(line)
        print(border_line)


def dfs(board, row):
    if row == len(board):
        print_board(board)
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            if dfs(board, row + 1):
                return True
            board[row] = -1

    return False


def solve_8_queens():
    board = [-1] * 8
    dfs(board, 0)


solve_8_queens()
