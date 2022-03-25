import pickle


def main():
    try:
        with open("data.pickle", "rb") as data:
            counting_sequence = pickle.load(data)
            current_number = pickle.load(data)
            last_number = pickle.load(data)
    except EOFError:
        with open("input.txt") as f:
            starting_sequence = f.read().split(',')
        counting_sequence = {}
        for idx, number in enumerate(starting_sequence):
            counting_sequence[int(number)] = [int(idx + 1)]
        current_number = len(counting_sequence) + 1
        last_number = int(starting_sequence[-1])

    while current_number <= 30000000:
        if current_number % 1000000 == 0:
            print(current_number)
            with open("data.pickle", "wb") as data:
                pickle.dump(counting_sequence, data)
                pickle.dump(current_number, data)
                pickle.dump(last_number, data)
        number_to_speak = 0 if len(counting_sequence[last_number]) == 1 else counting_sequence[last_number][-1] - \
                                                                             counting_sequence[last_number][-2]
        if number_to_speak in counting_sequence:
            counting_sequence[number_to_speak].append(current_number)
        else:
            counting_sequence[number_to_speak] = [current_number]
        last_number = number_to_speak
        current_number += 1
    print("Found!", last_number)


main()
