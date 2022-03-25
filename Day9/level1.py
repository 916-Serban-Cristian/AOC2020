def is_sum(preamble, number_to_check):
    for number in preamble:
        if number_to_check - number in preamble:
            return True
    return False


def main():
    preamble = [0] * 25
    f = open("input.txt")
    for i in range(len(preamble)):
        preamble[i] = int(f.readline())
    found = None
    while found is None:
        current_number = int(f.readline())
        if not is_sum(preamble, current_number):
            found = current_number
        else:
            preamble.pop(0)
            preamble.append(current_number)
    print(found)


main()
