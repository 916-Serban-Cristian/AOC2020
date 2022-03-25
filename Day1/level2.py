f = open("input.txt", "r")
lines = f.read().split("\n")
expenses = []
for line in lines:
    expenses.append(int(line.strip()))
for i in range(len(expenses) - 1):
    s = set()
    current_sum = 2020 - expenses[i]
    for j in range(i + 1, len(expenses)):
        if current_sum - expenses[j] in s:
            print(expenses[i] * expenses[j] * (current_sum - expenses[j]))
        s.add(expenses[j])
