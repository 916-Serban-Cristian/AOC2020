def get_input(bus_list):
    with open("input.txt") as f:
        my_time = int(f.readline())
        buses = f.readline().split(',')
        for bus in buses:
            if bus != 'x':
                bus_list.append(int(bus))
    return my_time


def main():
    bus_list = []
    my_time = get_input(bus_list)
    elapsed_minutes = 0
    my_bus = None
    departed = False
    while not departed:
        for bus in bus_list:
            if (my_time + elapsed_minutes) % bus == 0:
                departed = True
                my_bus = bus
                break
        elapsed_minutes += 1
    elapsed_minutes -= 1
    print(elapsed_minutes * my_bus)


main()
