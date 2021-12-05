
def part1():
    f = open("input.txt", "r")

    lines = [x.rstrip() for x in f]

    points = [x.split(' -> ') for x in lines]
    print(points[0:5])

    split_points = [[list(map(int, x[0].split(','))), list(map(int, x[1].split(',')))] for x in points]

    print(split_points[0:5])


def part2():
    f = open("input.txt", "r")

    lines = [x.rstrip() for x in f]


if __name__ == '__main__':
    part1()
    part2()
