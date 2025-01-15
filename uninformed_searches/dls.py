# depth limited search
# DFS with a depth limit to avoid infinite loops in graphs with cycles or very deep trees.
# Fails if the goal is beyond the depth limit.

def dls(graph, start, depth, visited=None):
    if visited is None:
        visited = set()

    if depth == 0:
        return

    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in graph[start]:
            dls(graph, neighbor, depth - 1, visited)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dls(graph, 'A', 2)
