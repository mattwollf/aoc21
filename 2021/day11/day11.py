import collections


def adjacent(arr, y, x):
    result = []
    y_pred_1 = y > 0
    x_pred_1 = x > 0
    y_pred_2 = y < len(arr) - 1
    x_pred_2 = x < len(arr[0]) - 1
    if y_pred_1:
        result.append((y - 1, x))
    if y_pred_2:
        result.append((y + 1, x))
    if x_pred_1:
        result.append((y, x - 1))
    if x_pred_2:
        result.append((y, x + 1))
    if y_pred_1 and x_pred_1:
        result.append((y - 1, x - 1))
    if y_pred_1 and x_pred_2:
        result.append((y - 1, x + 1))
    if y_pred_2 and x_pred_1:
        result.append((y + 1, x - 1))
    if y_pred_2 and x_pred_2:
        result.append((y + 1, x + 1))
    return result


def generator(arr, inc_queue):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            yield y, x

    while inc_queue:
        yield inc_queue.popleft()


def increment(arr):

    inc_q = collections.deque()
    banned = set()

    for y, x in generator(arr, inc_q):
        if (y, x) in banned:
            continue
        arr[y][x] += 1
        if arr[y][x] == 10:
            banned.add((y, x))
            arr[y][x] = 0
            for i in adjacent(arr, y, x):
                inc_q.append(i)

    return len(banned)


def part1(arr, n):

    flashes = [increment(arr) for _ in range(n)]

    return sum(flashes)


def part2(arr):

    goal = len(arr) * len(arr[0])

    def forever():
        yield True

    iterations = 0

    while increment(arr) != goal:
        iterations += 1

    return iterations + 1


def tests():
    p = part1(parse_input('baby_sample.txt'), 2)
    print('{0}==9'.format(p))
    p1 = part1(parse_input('sample.txt'), 100)
    print('{0}==1656'.format(p1))
    baby_p2 = part2(parse_input('baby_sample.txt'))
    print('{0}==195'.format(baby_p2))
    p2 = part2(parse_input('sample.txt'))
    print('{0}==195'.format(p2))


def parse_input(name):
    result = []

    for line in (x.strip() for x in open(name, 'r').readlines()):
        result.append([int(c) for c in line])

    return result


if __name__ == '__main__':
    tests()
    print(part1(parse_input('input.txt'), 100))
    print(part2(parse_input('input.txt')))

