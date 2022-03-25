class Ship:
    def __init__(self):
        self.direction = 0
        self.x_coord = 0
        self.y_coord = 0

    def turn_left(self, degrees):
        self.direction = (self.direction - degrees) % 360

    def turn_right(self, degrees):
        self.direction = (self.direction + degrees) % 360

    def move_forward(self, units):
        if self.direction == 0:
            self.move_east(units)
        elif self.direction == 90:
            self.move_north(units)
        elif self.direction == 180:
            self.move_west(units)
        elif self.direction == 270:
            self.move_south(units)

    def move_east(self, units):
        self.x_coord += units

    def move_north(self, units):
        self.y_coord += units

    def move_west(self, units):
        self.x_coord -= units

    def move_south(self, units):
        self.y_coord -= units

    def __str__(self):
        return "Direction={0}  x_coord={1}  y_coord={2}".format(self.direction, self.x_coord, self.y_coord)


def main():
    ship = Ship()
    directions = {'E': ship.move_east, 'N': ship.move_north, 'W': ship.move_west, 'S': ship.move_south,
                  'F': ship.move_forward}
    turns = {'L': ship.turn_left, 'R': ship.turn_right}
    with open("input.txt") as f:
        for line in f:
            action = line[0]
            value = int(line[1:])
            if action in directions:
                directions[action](value)
            elif action in turns:
                turns[action](value)
    print(abs(ship.x_coord) + abs(ship.y_coord))


main()
