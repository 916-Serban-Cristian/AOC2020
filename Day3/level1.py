f = open("input.txt", "r")
lines = f.read().split('\n')
tree_map = []
for line in lines:
    tree_map.append(line.strip())
i, j = 0, 0
right_slope = 3
down_slope = 1
nr_trees = 0
line_len = len(tree_map[0])
while i < len(tree_map):
    if tree_map[i][j] == '#':
        nr_trees += 1
    i += down_slope
    j = (j + right_slope) % line_len
print(nr_trees)
