class Waypoint:
    def __init__(self):
        self.x_relative_coord = 10
        self.y_relative_coord = 1

    def move_east(self, units):
        self.x_relative_coord += units

    def move_north(self, units):
        self.y_relative_coord += units

    def move_west(self, units):
        self.x_relative_coord -= units

    def move_south(self, units):
        self.y_relative_coord -= units

    def rotate_left(self):
        self.x_relative_coord, self.y_relative_coord = -self.y_relative_coord, self.x_relative_coord

    def rotate_right(self):
        self.x_relative_coord, self.y_relative_coord = self.y_relative_coord, -self.x_relative_coord

    def __str__(self):
        return "(x_rel_coord={0},y_rel_coord={1})".format(self.x_relative_coord, self.y_relative_coord)


class Ship:
    def __init__(self, waypoint):
        self.waypoint = waypoint
        self.x_coord = 0
        self.y_coord = 0

    def turn_left(self, degrees):
        while degrees != 0:
            self.waypoint.rotate_left()
            degrees -= 90

    def turn_right(self, degrees):
        while degrees != 0:
            self.waypoint.rotate_right()
            degrees -= 90

    def move_to_waypoint(self, units):
        self.x_coord += self.waypoint.x_relative_coord * units
        self.y_coord += self.waypoint.y_relative_coord * units

    def __str__(self):
        return "Waypoint={0}  x_coord={1}  y_coord={2}".format(self.waypoint, self.x_coord, self.y_coord)


def main():
    waypoint = Waypoint()
    ship = Ship(waypoint)
    directions = {'E': ship.waypoint.move_east, 'N': ship.waypoint.move_north, 'W': ship.waypoint.move_west,
                  'S': ship.waypoint.move_south, 'F': ship.move_to_waypoint}
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
