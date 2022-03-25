f = open("input.txt", "r")
lines = f.read().split('\n')
counter = 0
for line in lines:
    line = line.strip().split()
    positions = line[0].split('-')
    lower_position = int(positions[0]) - 1
    upper_position = int(positions[1]) - 1
    char_to_search = line[1][0]
    password = line[2]
    if password[lower_position] == char_to_search and password[upper_position] != char_to_search:
        counter += 1
    if password[upper_position] == char_to_search and password[lower_position] != char_to_search:
        counter += 1
print(counter)
