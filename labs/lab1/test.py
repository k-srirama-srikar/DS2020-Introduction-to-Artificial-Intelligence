# from l1 import YantraCollector

# grid = []

# with open('test-cases.txt', 'r+') as f:
#     g1 = []
#     # print(f)
#     # print(f.readlines())
#     for line in f.readlines():
#         # print(line)
#         l1 = line.strip()
#         print(l1)
#         if l1:
#             g1.append(l1)
#         else:
#             grid.append(g1)
#             g1 = []

# print(grid)



# Simulating from a text file of test cases

from l1 import YantraCollector


def load_grids(f_name):
    with open(f_name, 'r') as f:
        lines = f.readlines()
        grids = []
        curr_str = ''
        for line in lines:
            if line != '\n':
                curr_str += line
            else:
                grids.append(curr_str)
                curr_str = ''

        out = [[i.strip('\n').split('\t') for i in g.split('\n') if i != ''] for g in grids]
        return out
            


def simulate(f_name, strat):
    gs = load_grids(f_name)
    for g in gs:
        game = YantraCollector(g)
        strategy = strat
        solution, total_frontier, total_explored = game.solve(strategy)
        if solution:
            print("Solution Path:", solution)
            print("Total Frontier Nodes:", total_frontier)
            print("Total Explored Nodes:", total_explored)
        else:
            print("No solution found.")
        print('\n')


simulate('cases_1000.txt', 'BFS')