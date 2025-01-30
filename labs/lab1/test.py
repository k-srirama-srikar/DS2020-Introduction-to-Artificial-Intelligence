from l1 import YantraCollector

grid = []

with open('test-cases.txt', 'r+') as f:
    g1 = []
    # print(f)
    # print(f.readlines())
    for line in f.readlines():
        # print(line)
        l1 = line.strip()
        print(l1)
        if l1:
            g1.append(l1)
        else:
            grid.append(g1)
            g1 = []

print(grid)
