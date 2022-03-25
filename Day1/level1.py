f = open("input.txt", "r")
expenses = []
lines = f.read().split('\n')
for line in lines:
    expenses.append(int(line.strip()))
for expense in expenses:
    if 2020 - expense in expenses:
        print(expense * (2020 - expense))
