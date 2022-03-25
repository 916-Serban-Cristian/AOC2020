from copy import copy


class Equation:
    def __init__(self, multiple, remainder):
        self.multiple = multiple
        self.remainder = remainder

    def __repr__(self):
        return "x = {0} * const + {1}".format(self.multiple, self.remainder)


def get_input(bus_list):
    with open("input.txt") as f:
        f.readline()
        buses = f.readline().split(',')
        for bus in buses:
            if bus != 'x':
                bus_list.append(int(bus))
            else:
                bus_list.append(bus)


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

        # Make x positive
    if (x < 0):
        x = x + m0

    return x


def main():
    current_time = 0
    bus_list = []
    get_input(bus_list)
    equations = [Equation(bus_list[0], 0)]
    for idx, bus in enumerate(bus_list[1:]):
        if bus != 'x':
            last_eq = equations[-1]

    print(equations)


main()
