# Filename: l2.py

# Constant costs for yantra and exit cells
YANTRA_COST = 0
EXIT_COST = 0
TRAP_COST = 99999

class YantraCollector:
    """
    YantraCollector class to solve the yantra collection puzzle with cost-based movement.
    The player must collect all yantras sequentially and reach the exit.
    """
    
    def __init__(self, grid):
        """
        Initializes the game with the provided grid.

        Args:
            grid (list of list of str): The grid representing the puzzle.
        """
        self.grid = grid
        self.n = len(grid)
        self.start = self.find_position('P')
        self.exit = None
        self.yantras = self.find_all_yantras()
        self.revealed_yantra = self.find_position('Y1')
        ## use these variables if needed
        # self.collected_yantras = 0
        # self.total_frontier_nodes = 0
        # self.total_explored_nodes = 0
        # self.total_cost = 0
        self.cost_map = self.initialize_cost_map()
        
    def initialize_cost_map(self):
        """
        Initializes a dictionary mapping each position to its movement cost.
        """
        cost_map = {}
        for i in range(self.n):
            for j in range(self.n):
                cell_value = self.grid[i][j]
                if isinstance(cell_value, int):  
                    cost_map[(i, j)] = cell_value
                elif cell_value == 'P':
                    cost_map[(i, j)] = 0
                elif cell_value.startswith('Y'):  
                    cost_map[(i, j)] = YANTRA_COST
                elif cell_value == 'E':  
                    cost_map[(i, j)] = EXIT_COST
                elif cell_value == 'T':
                    cost_map[(i, j)] = TRAP_COST 
                # Walls ('#') are ignored, no need to assign them a cost.
        return cost_map
    
    def find_position(self, symbol):
        """
        Finds the position of a given symbol in the grid.

        Args:
            symbol (str): The symbol to locate.

        Returns:
            tuple or None: The position of the symbol, or None if not found.
        """
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == symbol:
                    return (i, j)
        return None

    def find_all_yantras(self):
        """
        Finds and stores the positions of all yantras in the grid.

        Returns:
            dict: A dictionary mapping yantra numbers to their positions.
        """
        positions = {}
        for i in range(self.n):
            for j in range(self.n):
                if isinstance(self.grid[i][j], str) and self.grid[i][j].startswith('Y'):
                    positions[int(self.grid[i][j][1:])] = (i, j)
                elif self.grid[i][j] == 'E':
                    self.exit = (i, j)
        return positions

    def reveal_next_yantra_or_exit(self):
        """
        Reveals the next yantra in sequence or the exit when all yantras are collected.
        """
        self.collected_yantras += 1
        if self.collected_yantras + 1 in self.yantras:
            self.revealed_yantra = self.yantras[self.collected_yantras + 1]
        elif self.collected_yantras == len(self.yantras):
            self.revealed_yantra = self.exit
        else:
            self.revealed_yantra = None

        return self.revealed_yantra

    def goal_test(self, position):
        """
        Checks if the given position matches the currently revealed yantra or exit.
        """
        pass  # TO DO 

    def get_neighbors(self, position):
        """
        Generates valid neighboring positions for the given position.
        Each move has an associated movement cost, with yantras and exit having a fixed cost.
        """
        pass  # TO DO 

    def ucs(self):
        """
        Performs Uniform Cost Search (UCS) to find the path to the goal.
        """
        pass  # TO DO 

    def heuristic(self, position):
        """
        Defines a heuristic function to estimate the cost from the current position to the goal-not necessarily admissible.
        """
        pass  # TO DO 

    def gbfs(self):
        """
        Performs Greedy Best-First Search (GBFS) to find the path to the goal.
        """
        pass  # TO DO 

    def a_star(self):
        """
        Performs A* Search to find the optimal path to the goal.
        """
        pass  # TO DO 

    def solve(self, strategy):
        """
        Solves the yantra collection puzzle using the specified strategy.
        """
        pass  # TO DO 

if __name__ == "__main__":
    grid = [
        ['P', 2, '#', 5, 'Y2'],
        ['T', 2, 3, '#', 1],
        [0, 7, 'Y1', 4, 2],
        ['#', 'T', 2, 1, 3],
        [1, 3, 0, 2, 'E']
    ]

    game = YantraCollector(grid)
    strategy = "A*"  # or "UCS" or "GBFS"
    result = game.solve(strategy)
    
    if result:
        total_frontier_nodes, total_explored_nodes, total_cost = result
        print("Total Frontier Nodes:", total_frontier_nodes)
        print("Total Explored Nodes:", total_explored_nodes)
        print("Total Cost:", total_cost)
    else:
        print("No solution found.")
