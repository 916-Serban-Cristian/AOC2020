def main():
    adapters = [0]
    with open("input.txt") as f:
        for line in f:
            adapters.append(int(line))
    adapters.sort()
    diff_1, diff_3 = 0, 1
    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] == 1:
            diff_1 += 1
        elif adapters[i + 1] - adapters[i] == 3:
            diff_3 += 1
    print(diff_1 * diff_3)


main()
