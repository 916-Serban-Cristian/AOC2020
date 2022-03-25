from copy import deepcopy

from level1 import get_layout


def nr_of_adjacent_seats_occupied(layout, pos_x, pos_y):
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    seats = 0
    for i in range(8):
        next_x = pos_x + dx[i]
        next_y = pos_y + dy[i]
        while 0 < next_x < len(layout) and 0 < next_y < len(layout[next_x]):
            if layout[next_x][next_y] == "#":
                seats += 1
                break
            elif layout[next_x][next_y] == "L":
                break
            next_x += dx[i]
            next_y += dy[i]
    return seats


def main():
    layout = []
    get_layout(layout)
    finished = False
    while not finished:
        finished = True
        temp_layout = deepcopy(layout)
        for pos_x, line in enumerate(layout):
            for pos_y, seat in enumerate(line):
                if seat == "L":
                    if nr_of_adjacent_seats_occupied(layout, pos_x, pos_y) == 0:
                        temp_layout[pos_x] = temp_layout[pos_x][:pos_y] + "#" + temp_layout[pos_x][pos_y + 1:]
                        finished = False
                elif seat == "#":
                    if nr_of_adjacent_seats_occupied(layout, pos_x, pos_y) >= 5:
                        temp_layout[pos_x] = temp_layout[pos_x][:pos_y] + "L" + temp_layout[pos_x][pos_y + 1:]
                        finished = False
        layout = temp_layout
    final_seats = 0
    for line in layout:
        for seat in line:
            if seat == "#":
                final_seats += 1
    print(final_seats)


main()
