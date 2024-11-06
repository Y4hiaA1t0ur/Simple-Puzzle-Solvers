from TP_Bonus_8Queens.Common import Common


def dfs(board, row):
    if row == len(board):
        Common.print_board(board)
        return True

    for col in range(len(board)):
        if Common.is_safe(board, row, col):
            board[row] = col
            if dfs(board, row + 1):
                return True
            board[row] = -1

    return False


def solve_8_queens():
    board = [-1] * 8
    dfs(board, 0)


solve_8_queens()
