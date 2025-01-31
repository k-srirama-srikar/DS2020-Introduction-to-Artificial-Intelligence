# Filename: 142301013.py

class Node:
    '''
    A node class to store the current position, parent, children
    of a node in a tree
    '''
    def __init__(self, value, parent=None):
        """
        Initializes the node with the position and parent.

        Args:
            value (tuple) : Tuple containing the position.
            parent (Node object) : Parent of the node (self)
        """
        self.parent = parent
        self.value = value
        self.children = []
        
    def add_child(self, child):
        """
        Adds a child to the node(self).

        Args:
            child (Node object): Child of the node.
        """
        self.children.append(child)


class Tree:
    '''
    A tree class to store the paths in the bfs or dfs
    '''
    def __init__(self):
        '''
        Initilizes an empty tree with an empty root
        '''
        self.root=None

    def insert(self, value, parent=None):
        '''
        Creates a node object and adds to the current tree

        Args:
            value (tuple) : the position of the node explored
            parent (Node object) : node object of the parent of the value

        Returns:
            new_node (node object) : the node the contains the value
        '''
        new_node = Node(value, parent)
        if self.root is None:
            self.root = new_node
        else:
            parent.add_child(new_node)
        return new_node

    def backtrack(self, node) -> list:
        path = []
        while node!=None:
            # print(path)
            path.append(node.value)
            node = node.parent
        return path[::-1]


class YantraCollector:
    """
    YantraCollector class to solve the yantra collection puzzle.
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
        self.collected_yantras = 0
        self.total_frontier_nodes = 0
        self.total_explored_nodes = 0
        
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
                if self.grid[i][j].startswith('Y'):
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

    def goal_test(self, position):
        """
        Checks if the given position matches the currently revealed yantra or exit.

        Args:
            position (tuple): The current position to check.
        """
        if position==self.revealed_yantra:
            self.reveal_next_yantra_or_exit()
            return True
        return False

    def get_neighbors(self, position):
        """
        Generates valid neighboring positions for the given position.

        Args:
            position (tuple): The current position of the player.
        """
        neighbors = []
        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_i, new_j = position[0] + i, position[1] + j
            if (0 <= new_i < self.n and 0 <= new_j < self.n) and self.grid[new_i][new_j] != '#' and self.grid[new_i][new_j] != "T":
                neighbors.append((new_i, new_j))
        return neighbors

    def bfs(self, start, goal):
        """
        Performs Breadth-First Search (BFS) to find the path to the goal.

        Args:
            start (tuple): The starting position.
            goal (tuple): The goal position.
        """
        explored_list = []
        frontier_list = []
        # frontier_list.append(start)
        e_list_vals = []
        f_list_vals = []
        path = Tree()
        path.insert(start)
        frontier_list.append(path.root)
        f_list_vals.append(start)
        while frontier_list:
            if frontier_list[0].value == goal:
                current = frontier_list.pop(0)
                explored_list.append(current)
                return path.backtrack(current), len(frontier_list), len(explored_list)
            
            current = frontier_list.pop(0)
            f_list_vals.pop(0)
            parent_node = current.parent
            explored_list.append(current)
            e_list_vals.append(current.value)
            neighbors = self.get_neighbors(current.value)
            
            for neighbor in neighbors:
                if neighbor not in e_list_vals and neighbor not in f_list_vals:
                    neighbor_node = path.insert(neighbor,current)
                    frontier_list.append(neighbor_node)
                    f_list_vals.append(neighbor)
            
            if len(frontier_list) == 0:
                return None, None, None
        
        explored_list.append(frontier_list.pop(0))
        return path.backtrack(current), len(frontier_list), len(explored_list)
        
        
    def dfs(self, start, goal):
        """
        Performs Depth-First Search (DFS) to find the path to the goal.

        Args:
            start (tuple): The starting position.
            goal (tuple): The goal position.
        """
        explored_list = []  
        frontier_list = []  
        e_list_vals = []  
        f_list_vals = []  
        path = Tree()  
        path.insert(start)
        frontier_list.append(path.root)
        f_list_vals.append(start)
        
        while frontier_list:
            current = frontier_list.pop(0)  
            f_list_vals.pop(0)  
            
            if current.value == goal:
                explored_list.append(current)
                return path.backtrack(current), len(frontier_list), len(explored_list)

            explored_list.append(current)
            e_list_vals.append(current.value)

            neighbors = self.get_neighbors(current.value)
            for neighbor in neighbors[::-1]:
                if neighbor not in e_list_vals and neighbor not in f_list_vals:
                    neighbor_node = path.insert(neighbor, current)
                    frontier_list.insert(0, neighbor_node)  
                    f_list_vals.insert(0, neighbor)
            
            if len(frontier_list) == 0:
                return None, None, None

        explored_list.append(frontier_list.pop(0))
        return path.backtrack(current), len(frontier_list), len(explored_list)


    def solve(self, strategy):
        """
        Solves the yantra collection puzzle using the specified strategy.

        Args:
            strategy (str): The search strategy (BFS or DFS).
        """
        if strategy == "BFS":
            func = self.bfs
            
        elif strategy == "DFS":
            func = self.dfs
        else :
            raise "Invalid strategy"
        
        curr_pos = self.start
        solution_path = [self.start]
        while self.revealed_yantra:
            path, frontier, explored = func(curr_pos, self.revealed_yantra)
            # print(path, frontier, explored)
            if path is None:
                return False, None, None
            solution_path += path[1:]
            # print(f"Frontier: {frontier}, Explored: {explored}")
            self.total_frontier_nodes += frontier
            self.total_explored_nodes += explored
            curr_pos = self.revealed_yantra
            self.reveal_next_yantra_or_exit()
        return solution_path, self.total_frontier_nodes, self.total_explored_nodes


if __name__ == "__main__":
    grid = [
        ['P', '.', '.', '#', 'Y2'],
        ['#', 'T', '.', '#', '.'],
        ['.', '.', 'Y1', '.', '.'],
        ['#', '.', '.', 'T', '.'],
        ['.', '.', '.', '.', 'E']
    ]

    game = YantraCollector(grid)
    strategy = "DFS"  # or "DFS"
    solution, total_frontier, total_explored = game.solve(strategy)
    if solution:
        print("Solution Path:", solution)
        print("Total Frontier Nodes:", total_frontier)
        print("Total Explored Nodes:", total_explored)
    else:
        print("No solution found.")
