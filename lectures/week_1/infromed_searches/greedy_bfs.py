import heapq

# Greedy Best-First Search
def greedy_bfs(start, goal, heuristic):
    open_list = []  # Priority queue to store nodes
    closed_list = set()  # Set of explored nodes
    
    # Push the start node into the priority queue with its heuristic value
    heapq.heappush(open_list, (heuristic(start, goal), start))
    
    # While there are nodes to explore
    while open_list:
        # Pop the node with the lowest heuristic value
        _, current = heapq.heappop(open_list)
        
        # If the current node is the goal, we found the solution
        if current == goal:
            return True
        
        closed_list.add(current)
        
        # Explore the neighbors of the current node
        for neighbor in get_neighbors(current):
            if neighbor not in closed_list:
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))
    
    return False

# Example of a simple Manhattan distance heuristic
def manhattan_heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# Example function to get neighbors of a node
def get_neighbors(node):
    x, y = node
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]  # 4-connected grid
    return neighbors

# Example Usage
start = (0, 0)
goal = (3, 3)

# Run Greedy BFS
found = greedy_bfs(start, goal, manhattan_heuristic)
print("Found path:", found)