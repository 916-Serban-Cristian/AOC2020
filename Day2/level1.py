f = open("input.txt", "r")
lines = f.read().split('\n')
counter = 0
for line in lines:
    line = line.strip().split()
    bounds = line[0].split('-')
    lower_bound = int(bounds[0])
    upper_bound = int(bounds[1])
    char_to_search = line[1][0]
    password = line[2]
    appearances = password.count(char_to_search)
    if lower_bound <= appearances <= upper_bound:
        counter += 1
print(counter)