
#################8 Puzzle problem using Heuristic Search####################

import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return (self.depth + self.heuristic()) < (other.depth + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def __str__(self):
        return str(self.state)

    def heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x, y = divmod(self.state[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def is_goal(self):
        return self.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def generate_children(self):
        children = []
        i, j = next((i, j) for i in range(3) for j in range(3) if self.state[i][j] == 0)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_i, new_j = i + move[0], j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in self.state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                children.append(PuzzleNode(new_state, self, move, self.depth + 1))
        return children

def a_star_search(initial_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, initial_state)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.is_goal():
            return current_node

        closed_set.add(current_node)

        for child in current_node.generate_children():
            if child not in closed_set:
                heapq.heappush(open_list, child)

    return None

def print_solution(solution_node):
    path = []
    current_node = solution_node
    while current_node:
        path.append(current_node)
        current_node = current_node.parent
    path.reverse()
    for i, node in enumerate(path):
        print(f"Step {i}: {node.move} \n{node}")
        print()

def main():
    initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]  # Initial state with 0 representing the empty space
    initial_node = PuzzleNode(initial_state)
    solution_node = a_star_search(initial_node)
    if solution_node:
        print("Solution found!")
        print_solution(solution_node)
    else:
        print("No solution found.")
main()
