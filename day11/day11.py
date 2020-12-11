IN_FILE = 'day11-input.txt'
FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def get_input(in_file: str) -> list:
    with open(in_file) as f:
        return [x.replace('\n', '') for x in f.readlines()]


def get_valid_range(coord: int, upper_bound: int) -> list:
    if coord == 0:
        return [coord, coord+1]
    elif coord == upper_bound:
        return [coord-1, coord]
    else:
        return [coord-1, coord, coord+1]


def update_seat(old_layout: list, coords: tuple) -> str:

    y, x = coords[0], coords[1]
    seat = old_layout[y][x]

    adj = ''
    y_range = get_valid_range(y, len(old_layout)-1)
    x_range = get_valid_range(x, len(old_layout[0])-1)

    for _y in y_range:
        for _x in x_range:
            if (_y, _x) != coords:
                adj += old_layout[_y][_x]
    if seat == EMPTY:
        return OCCUPIED if adj.count(OCCUPIED) == 0 else EMPTY
    elif seat == OCCUPIED:
        return EMPTY if adj.count(OCCUPIED) >= 4 else OCCUPIED
    else:
        return FLOOR


def update_seat_layout(seat_layout: list) -> list:
    new_layout = list()
    for i in range(len(seat_layout)):
        new_layout.append('')
        for j in range(len(seat_layout[i])):
            new_layout[i] += update_seat(seat_layout, (i, j))
    return new_layout


DELTAS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def update_seat_part_2(old_layout: list, coords: tuple, sizes: tuple) -> str:
    i, j = coords[0], coords[1]
    height, width = sizes[0], sizes[1]
    seat = old_layout[i][j]
    adj_count = 0
    for di, dj in DELTAS:
        ai, aj = i + di, j + dj
        if 0 <= ai < height and 0 <= aj < width:
            while old_layout[ai][aj] == '.':
                if 0 <= ai+di < height and 0 <= aj+dj < width:
                    ai += di
                    aj += dj
                else:
                    break
            if old_layout[ai][aj] == OCCUPIED:
                adj_count += 1

    if seat == EMPTY:
        return OCCUPIED if adj_count == 0 else EMPTY
    elif seat == OCCUPIED:
        return EMPTY if adj_count >= 5 else OCCUPIED
    else:
        return FLOOR


def update_seat_layout_part_2(seat_layout: list) -> list:
    new_layout = list()
    height = len(seat_layout)
    width = len(seat_layout[0])
    for i in range(height):
        new_layout.append('')
        for j in range(width):
            new_layout[i] += update_seat_part_2(seat_layout, (i, j), (height, width))
    return new_layout


def main():
    starting_seat_layout = get_input(IN_FILE)

    seat_layout_part1 = list(map(str, starting_seat_layout))
    while True:
        updated_seat_layout = update_seat_layout(seat_layout_part1)

        if updated_seat_layout == seat_layout_part1:
            seat_layout_part1 = updated_seat_layout
            break
        else:
            seat_layout_part1 = updated_seat_layout
    part1_count = sum([x.count(OCCUPIED) for x in seat_layout_part1])
    print(part1_count)

    seat_layout_part2 = list(map(str, starting_seat_layout))
    while True:
        updated_seat_layout = update_seat_layout_part_2(seat_layout_part2)

        if updated_seat_layout == seat_layout_part2:
            seat_layout_part2 = updated_seat_layout
            break
        else:
            seat_layout_part2 = updated_seat_layout
    part2_count = sum([x.count(OCCUPIED) for x in seat_layout_part2])
    print(part2_count)


if __name__ == '__main__':
    main()
