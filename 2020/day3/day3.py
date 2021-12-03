def part1():
    f = open("input.txt", "r")

    lines = f.readlines()
    lines = list(map(lambda x: x.rstrip(), lines))

    for i in range(len(lines)):
        lines[i] = lines[i] * 500

    position = (0, 0)

    moves = [
        lambda x: (x[0] + 1, x[1]),
        lambda x: (x[0] + 1, x[1]),
        lambda x: (x[0] + 1, x[1]),
        lambda x: (x[0], x[1] + 1),

    ]

    encountered_trees = 0

    height = len(lines)

    while position[1] < height - 1:

        x, y = position

        for f in moves:
            position = f(position)
            row = lines[position[1]]
            y = row[position[0]]
        if y == '#':
            encountered_trees += 1

    print(encountered_trees)


def part2():

    def right1(xy):
        return xy[0] + 1, xy[1]

    def down1(xy):
        return xy[0], xy[1] + 1

    f = open("input.txt", "r")

    lines = f.readlines()
    lines = list(map(lambda x: x.rstrip(), lines))

    for i in range(len(lines)):
        lines[i] = lines[i] * 500

    moves = [
        [
            right1,
            down1
        ],
        [
            right1,
            right1,
            right1,
            down1,
        ],
        [
            right1,
            right1,
            right1,
            right1,
            right1,
            down1
        ],
        [
            right1,
            right1,
            right1,
            right1,
            right1,
            right1,
            right1,
            down1
        ],
        [
            right1,
            down1,
            down1
        ]
    ]

    treecnt = []

    for slope in moves:

        position = (0, 0)

        encountered_trees = 0

        height = len(lines)

        while position[1] < height - 1:

            x, y = position

            for f in slope:
                position = f(position)
                row = lines[position[1]]
                y = row[position[0]]
            if y == '#':
                encountered_trees += 1

        treecnt.append(encountered_trees)

    from functools import reduce
    from operator import mul
    print(reduce(mul, treecnt))


if __name__ == "__main__":
    part1()
    part2()
