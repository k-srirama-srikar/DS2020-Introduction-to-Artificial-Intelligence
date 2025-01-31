# Simulating from a text file of test cases
import importlib.util
import sys

file_path = './142301013.py'

# Load the module dynamically
spec = importlib.util.spec_from_file_location("TreeModule", file_path)
tree_module = importlib.util.module_from_spec(spec)
sys.modules["TreeModule"] = tree_module
spec.loader.exec_module(tree_module)

YantraCollector = tree_module.YantraCollector


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