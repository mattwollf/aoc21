
def winning(b: list[list[(int, bool)]]):
    if not b:
        return False
    horizontal = any([all([x[1] for x in r]) for r in b])
    rotated = [[r[i] for r in b] for i in range(5)]
    vertical = any([all([x[1] for x in r]) for r in rotated])

    diagonal = (b[0][0][1] and b[1][1][1] and b[2][2][1] and b[3][3][1] and b[4][4][1]) \
        or (b[4][0][1] and b[3][1][1] and b[2][2][1] and b[1][3][1] and b[0][4][1])

    return horizontal or vertical or diagonal


def mark(b: list[list[(int, bool)]], n: int):
    for r in b:
        for c in r:
            if c[0] == n:
                c[1] = True
                return b
    return b


def score(b: list[list[(int, bool)]]):
    if not b:
        return False
    unmarked = [c for r in b for c in r if not c[1]]
    return sum([x[0] for x in unmarked])


def part1():
    f = open("input.txt", "r")

    lines = [x.rstrip() for x in f]
    draws = [int(x) for x in lines[0].split(',')]

    boards = []

    board = []
    for i in range(2, len(lines)):
        line = lines[i]
        if line:
            splitline = line.split()
            board.append([[int(x), False] for x in splitline])
        else:
            boards.append(board)
            board = []

    for n in draws:
        for b in boards:
            mark(b, n)
            if winning(b):
                print(score(b) * n)
                return


def part2():
    f = open("input.txt", "r")

    lines = [x.rstrip() for x in f]
    draws = [int(x) for x in lines[0].split(',')]

    boards = []

    board = []
    for i in range(2, len(lines)):
        line = lines[i]
        if line:
            splitline = line.split()
            board.append([[int(x), False] for x in splitline])
        else:
            boards.append(board)
            board = []

    last = None
    for n in draws:
        for b in boards:
            mark(b, n)
        in_play = [a for a in boards if not winning(a)]
        if 1 == len(in_play):
            last = in_play[0]
        if winning(last):
            print(score(last) * n)
            return


if __name__ == '__main__':
    part1()
    part2()
