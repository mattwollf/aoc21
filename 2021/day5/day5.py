import collections
import itertools


def part1():
    f = open("input.txt", "r")

    lines = [x.rstrip() for x in f]

    points = [x.split(' -> ') for x in lines]
    points = [[list(map(int, x[0].split(','))), list(map(int, x[1].split(',')))] for x in points]

    ys = (v[1] for pair in points for v in pair)

    max_y = max(ys) + 5

    horv = [p for p in points if p[0][0] == p[1][0] or p[0][1] == p[1][1]]

    b = collections.defaultdict(lambda: 0)

    for vector in horv:
        src, dest = vector
        xrange = range(min(src[0], dest[0]), max(src[0], dest[0]) + 1)
        yrange = range(min(src[1], dest[1]), max(src[1], dest[1]) + 1)

        if len(xrange) == 1:
            xrange = itertools.cycle(xrange)
        elif len(yrange) == 1:
            yrange = itertools.cycle(yrange)
        for x, y in zip(xrange, yrange):
            i = max_y * y + x
            b[i] = b[i] + 1

    print(len(list(filter(lambda kv: kv[1] > 1, b.items()))))


def part2():
    f = open("input.txt", "r")

    lines = [x.rstrip() for x in f]

    points = [x.split(' -> ') for x in lines]
    points = [[list(map(int, x[0].split(','))), list(map(int, x[1].split(',')))] for x in points]

    max_y = max(v[1] for pair in points for v in pair) + 5

    horv_pred = lambda p: p[0][0] == p[1][0] or p[0][1] == p[1][1]
    horv = [p for p in points if horv_pred(p)]
    diag = [p for p in points if not horv_pred(p)]

    b = collections.defaultdict(lambda: 0)

    for vector in horv:
        src, dest = vector
        xrange = range(min(src[0], dest[0]), max(src[0], dest[0]) + 1)
        yrange = range(min(src[1], dest[1]), max(src[1], dest[1]) + 1)

        if len(xrange) == 1:
            xrange = itertools.cycle(xrange)
        elif len(yrange) == 1:
            yrange = itertools.cycle(yrange)
        for x, y in zip(xrange, yrange):
            i = max_y * y + x
            b[i] = b[i] + 1

    for vector in diag:
        first = min(vector, key=lambda x: x[0])
        second = max(vector, key=lambda x: x[0])

        x1, y1 = first
        x2, y2 = second

        slope = 1 if y2 >= y1 else -1

        y2 = y2 + 1 if slope == 1 else y2 - 1

        xrange = range(x1, x2 + 1)
        yrange = range(y1, y2, slope)

        points = list(zip(xrange, yrange))
        for x, y in points:
            i = max_y * y + x
            b[i] = b[i] + 1

    print(len(list(filter(lambda kv: kv[1] > 1, b.items()))))


if __name__ == '__main__':
    part1()
    part2()
