def binary_row(s):
    from math import ceil, floor
    lower, upper = 0, 127

    binary_fb = s[:7]
    for c in binary_fb:
        if c == 'F':
            upper = floor(upper - ((upper - lower) / 2))
        elif c == 'B':
            lower = ceil(lower + ((upper - lower) / 2))
        else:
            raise Exception("wtf")

    return lower


def binary_column(s):
    from math import ceil, floor
    lower, upper = 0, 7

    binary_lr = s[7:]
    for c in binary_lr:
        if c == 'L':
            upper = floor(upper - ((upper - lower) / 2))
        elif c == 'R':
            lower = ceil(lower + ((upper - lower) / 2))
        else:
            raise Exception("wtf")

    return lower


def seat_id(s):
    return 8 * binary_row(s) + binary_column(s)


def part1():
    f = open("input.txt", "r")

    high = 0
    for line in f:
        high = max(high, seat_id(line.rstrip()))

    print(high)

def part2():
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

    positions = [(binary_column(n), binary_row(n)) for n in lines]
    ids = [seat_id(n) for n in lines]

    import copy
    row = [None, None, None, None, None, None, None, None]
    seats = []
    for i in range(128):
        seats.append(copy.deepcopy(row))

    for i in range(len(positions)):
        p = positions[i]
        id = ids[i]
        x = p[0]
        y = p[1]
        seats[y][x] = id

    print(seats)



if __name__ == "__main__":
    part1()
    part2()
