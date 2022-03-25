def main():
    ticket_fields = {}
    eror_rate = 0
    with open("input.txt") as f:
        input_lines = f.read()
    input_lines = input_lines.split('\n\n')
    fields = input_lines[0].split('\n')
    for line in fields:
        name = line.split(':')[0].strip()
        range1 = line.split(':')[1].strip().split()[0].split('-')
        range2 = line.split(':')[1].strip().split()[-1].split('-')
        ticket_fields[name] = (range(int(range1[0]), int(range1[1]) + 1), range(int(range2[0]), int(range2[1]) + 1))
    nearby_tickets = input_lines[-1].split('\n')[1:]
    for ticket in nearby_tickets:
        values = ticket.split(',')
        for value in values:
            value = int(value)
            valid = False
            for field in ticket_fields:
                for value_range in ticket_fields[field]:
                    if value in value_range:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                eror_rate += value

    print(eror_rate)


main()
