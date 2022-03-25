f = open("input.txt", "r")
lines = f.read().split('\n')
tree_map = []
for line in lines:
    tree_map.append(line.strip())


def count_trees(right_slope, down_slope):
    i, j = 0, 0
    nr_trees = 0
    line_len = len(tree_map[0])
    while i < len(tree_map):
        if tree_map[i][j] == '#':
            nr_trees += 1
        i += down_slope
        j = (j + right_slope) % line_len
    return nr_trees


tree_product = count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2)
print(tree_product)