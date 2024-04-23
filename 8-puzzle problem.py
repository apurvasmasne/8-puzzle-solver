from queue import PriorityQueue

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Helper function to find the coordinates of a value in the puzzle
def find_coord(puzzle, value):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == value:
                return i, j

# Heuristic function (Manhattan distance)
def heuristic(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                goal_i, goal_j = find_coord(goal_state, puzzle[i][j])
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# Helper function to generate new puzzle states
def generate_states(puzzle):
    new_states = []
    zero_i, zero_j = find_coord(puzzle, 0)
    for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_i, new_j = zero_i + move[0], zero_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in puzzle]
            new_state[zero_i][zero_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[zero_i][zero_j]
            new_states.append(new_state)
    return new_states

# A* search algorithm
def solve_puzzle(initial_state):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, initial_state))
    
    while not queue.empty():
        _, current_state = queue.get()
        if current_state == goal_state:
            return current_state
        visited.add(tuple(map(tuple, current_state)))
        
        for new_state in generate_states(current_state):
            if tuple(map(tuple, new_state)) not in visited:
                queue.put((heuristic(new_state), new_state))
                visited.add(tuple(map(tuple, new_state)))
    return None

# Function to print the puzzle state
def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Example initial state
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    print("Initial Puzzle State:")
    print_puzzle(initial_state)
    print("\nSolving...")
    solution = solve_puzzle(initial_state)
    if solution:
        print("\nSolution:")
        print_puzzle(solution)
    else:
        print("No solution found.")
