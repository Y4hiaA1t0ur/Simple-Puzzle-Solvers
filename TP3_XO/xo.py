def display_tic_tac_toe(filled_mask: int, items_bin: int):
    print("\nCurrent Board:")

    def get_char(filled, item):
        if not filled:
            return ' '
        return 'X' if item else 'O'

    for row in range(2, -1, -1):
        filled_row = (filled_mask >> (row * 3)) & 0b111
        items_row = (items_bin >> (row * 3)) & 0b111
        row_str = []
        for col in range(2, -1, -1):
            filled = (filled_row >> col) & 1
            item = (items_row >> col) & 1
            row_str.append(get_char(filled, item))
        print(" " + " | ".join(row_str))
        if row > 0:
            print("---|---|---")
    print()


def check_winner(filled_mask: int, items_bin: int) -> int:
    """ Check for a winner. Return +1 for AI win, -1 for human win, 0 for draw """
    winning_positions = [
        0b111000000, 0b000111000, 0b000000111,
        0b100100100, 0b010010010, 0b001001001,
        0b100010001, 0b001010100
    ]
    ai_mask = filled_mask & ~items_bin
    human_mask = filled_mask & items_bin
    for win in winning_positions:
        if (ai_mask & win) == win:
            return 1
        if (human_mask & win) == win:
            return -1
    if filled_mask == 0b111111111:
        return 0
    return None


def minimax(filled_mask: int, items_bin: int, is_ai_turn: bool) -> tuple:
    winner = check_winner(filled_mask, items_bin)
    if winner is not None:
        return None, winner

    best_score = -float('inf') if is_ai_turn else float('inf')
    best_move = None

    for cell_index in range(9):
        if (filled_mask >> cell_index) & 1 == 0:
            new_filled_mask = filled_mask | (1 << cell_index)
            new_items_bin = items_bin
            if is_ai_turn:
                new_items_bin &= ~(1 << cell_index)
            else:
                new_items_bin |= (1 << cell_index)

            _, score = minimax(new_filled_mask, new_items_bin, not is_ai_turn)

            if is_ai_turn:
                if score > best_score:
                    best_score = score
                    best_move = cell_index
            else:
                if score < best_score:
                    best_score = score
                    best_move = cell_index

    return best_move, best_score


def ai_move(filled_mask: int, items_bin: int):
    """ AI makes its move using Minimax """
    best_move, _ = minimax(filled_mask, items_bin, True)
    if best_move is not None:
        filled_mask |= (1 << best_move)
        items_bin &= ~(1 << best_move)
        print("AI has made its move.")
        display_tic_tac_toe(filled_mask, items_bin)
    return filled_mask, items_bin


def human_move(filled_mask: int, items_bin: int):
    """ Get the human player's move """
    print("Your turn (You are 'X')")
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if not (1 <= move <= 9):
                print("Invalid input. Enter a number between 1 and 9.")
                continue

            cell_index = 9 - move
            if (filled_mask >> cell_index) & 1:
                print("Cell is already occupied. Choose another cell.")
                continue

            filled_mask |= (1 << cell_index)
            items_bin |= (1 << cell_index)
            break
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
    return filled_mask, items_bin


def play_tic_tac_toe():
    filled_mask = 0
    items_bin = 0
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print("Board positions are numbered as follows:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    while True:
        display_tic_tac_toe(filled_mask, items_bin)

        filled_mask, items_bin = human_move(filled_mask, items_bin)
        if check_winner(filled_mask, items_bin) == -1:
            display_tic_tac_toe(filled_mask, items_bin)
            print("Congratulations! You win!")
            break
        elif check_winner(filled_mask, items_bin) == 0:
            display_tic_tac_toe(filled_mask, items_bin)
            print("It's a draw!")
            break

        filled_mask, items_bin = ai_move(filled_mask, items_bin)
        if check_winner(filled_mask, items_bin) == 1:
            display_tic_tac_toe(filled_mask, items_bin)
            print("AI wins! Better luck next time.")
            break
        elif check_winner(filled_mask, items_bin) == 0:
            display_tic_tac_toe(filled_mask, items_bin)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_tic_tac_toe()
