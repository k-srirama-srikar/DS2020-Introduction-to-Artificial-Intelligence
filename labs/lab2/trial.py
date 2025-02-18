import heapq

class ObjectCollector:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = None
        self.objects = []
        self.exit = None
        self.traps = set()
        self.walls = set()
        self.parse_grid()
    
    def parse_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                if cell == 'P':
                    self.start = (r, c)
                elif cell.startswith('Y'):
                    self.objects.append((r, c))
                elif cell == 'E':
                    self.exit = (r, c)
                elif cell == '#':
                    self.walls.add((r, c))
                elif cell == 'T':
                    self.traps.add((r, c))
    
    def get_neighbors(self, position):
        r, c = position
        neighbors = []
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.walls:
                cost = self.grid[nr][nc] if isinstance(self.grid[nr][nc], int) else 0
                neighbors.append(((nr, nc), cost))
        
        return neighbors
    
    def goal_test(self, position):
        return position == self.exit
    
    def ucs(self):
        return self.uniform_cost_search()
    
    def uniform_cost_search(self):
        frontier = []
        heapq.heappush(frontier, (0, self.start))
        explored = set()
        cost_so_far = {self.start: 0}
        
        while frontier:
            cost, current = heapq.heappop(frontier)
            if self.goal_test(current):
                return cost
            
            explored.add(current)
            for neighbor, move_cost in self.get_neighbors(current):
                new_cost = cost_so_far[current] + move_cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(frontier, (new_cost, neighbor))
        
        return float('inf')
    
    def heuristic(self, position):
        return 0  # Replace with a custom heuristic
    
    def gbfs(self):
        return self.greedy_best_first_search()
    
    def greedy_best_first_search(self):
        frontier = []
        heapq.heappush(frontier, (self.heuristic(self.start), self.start))
        explored = set()
        
        while frontier:
            _, current = heapq.heappop(frontier)
            if self.goal_test(current):
                return True
            
            explored.add(current)
            for neighbor, _ in self.get_neighbors(current):
                if neighbor not in explored:
                    heapq.heappush(frontier, (self.heuristic(neighbor), neighbor))
        
        return False
    
    def a_star(self):
        return self.a_star_search()
    
    def a_star_search(self):
        frontier = []
        heapq.heappush(frontier, (0, self.start))
        explored = set()
        cost_so_far = {self.start: 0}
        
        while frontier:
            cost, current = heapq.heappop(frontier)
            if self.goal_test(current):
                return cost
            
            explored.add(current)
            for neighbor, move_cost in self.get_neighbors(current):
                new_cost = cost_so_far[current] + move_cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor)
                    heapq.heappush(frontier, (priority, neighbor))
        
        return float('inf')
    
    def solve(self, strategy):
        if strategy == 'ucs':
            return self.ucs()
        elif strategy == 'gbfs':
            return self.gbfs()
        elif strategy == 'a_star':
            return self.a_star()
        else:
            raise ValueError("Unknown strategy")
