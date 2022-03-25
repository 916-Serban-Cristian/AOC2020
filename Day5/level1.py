def determine_seat(boarding_pass):
    row_min = 0
    row_max = 127
    for i in range(7):
        if boarding_pass[i] == "F":
            row_max = int((row_max + row_min) / 2)
        else:
            row_min = int((row_max + row_min + 1) / 2)
    col_min = 0
    col_max = 7
    for i in range(7, 10):
        if boarding_pass[i] == "L":
            col_max = int((col_max + col_min) / 2)
        else:
            col_min = int((col_max + col_min + 1) / 2)
    return row_max, col_max, row_max * 8 + col_max


def get_max_id():
    with open("input.txt") as f:
        boarding_passes = []
        for line in f:
            boarding_passes.append(line)
        max_id = 0
        for boarding_pass in boarding_passes:
            seat = determine_seat(boarding_pass)
            if seat[2] > max_id:
                max_id = seat[2]
    return max_id
