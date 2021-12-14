def fold(coords, axis, v):
    d = {
        'y': lambda: fold_up(coords, v),
        'x': lambda: fold_left(coords, v),
    }
    return d[axis]()


def fold_up(coords, y):
    top = coords[:y]
    bottom_folded = coords[y+1:][::-1]

    result = []

    toplen = len(top)
    botlen = len(bottom_folded)

    ymin = min(toplen, botlen)

    for y1 in range(0, ymin):
        top_row = top[toplen - y1 - 1]
        bottom_row = bottom_folded[botlen - y1 - 1]
        resultrow = []
        for x1 in range(len(top_row)):
            resultrow.append('#' if top_row[x1] == '#' or bottom_row[x1] == '#' else '.')
        result.append(resultrow)

    return list(reversed(result))


def fold_left(coords, x):
    left = [l[:x] for l in coords]
    right = [l[x+1:][::-1] for l in coords]

    leftlen = len(left[0])
    rightlen = len(right[0])

    lenmin = min(leftlen, rightlen)

    result = []

    for y1 in range(0, len(left)):
        left_row = left[y1]
        right_row = right[y1]
        resultrow = []
        for x1 in range(0, lenmin):
            resultrow.append('#' if left_row[x1] == '#' or right_row[x1] == '#' else '.')
        result.append(resultrow)

    return result


def part1(cf):
    paper = cf[0]
    for i in cf[1][:1]:
        paper = fold(paper, i[0], i[1])

    return sum(x.count('#') for x in paper)


def part2(cf):
    paper = cf[0]
    for i in cf[1]:
        paper = fold(paper, i[0], i[1])

    return paper


def parse_input(name):
    coords = [x.strip() for x in open(name, 'r').readlines()]

    idx = coords.index('')
    coords, folds = coords[:idx], coords[idx+1:]
    coords = [x.split(',') for x in coords]
    coords = [(int(x[0]), int(x[1])) for x in coords]

    folds = [x.strip('fold along').split('=') for x in folds]
    folds = [(x[0], int(x[1])) for x in folds]

    xmax = max(coords, key=lambda x: x[0])[0] + 1
    ymax = max(coords, key=lambda x: x[1])[1] + 1

    def rowmaker(xmax):
        return ['.'] * xmax
    board = [rowmaker(xmax) for _ in range(ymax)]

    for c in coords:
        board[c[1]][c[0]] = '#'

    return board, folds


def tests():
    p1 = part1(parse_input('sample.txt'))
    print('{0}==17'.format(p1))


if __name__ == '__main__':
    tests()
    print(part1(parse_input('input.txt')))
    print(*part2(parse_input('input.txt')), sep='\n')

