class Common:
    def __init__(self):
        pass

    @staticmethod
    def is_safe(board, row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    @staticmethod
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
