class Situation:
    def __init__(self, situation_bin, parent=None):
        self.children = []
        self.situation_bin = situation_bin
        self.get_children()
        self.parent = parent

    def decisions_generator(self):
        empty_spots = []
        cubes_to_move = []
        for table_num in range(3):
            sit_bin_copy = self.situation_bin >> table_num * 6
            current_to_move = []
            for position in range(3):
                current_check = sit_bin_copy & 3
                if current_check == 0:
                    empty_spots.append([table_num, position])
                    break
                else:
                    current_to_move = [table_num, position, current_check]
                sit_bin_copy = sit_bin_copy >> 2
            if current_to_move:
                cubes_to_move.append(current_to_move)
        return empty_spots, cubes_to_move

    def __possible_movement_generator(self):
        empty_spots, cubes_to_move = self.decisions_generator()
        possible_movements = []
        for free_cube in cubes_to_move:
            p = (3 * free_cube[0] + free_cube[1]) * 2
            mask = (1 << 18) - 1
            zero_mask = (3 << p)
            first_mask = mask & ~zero_mask
            for empty_spot in empty_spots:
                if empty_spot[0] == free_cube[0]:
                    continue
                second_mask = (free_cube[2] << ((3 * empty_spot[0] + empty_spot[1]) * 2))
                possible_movements.append([first_mask, second_mask])

        return possible_movements

    def get_children(self):
        possible_moves = self.__possible_movement_generator()
        for movement in possible_moves:
            self.children.append((self.situation_bin & movement[0]) | movement[1])


# sit = Situation(0b001110000001000000)
# for child in sit.children:
#     child_bin = bin(child)[2:].zfill(18)  # Convert to binary and pad to 18 bits
#     print(child_bin)
