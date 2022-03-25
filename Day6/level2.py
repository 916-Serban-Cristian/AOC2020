f = open("input.txt")
group_answers = f.read().split('\n\n')
total_yes = 0
for group in group_answers:
    persons = group.split('\n')
    group_yes_frequency = [0] * 26
    for person in persons:
        for question in person:
            group_yes_frequency[ord(question) - ord('a')] += 1
    for freq in group_yes_frequency:
        if freq == len(persons):
            total_yes += 1
print(total_yes)
