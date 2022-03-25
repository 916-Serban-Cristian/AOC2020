from level1 import determine_seat, get_max_id

with open("input.txt") as f:
    boarding_passes = []
    for line in f:
        boarding_passes.append(line)
    seats = {}
    max_id = get_max_id()
    my_seat = None
    for i in range(0, max_id + 1):
        seats[i] = False
    for boarding_pass in boarding_passes:
        seat = determine_seat(boarding_pass)
        seats[seat[2]] = True
    for seat in seats:
        if seat == 0:
            continue
        if seats[seat] is False:
            if seats[seat - 1] is True and seats[seat + 1] is True:
                my_seat = seat
                break
print(my_seat)
