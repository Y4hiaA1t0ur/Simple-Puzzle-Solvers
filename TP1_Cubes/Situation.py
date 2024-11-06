class Situation:
    def __init__(self, situation_bin, parent=None):
        self.children = []
        self.situation_bin = situation_bin
        self.get_children_bin()
        self.parent = parent

    @staticmethod
    def situation_to_human_readable(input_bin):
        # Create the mapping from binary to human-readable format
        cube_map = {
            '11': 'C',
            '10': 'B',
            '01': 'A',
            '00': ' '
        }

        # Prepare a list to hold the result for each table
        tables = []

        # Process each table's 6 bits
        for table_num in range(3):
            table_representation = []
            # Extract 6 bits (3 groups of 2 bits) for this table
            table_bits = (input_bin >> (table_num * 6)) & 0b111111  # Extract the relevant 6 bits
            for position in range(3):  # 3 positions per table
                # Extract 2 bits for this position
                cube_bits = (table_bits >> (position * 2)) & 0b11
                # Convert to a string of two bits
                cube_str = f'{cube_bits:02b}'
                # Map the 2-bit string to the corresponding cube or empty spot
                table_representation.append(cube_map[cube_str])
            tables.append(table_representation)

        # Keep the table order as is but reverse the cube positions for each table
        tables = [table for table in tables[::-1]]

        # Create a human-readable string (no need to reverse the output anymore)
        readable_string = "\n".join(
            f"Table {i + 1}: {' | '.join(tables[i])}" for i in range(3)
        )

        return readable_string

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

    def get_children_bin(self):
        possible_moves = self.__possible_movement_generator()
        for movement in possible_moves:
            self.children.append((self.situation_bin & movement[0]) | movement[1])


# sit = Situation(0b001110000001000000)
# for child in sit.children:
#     child_bin = bin(child)[2:].zfill(18)  # Convert to binary and pad to 18 bits
#     print(child_bin)

# print(Situation.situation_to_human_readable(0b000010000011000001))
