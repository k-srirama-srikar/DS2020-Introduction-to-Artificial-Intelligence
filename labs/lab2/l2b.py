# # Filename: l2.py

# # Constant costs for yantra and exit cells
# YANTRA_COST = 0
# EXIT_COST = 0
# TRAP_COST = 99999


# def custom_sort(inp, key=lambda x: x):
#     n = len(inp)
#     if n == 0 or n == 1:
#         return inp
#     for i in range(1, n - 1):
#         it = inp[i]
#         for j in range(i - 1, -1, -1):
#             if key(inp[j]) > key(it):
#                 inp[j + 1] = inp[j]
#                 inp[j] = it
#     return


# class YantraCollector:
#     """
#     YantraCollector class to solve the yantra collection puzzle with cost-based movement.
#     The player must collect all yantras sequentially and reach the exit.
#     """

#     def __init__(self, grid):
#         """
#         Initializes the game with the provided grid.

#         Args:
#             grid (list of list of str): The grid representing the puzzle.
#         """
#         self.grid = grid
#         self.n = len(grid)
#         self.start = self.find_position("P")
#         self.exit = None
#         self.yantras = self.find_all_yantras()
#         self.revealed_yantra = self.find_position("Y1")
#         ## use these variables if needed
#         self.collected_yantras = 0
#         self.total_frontier_nodes = 0
#         self.total_explored_nodes = 0
#         self.total_cost = 0
#         self.cost_map = self.initialize_cost_map()

#     def initialize_cost_map(self):
#         """
#         Initializes a dictionary mapping each position to its movement cost.
#         """
#         cost_map = {}
#         for i in range(self.n):
#             for j in range(self.n):
#                 cell_value = self.grid[i][j]
#                 if isinstance(cell_value, int):
#                     cost_map[(i, j)] = cell_value
#                 elif cell_value == "P":
#                     cost_map[(i, j)] = 0
#                 elif cell_value.startswith("Y"):
#                     cost_map[(i, j)] = YANTRA_COST
#                 elif cell_value == "E":
#                     cost_map[(i, j)] = EXIT_COST
#                 elif cell_value == "T":
#                     cost_map[(i, j)] = TRAP_COST
#                 # Walls ('#') are ignored, no need to assign them a cost.
#         return cost_map

#     def find_position(self, symbol):
#         """
#         Finds the position of a given symbol in the grid.

#         Args:
#             symbol (str): The symbol to locate.

#         Returns:
#             tuple or None: The position of the symbol, or None if not found.
#         """
#         for i in range(self.n):
#             for j in range(self.n):
#                 if self.grid[i][j] == symbol:
#                     return (i, j)
#         return None

#     def find_all_yantras(self):
#         """
#         Finds and stores the positions of all yantras in the grid.

#         Returns:
#             dict: A dictionary mapping yantra numbers to their positions.
#         """
#         positions = {}
#         for i in range(self.n):
#             for j in range(self.n):
#                 if isinstance(self.grid[i][j], str) and self.grid[i][j].startswith("Y"):
#                     positions[int(self.grid[i][j][1:])] = (i, j)
#                 elif self.grid[i][j] == "E":
#                     self.exit = (i, j)
#         return positions

#     def reveal_next_yantra_or_exit(self):
#         """
#         Reveals the next yantra in sequence or the exit when all yantras are collected.
#         """
#         self.collected_yantras += 1
#         if self.collected_yantras + 1 in self.yantras:
#             self.revealed_yantra = self.yantras[self.collected_yantras + 1]
#         elif self.collected_yantras == len(self.yantras):
#             self.revealed_yantra = self.exit
#         else:
#             self.revealed_yantra = None

#         return self.revealed_yantra

#     def goal_test(self, position):
#         """
#         Checks if the given position matches the currently revealed yantra or exit.
#         """
#         # pass  # TO DO
#         if position == self.revealed_yantra:
#             return True
#         return False

#     def get_neighbors(self, position):
#         """
#         Generates valid neighboring positions for the given position.
#         Each move has an associated movement cost, with yantras and exit having a fixed cost.
#         """
#         nesw = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         neighbors = []
#         for i in nesw:
#             neighbor = (position[0] + i[0], position[1] + i[1])
#             if 0 <= neighbor[0] < self.n and 0 <= neighbor[1] < self.n:
#                 if not self.grid[neighbor[0]][neighbor[1]] == "#":
#                     neighbors.append(neighbor)
#         return neighbors
#         # pass  # TO DO

#     # def ucs(self):
#     #     """
#     #     Performs Uniform Cost Search (UCS) to find the path to the goal.
#     #     """
#     #     frontier_list = Priority_queue(key=lambda x: x[0][1])
#     #     frontier_list.insert((((0, 0), self.cost_map[(0, 0)]), [], 0))
#     #     # solution: tuple[list, int] | None
#     #     solution = None
#     #     explored_list = []
#     #     # current_cost = 0
#     #     # tracking_path = []
#     #     while True:
#     #         if frontier_list.is_empty():
#     #             break
#     #         # If required we have to maintain two seperate frontier lists rather than like triplets
#     #         curr, path, cost = frontier_list.get_item()
#     #         print("checking:", path)
#     #         # print("Debug:")
#     #         # print(curr)
#     #         """Change this part to store only the path insted the cost of whole path"""
#     #         path.append(curr)
#     #         cost += curr[1]
#     #         if self.goal_test(curr[0]):
#     #             if solution == None:
#     #                 solution = (path, cost)
#     #                 print(solution)
#     #             else:
#     #                 if cost < solution[1]:
#     #                     solution = (path, cost)
#     #                 else:
#     #                     path = solution[0]
#     #                     cost = solution[1]
#     #         explored_list.append(curr)
#     #         neighbors = self.get_neighbors(curr[0])
#     #         for neighbor in neighbors:
#     #             # ref = False
#     #             # for i in frontier_list:
#     #             #     if i[0] == neighbor:
#     #             #         ref = True
#     #             #         break
#     #             if frontier_list.contains(neighbor, key=lambda x: x[0]) or (
#     #                 neighbor in explored_list
#     #             ):
#     #                 continue
#     #             frontier_list.insert((neighbor, path, cost))
#     #     return solution

#     # def ucs(self):
#     #     """
#     #     Performs Uniform Cost Search (UCS) to find the path to the goal.
#     #     """
#     #     frontier_list = Priority_queue(key = lambda x: x[0][1])
#     #     explored_list = []
#     #     curr_cost = 0
#     #     solution = None
#     #     while True:
#     #         if frontier_list.is_empty():
#     #             break
#     #         path: list
#     #         cost: int
#     #         curr: tuple[int,int]
#     #         curr,path,cost = frontier_list.get_item()
#     #         curr_cost = self.cost_map[curr]
#     #         cost+= curr_cost
#     #         path.append(curr)
#     #         if self.goal_test(curr):
#     #             solution = (path,cost)
#     #         neighbors = self.get_neighbors(curr)
#     #         for neighbor in neighbors:
#     #     return solution

#     def ucs(self):
#         """
#         Performs Uniform Cost Search (UCS) to find the path to the goal.
#         """
#         print(self.cost_map)
#         print(self.grid)
#         frontier_list: list[list[tuple[int, int], list[tuple], int]]
#         frontier_list = [[self.start, [self.start], 0]]
#         explored_list = []
#         solution = None
#         while True:
#             if len(frontier_list) == 0:
#                 break
#             custom_sort(frontier_list, key=lambda x: (x[2], -x[0][0] - x[0][1]))
#             curr, path, cost = frontier_list.pop(0)
#             explored_list.append(curr)
#             if self.goal_test(curr):
#                 solution = (path, cost)
#                 self.total_frontier_nodes += len(frontier_list)
#                 self.total_explored_nodes += len(explored_list)
#                 return solution, frontier_list, explored_list
#             neighbors = self.get_neighbors(curr)
#             for neighbor in neighbors:
#                 ref = False
#                 curr_cost = self.cost_map[neighbor]
#                 print("debug:",neighbor,self.cost_map[neighbor])
#                 for i in frontier_list:
#                     if neighbor == i[0]:
#                         ref = True
#                         if cost + curr_cost < i[2]:
#                             i[2] = cost + curr_cost
#                             i[1] = path + [neighbor]
#                             break
#                 if (not ref) and (neighbor not in explored_list):
#                     frontier_list.append(
#                         [neighbor, path + [neighbor], cost + curr_cost]
#                     )
#         return None

#     def heuristic(self, position):
#         """
#         Defines a heuristic function to estimate the cost from the current position to the goal-not necessarily admissible.
#         """
#         pass  # TO DO

#     def gbfs(self):
#         """
#         Performs Greedy Best-First Search (GBFS) to find the path to the goal.
#         """
#         pass  # TO DO

#     def a_star(self):
#         """
#         Performs A* Search to find the optimal path to the goal.
#         """
#         pass  # TO DO

#     def solve(self, strategy):
#         """
#         Solves the yantra collection puzzle using the specified strategy.
#         """
#         if strategy == "UCS":
#             fun = self.ucs
#         self.total_costcost = 0
#         soln = [self.start]
#         while self.revealed_yantra:
#             a = fun()
#             # print(a[0])
#             self.total_cost += a[0][1]
#             # print("frontier list:", a[1], len(a[1]))
#             # print("explored list:", a[2], len(a[2]))
#             self.start = self.revealed_yantra
#             self.reveal_next_yantra_or_exit()
#         return self.total_frontier_nodes, self.total_explored_nodes, self.total_cost

#         # pass  # TO DO


# if __name__ == "__main__":
#     grid = [
#         ["P", 2, "#", 5, "Y2"],
#         ["T", 2, 3, "#", 1],
#         [0, 7, "Y1", 4, 2],
#         ["#", "T", 2, 1, 3],
#         [1, 3, 0, 2, "E"],
#     ]
#     #     grid = [
#     #     ['P', 2, '#', 5, 'Y11', 3, 4, 1, 2, 'T', 6, 8, 9, 3, 'Y8'],
#     #     ['T', 5, 1, 6, 'Y2', '#', 4, 7, 0, 3, 9, 'T', 2, 'Y14', 8],
#     #     [0, 'T', 2, 'Y13', '#', 8, 6, 5, 7, 3, 9, 'T', 'Y3', 4, 2],
#     #     ['Y10', 5, 8, 2, '#', 9, 3, 7, 'T', 0, 4, 6, 'E', 5, 'T'],
#     #     ['Y1', 'T', 3, 9, 0, 8, 7, 'Y7', 'T', 5, 3, 'Y5', '#', 2, 7],
#     #     ['Y4', 4, 8, 2, 3, 1, 'Y12', 'T', 7, 9, 0, 'Y6', 6, 3, 'T'],
#     #     [2, 'Y9', 1, 9, 6, 0, 'T', 5, 'Y15', 7, 8, 3, 'Y10', 4, 'T'],
#     #     ['Y14', 9, 'T', 1, 'Y11', 2, 5, 6, '#', 4, 'Y13', 3, 7, 8, 9],
#     #     [1, 'Y6', 7, 5, 3, 'Y1', 'T', 4, 9, 6, 0, 8, 'Y8', 2, 3],
#     #     ['Y12', 0, 'T', 5, 8, 1, 'Y4', 2, 7, 3, 9, 'T', 6, 4, 7],
#     #     [3, 'Y2', 'T', 6, 9, 4, 7, 'Y5', 2, 1, 8, 'Y15', 5, 3, 9],
#     #     [2, 3, 'Y7', 'T', 9, 1, 'Y10', 5, 7, 4, 8, 0, 6, 'T', 3],
#     #     ['Y13', 8, 0, 6, 4, 9, 'T', 3, 7, 2, 5, 6, 1, 9, 'E'],
#     # ]

#     game = YantraCollector(grid)
#     strategy = "UCS"  # or "UCS" or "GBFS"
#     result = game.solve(strategy)
#     # result = game.ucs()
#     # print(result)
#     # for i in result:
#     #     print(i)
#     #     print("debug")
#     # print (result)
#     # check = game.solve(strategy)
#     # print(game.total_explored_nodes, game.total_frontier_nodes)
#     if result:
#         total_frontier_nodes, total_explored_nodes, total_cost = result
#         print("Total Frontier Nodes:", total_frontier_nodes)
#         print("Total Explored Nodes:", total_explored_nodes)
#         print("Total Cost:", total_cost)
#     else:
#         print("No solution found.")




#         Finds the position of a given symbol in the grid.

#         Args:
#             symbol (str): The symbol to locate.

#         Returns:
#             tuple or None: The position of the symbol, or None if not found.
#         """
#         for i in range(self.n):
#             for j in range(self.n):
#                 if self.grid[i][j] == symbol:
#                     return (i, j)
#         return None
# ... (206 lines left)
# Collapse
# message.txt
# 11 KB
# ﻿
# Bharath
# bharath_._00402
# Filename: l2.py

# Constant costs for yantra and exit cells
YANTRA_COST = 0
EXIT_COST = 0
TRAP_COST = 99999


# def custom_sort(inp, key=lambda x: x):
#     n = len(inp)
#     if n == 0 or n == 1:
#         return inp
#     for i in range(1, n - 1):
#         it = inp[i]
#         for j in range(i - 1, -1, -1):
#             if key(inp[j]) > key(it):
#                 inp[j + 1] = inp[j]
#                 inp[j] = it
#     return


def custom_sort(inp, key=lambda x: x):
    n = len(inp)
    if n <= 1:
        return inp
    for i in range(1, n):
        it = inp[i]
        j = i - 1
        while j >= 0 and key(inp[j]) > key(it):
            inp[j + 1] = inp[j]
            j -= 1
        inp[j + 1] = it

    return inp


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
        self.start = self.find_position("P")
        self.exit = None
        self.yantras = self.find_all_yantras()
        self.revealed_yantra = self.find_position("Y1")
        ## use these variables if needed
        self.collected_yantras = 0
        self.total_frontier_nodes = 0
        self.total_explored_nodes = 0
        self.total_cost = 0
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
                    # if str.isdigit(cell_value):
                    # change these later
                    cost_map[(i, j)] = int(cell_value)
                elif cell_value == "P":
                    cost_map[(i, j)] = 0
                elif cell_value.startswith("Y"):
                    cost_map[(i, j)] = YANTRA_COST
                elif cell_value == "E":
                    cost_map[(i, j)] = EXIT_COST
                elif cell_value == "T":
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
                if isinstance(self.grid[i][j], str) and self.grid[i][j].startswith("Y"):
                    positions[int(self.grid[i][j][1:])] = (i, j)
                elif self.grid[i][j] == "E":
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
        # pass  # TO DO
        if position == self.revealed_yantra:
            return True
        return False

    def get_neighbors(self, position):
        """
        Generates valid neighboring positions for the given position.
        Each move has an associated movement cost, with yantras and exit having a fixed cost.
        """
        nesw = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        neighbors = []
        for i in nesw:
            neighbor = (position[0] + i[0], position[1] + i[1])
            if 0 <= neighbor[0] < self.n and 0 <= neighbor[1] < self.n:
                if not self.grid[neighbor[0]][neighbor[1]] == "#":
                    neighbors.append(neighbor)
        return neighbors
        # pass  # TO DO

    # def ucs(self):
    #     """
    #     Performs Uniform Cost Search (UCS) to find the path to the goal.
    #     """
    #     print(self.cost_map)
    #     print(self.grid)
    #     frontier_list: list[list[tuple[int, int], list[tuple], int]]
    #     frontier_list = [[self.start, [self.start], 0]]
    #     explored_list = []
    #     solution = None
    #     while True:
    #         if len(frontier_list) == 0:
    #             break
    #         custom_sort(frontier_list, key=lambda x: (x[2], -x[0][0] - x[0][1]))
    #         curr, path, cost = frontier_list.pop(0)
    #         explored_list.append(curr)
    #         if self.goal_test(curr):
    #             solution = (path, cost)
    #             self.total_frontier_nodes += len(frontier_list)
    #             self.total_explored_nodes += len(explored_list)
    #             return solution, frontier_list, explored_list
    #         neighbors = self.get_neighbors(curr)
    #         for neighbor in neighbors:
    #             ref = False
    #             curr_cost = self.cost_map[neighbor]
    #             print("debug:", neighbor, self.cost_map[neighbor])
    #             for i in frontier_list:
    #                 if neighbor == i[0]:
    #                     ref = True
    #                     if cost + curr_cost < i[2]:
    #                         i[2] = cost + curr_cost
    #                         i[1] = path + [neighbor]
    #                         break
    #             if (not ref) and (neighbor not in explored_list):
    #                 frontier_list.append(
    #                     [neighbor, path + [neighbor], cost + curr_cost]
    #                 )
    #     return None

    def ucs(self):
        frontier_list = [[self.start, 0]]
        explored_list = []
        while True:
            if len(frontier_list) == 0:
                return (None, 0, 0)
            custom_sort(frontier_list, key=lambda x: x[1])
            print('F ',frontier_list)
            curr, curr_cost = frontier_list.pop(0)
            explored_list.append(curr)
            if self.goal_test(curr):
                # print('F ',frontier_list)
                # print(explored_list)
                return curr_cost, len(frontier_list), len(explored_list)
            neighbors = self.get_neighbors(curr)
            for neighbor in neighbors:
                ref = False
                neigh_cost = self.cost_map[neighbor]
                for i in range(len(frontier_list)):
                    if neighbor == frontier_list[i][0]:
                        ref = True
                        if curr_cost + neigh_cost < frontier_list[i][1]:
                            frontier_list[i][1] = curr_cost + neigh_cost
                            break
                if (not ref) and (neighbor not in explored_list):
                    frontier_list.insert(0, [neighbor, curr_cost + neigh_cost])
        # return None

    def heuristic(self, position):
        """
        Defines a heuristic function to estimate the cost from the current position to the goal-not necessarily admissible.
        """
        
        # pass  # TO DO

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
        if strategy == "UCS":
            fun = self.ucs
        # self.total_cost = 0
        # soln = [self.start]
        while self.revealed_yantra:
            curr_sol = fun()
            if curr_sol[0] is None:
                return None
            cost, frontier, explored = curr_sol
            self.total_cost += cost
            self.total_frontier_nodes += frontier
            self.total_explored_nodes += explored
            self.start = self.revealed_yantra
            self.reveal_next_yantra_or_exit()
        return (self.total_frontier_nodes, self.total_explored_nodes, self.total_cost)

        # pass  # TO DO


if __name__ == "__main__":
    grid = [
        ["P", 2, "#", 5, "Y2"],
        ["T", 2, 3, "#", 1],
        [0, 7, "Y1", 4, 2],
        ["#", "T", 2, 1, 3],
        [1, 3, 0, 2, "E"],
    ]
    #     grid = [
    #     ['P', 2, '#', 5, 'Y11', 3, 4, 1, 2, 'T', 6, 8, 9, 3, 'Y8'],
    #     ['T', 5, 1, 6, 'Y2', '#', 4, 7, 0, 3, 9, 'T', 2, 'Y14', 8],
    #     [0, 'T', 2, 'Y13', '#', 8, 6, 5, 7, 3, 9, 'T', 'Y3', 4, 2],
    #     ['Y10', 5, 8, 2, '#', 9, 3, 7, 'T', 0, 4, 6, 'E', 5, 'T'],
    #     ['Y1', 'T', 3, 9, 0, 8, 7, 'Y7', 'T', 5, 3, 'Y5', '#', 2, 7],
    #     ['Y4', 4, 8, 2, 3, 1, 'Y12', 'T', 7, 9, 0, 'Y6', 6, 3, 'T'],
    #     [2, 'Y9', 1, 9, 6, 0, 'T', 5, 'Y15', 7, 8, 3, 'Y10', 4, 'T'],
    #     ['Y14', 9, 'T', 1, 'Y11', 2, 5, 6, '#', 4, 'Y13', 3, 7, 8, 9],
    #     [1, 'Y6', 7, 5, 3, 'Y1', 'T', 4, 9, 6, 0, 8, 'Y8', 2, 3],
    #     ['Y12', 0, 'T', 5, 8, 1, 'Y4', 2, 7, 3, 9, 'T', 6, 4, 7],
    #     [3, 'Y2', 'T', 6, 9, 4, 7, 'Y5', 2, 1, 8, 'Y15', 5, 3, 9],
    #     [2, 3, 'Y7', 'T', 9, 1, 'Y10', 5, 7, 4, 8, 0, 6, 'T', 3],
    #     ['Y13', 8, 0, 6, 4, 9, 'T', 3, 7, 2, 5, 6, 1, 9, 'E'],
    # ]

    game = YantraCollector(grid)
    strategy = "UCS"  # or "UCS" or "GBFS"
    result = game.solve(strategy)
    # result = game.ucs()
    # print(result)
    # for i in result:
    #     print(i)
    #     print("debug")
    # print (result)
    # check = game.solve(strategy)
    # print(game.total_explored_nodes, game.total_frontier_nodes)
    if result:
        total_frontier_nodes, total_explored_nodes, total_cost = result
        print("Total Frontier Nodes:", total_frontier_nodes)
        print("Total Explored Nodes:", total_explored_nodes)
        print("Total Cost:", total_cost)
    else:
        print("No solution found.")