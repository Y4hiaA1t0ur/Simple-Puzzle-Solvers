from collections import deque

from TP_Bonus_8Queens.Common import Common


def bfs_solve_n_queens(n):
    queue = deque()
    queue.append([-1] * n)

    while queue:
        board = queue.popleft()
        row = next((i for i in range(n) if board[i] == -1), n)

        if row == n:
            Common.print_board(board)
            print("\nSolution found!\n")
            return

        for col in range(n):
            if Common.is_safe(board, row, col):
                new_board = board[:]
                new_board[row] = col
                queue.append(new_board)


def solve_8_queens():
    bfs_solve_n_queens(8)


solve_8_queens()
