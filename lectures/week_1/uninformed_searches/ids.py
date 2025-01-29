# iterative deepening search

# Start with a depth limit of 0.
# Perform DLS with the current depth limit.
# Increment the depth limit and repeat.

def ids(graph, start, goal):
    def dls_recursive(node, depth, visited):
        if depth == 0:
            return False
        if node == goal:
            print(f"Found {goal}")
            return True

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dls_recursive(neighbor, depth - 1, visited):
                    return True
        return False

    depth = 0
    while True:
        visited = set()
        if dls_recursive(start, depth, visited):
            return
        depth += 1

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
ids(graph, 'A', 'F')
