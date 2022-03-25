class Bag:
    def __init__(self, color, count):
        self.color = color
        self.count = count

    def __str__(self):
        return "Color: {0}; Count: {1}".format(self.color, self.count)

    def __repr__(self):
        return self.__str__()


def get_input(neighbour_list):
    with open("input.txt") as f:
        for line in f:
            words = line.split()
            name = words[0] + ' ' + words[1]
            neighbour_list[name] = []
            if words[4] != "no":
                for i in range(4, len(words), 4):
                    value = int(words[i])
                    neighbour_name = words[i + 1] + ' ' + words[i + 2]
                    bag = Bag(neighbour_name, value)
                    neighbour_list[name].append(bag)


def DFS(neighbour_list, color, nb):
    nb.append(color)
    for neighbour in neighbour_list[color]:
        if neighbour.color not in nb:
            DFS(neighbour_list, neighbour.color, nb)


def main():
    neighbour_list = {}
    get_input(neighbour_list)
    nr_gold_ways = 0
    for color in neighbour_list:
        if color == "shiny gold":
            continue
        nb = []
        DFS(neighbour_list, color, nb)
        if "shiny gold" in nb:
            nr_gold_ways += 1
    print(nr_gold_ways)
