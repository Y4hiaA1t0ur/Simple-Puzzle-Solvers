from collections import deque

from Situation import Situation

INITIAL_STATE = 0b111001000000000000
FINAL_STATE = 0b000000000000111001


class SituationTree:
    def __init__(self, root):
        self.root = Situation(root)
        self.visited = set()
        self.solution = []

    def bfs(self):

        queue = deque([(self.root, [])])

        while queue:

            current_situation, path = queue.popleft()

            if current_situation.situation_bin == FINAL_STATE:
                self.solution = path + [current_situation.situation_bin]
                return True

            if current_situation.situation_bin in self.visited:
                continue

            self.visited.add(current_situation.situation_bin)

            for child_bin in current_situation.children:
                child_situation = Situation(child_bin, parent=current_situation)

                queue.append((child_situation, path + [current_situation.situation_bin]))

        return False


initial_state = INITIAL_STATE
tree = SituationTree(initial_state)

found_solution = tree.bfs()

if found_solution:
    print("Solution found!")

    print("Path to solution:")
    for step in tree.solution:
        print(Situation.situation_to_human_readable(step))
        print()
else:
    print("No solution found.")
