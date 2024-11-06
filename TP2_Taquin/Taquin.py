import heapq


def heuristic(state, goal):
    distance = 0
    goal_positions = {}

    for i in range(3):
        for j in range(3):
            value = goal[i][j]
            goal_positions[value] = (i, j)

    for i in range(3):
        for j in range(3):
            current_value = state[i][j]
            if current_value != 0:
                goal_position = goal_positions[current_value]
                distance += abs(goal_position[0] - i) + abs(goal_position[1] - j)

    return distance


def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], \
                new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors


def a_star(start, goal):
    start_tuple = tuple(tuple(row) for row in start)
    goal_tuple = tuple(tuple(row) for row in goal)

    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start_tuple, []))

    visited = set()
    visited.add(start_tuple)

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal_tuple:
            return path + [state]

        for neighbor in get_neighbors([list(row) for row in state]):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                h = heuristic(neighbor, goal)
                heapq.heappush(open_list, (g + 1 + h, g + 1, neighbor_tuple, path + [state]))

    return None


start_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

final_path = a_star(start_state, goal_state)

if final_path:
    print("Solution found!")
    for one in final_path:
        for r in one:
            print(r)
        print()
else:
    print("No solution found.")
