import heapq

def get_neighbors(node):
    x, y = node
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]  # 4-connected grid
    return neighbors

def manhattan_heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# A* Search
def a_star_search(start, goal, heuristic):
    open_list = []  # Priority queue to store nodes
    closed_list = set()  # Set of explored nodes
    g_cost = {start: 0}  # Cost to reach a node from the start
    
    # Push the start node into the priority queue with f(n) = g(n) + h(n)
    heapq.heappush(open_list, (heuristic(start, goal), start))
    
    # While there are nodes to explore
    while open_list:
        _, current = heapq.heappop(open_list)
        
        # If the current node is the goal, we found the solution
        if current == goal:
            return True
        
        closed_list.add(current)
        
        # Explore the neighbors of the current node
        for neighbor in get_neighbors(current):
            if neighbor not in closed_list:
                tentative_g = g_cost[current] + 1  # Assuming uniform cost for neighbors
                
                # If this path to the neighbor is better, add it to the open list
                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g
                    f_cost = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
    
    return False

# Example Usage
start = (0, 0)
goal = (3, 3)

# Run A* Search
found = a_star_search(start, goal, manhattan_heuristic)
print("Found path:", found)