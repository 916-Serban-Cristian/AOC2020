def main():
    f = open("input.txt")
    invalid_number = 400480901
    sequence = []
    while sum(sequence) != invalid_number:
        sequence.append(int(f.readline()))
        while sum(sequence) > invalid_number:
            sequence.pop(0)
    print(min(sequence)+max(sequence))


main()
