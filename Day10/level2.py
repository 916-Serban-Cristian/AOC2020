from functools import cache


@cache
def generate_arrangements(position):
    if position == len(adapters) - 1:
        return 1
    total_arrangements = 0
    for i in range(position + 1, min(position + 4, len(adapters))):
        if adapters[i] - adapters[position] <= 3:
            total_arrangements += generate_arrangements(i)
    return total_arrangements


def main():
    with open("input.txt") as f:
        for line in f:
            adapters.append(int(line))
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    print(generate_arrangements(0))


adapters = [0]
main()
