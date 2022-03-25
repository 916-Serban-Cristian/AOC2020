f = open("input.txt")
group_answers = f.read().split('\n\n')
total_yes = 0
for group in group_answers:
    persons = group.split('\n')
    group_yes = set()
    for person in persons:
        for question in person:
            if question not in group_yes:
                group_yes.add(question)
    total_yes += len(group_yes)
print(total_yes)