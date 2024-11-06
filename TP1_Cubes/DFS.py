from Situation import Situation

INITIAL_STATE = 0b111001000000000000
FINAL_STATE = 0b000000000000111001


class SituationTree:
    def __init__(self, root):
        self.root = Situation(root)
        self.visited = set()
        self.solution = []

    def dfs(self, current_situation=None, depth_limit=float('inf'), current_depth=0):

        if current_situation is None:
            current_situation = self.root

        if current_depth > depth_limit:
            return False

        if current_situation.situation_bin == FINAL_STATE:
            self.solution.append(current_situation.situation_bin)
            return True

        if current_situation.situation_bin in self.visited:
            return False

        self.visited.add(current_situation.situation_bin)
        self.solution.append(current_situation.situation_bin)

        for child_bin in current_situation.children:
            child_situation = Situation(child_bin, parent=current_situation)
            if self.dfs(child_situation, depth_limit, current_depth + 1):
                return True

        self.solution.pop()
        return False


initial_state = INITIAL_STATE
tree = SituationTree(initial_state)

depth_lmt = 10

found_solution = tree.dfs(depth_limit=depth_lmt)

if found_solution:
    print("Solution found!")

    print("Path to solution (binary):")
    for step in tree.solution:
        print(Situation.situation_to_human_readable(step))
        print()


else:
    print("No solution found.")
