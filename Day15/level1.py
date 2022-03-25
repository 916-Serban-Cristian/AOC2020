from dataclasses import dataclass


@dataclass
class CountingNumbers:
    value: int
    appearances: list


def main():
    with open("input.txt") as f:
        starting_sequence = f.read().split(',')
    counting_sequence = list(CountingNumbers(int(value), [idx+1]) for idx, value in enumerate(starting_sequence))
    current_number = len(counting_sequence) + 1
    last_number = counting_sequence[-1]
    while current_number <= 2020:
        if len(last_number.appearances) == 1:
            found = False
            for number in counting_sequence:
                if number.value == 0:
                    number.appearances.append(current_number)
                    last_number = number
                    found = True
                    break
            if not found:
                counting_sequence.append(CountingNumbers(0, [current_number]))
                last_number = counting_sequence[-1]
        else:
            number_to_speak = last_number.appearances[-1] - last_number.appearances[-2]
            found = False
            for number in counting_sequence:
                if number.value == number_to_speak:
                    number.appearances.append(current_number)
                    last_number = number
                    found = True
                    break
            if not found:
                counting_sequence.append(CountingNumbers(number_to_speak, [current_number]))
                last_number = counting_sequence[-1]
        current_number += 1
    print("Found!", last_number.value)


main()
