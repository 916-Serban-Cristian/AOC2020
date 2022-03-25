from level1 import get_input, Bag


def DFS(neighbour_list, bag, multiplier):
    global total_bags
    for neighbour in neighbour_list[bag.color]:
        total_bags += neighbour.count * multiplier
        multiplier *= neighbour.count
        DFS(neighbour_list, neighbour, multiplier)
        multiplier = int(multiplier / neighbour.count)


def main():
    neighbour_list = {}
    get_input(neighbour_list)
    DFS(neighbour_list, Bag("shiny gold", 1), 1)
    print(total_bags)


total_bags = 0
main()
