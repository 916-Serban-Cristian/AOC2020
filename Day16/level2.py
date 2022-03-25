def main():
    ticket_fields = {}

    with open("input.txt") as f:
        input_lines = f.read()
    input_lines = input_lines.split('\n\n')
    fields = input_lines[0].split('\n')
    for line in fields:
        name = line.split(':')[0].strip()
        range1 = line.split(':')[1].strip().split()[0].split('-')
        range2 = line.split(':')[1].strip().split()[-1].split('-')
        ticket_fields[name] = (range(int(range1[0]), int(range1[1]) + 1), range(int(range2[0]), int(range2[1]) + 1))

    my_ticket = input_lines[1].split('\n')[1:]
    my_ticket = my_ticket[0].split(',')

    nearby_tickets = input_lines[-1].split('\n')[1:]
    valid_tickets = set()
    for ticket in nearby_tickets:
        values = ticket.split(',')
        valid_ticket = True
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
                valid_ticket = False
        if valid_ticket:
            valid_tickets.add(ticket)

    field_order = [[]] * len(my_ticket)
    for ticket in valid_tickets:
        ticket_values = ticket.split(',')
        for idx, value in enumerate(ticket_values):
            value = int(value)
            for field in ticket_fields:
                for value_range in ticket_fields[field]:
                    if value in value_range:
                        field_order[idx].append(field)

    for field_list in field_order:
        max_occur, max_field = 0, None
        for field in ticket_fields:
            nr = field_list.count(field)
            print(nr)
            if nr > max_occur:
                max_occur = nr
                max_field = field
        print(max_field, max_occur)


main()
