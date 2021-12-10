import collections


def part1(lines):

    low_points = get_low_points(lines)
    risks = [int(x[2]) + 1 for x in low_points]
    return sum(risks)


def get_low_points(lines):
    rows = len(lines)
    columns = len(lines[0])
    low_points = []
    for y in range(rows):
        for x in range(columns):
            if lowest(lines, y, x):
                low_points.append((y, x, lines[y][x]))
    return low_points


def adjacent(lines, y, x):
    result = []
    if y > 0:
        result.append((y-1, x, lines[y-1][x]))
    if y < len(lines) - 1:
        result.append((y+1, x, lines[y+1][x]))
    if x > 0:
        result.append((y, x-1, lines[y][x-1]))
    if x < len(lines[0]) - 1:
        result.append((y, x+1, lines[y][x+1]))
    return result


def lowest(lines, y, x):
    candidate = lines[y][x]
    adj = [x[2] for x in adjacent(lines, y, x)]
    return candidate not in adj and candidate == min([candidate] + adj)


def part2(lines):
    low_points = get_low_points(lines)

    basins = []
    for p in low_points:
        basin = set()
        q = collections.deque()
        q.append(p)
        while q:
            i = q.popleft()
            if i in basin:
                continue
            for x in adjacent(lines, i[0], i[1]):
                if int(x[2]) < 9 and x not in basin:
                    q.append(x)
            if int(i[2]) < 9:
                basin.add(i)
        basins.append(basin)

    a, b, c = list(reversed(sorted(basins, key=len)))[:3]

    return len(a) * len(b) * len(c)


def tests():
    p1 = part1(parse_input('sample.txt'))
    print('{0}==15'.format(p1))
    p2 = part2(parse_input('sample.txt'))
    print('{0}==1134'.format(p2))


def parse_input(name):
    return [x.strip() for x in open(name, 'r').readlines()]


if __name__ == '__main__':
    tests()
    print(part1(parse_input('input.txt')))
    print(part2(parse_input('input.txt')))

    # print(part2())
