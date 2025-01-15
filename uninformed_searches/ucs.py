# uniform cost search or
# dijkstra's algorithm

import heapq

def ucs(graph, start, goal):
    pq = [(0,start)]
    visited = set()

    while pq:
        cost, node = heapq.heappushpop(pq)
        
        if node in visited:
            continue

        visited.add(node)

        if node==goal:
            print(f"Reached {goal} from {start} with cost of {cost}")
            return
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor))


# Example graph as adjacency list with weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
ucs(graph, 'A', 'F')