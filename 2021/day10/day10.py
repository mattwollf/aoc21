import collections

ctoo = {x[1]: x[0] for x in zip('([{<', ')]}>')}
otoc = {x[0]: x[1] for x in zip('([{<', ')]}>')}


def syntax_score(line):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    stack = collections.deque()

    for c in line:
        if c in ctoo.values():
            stack.append(c)
        elif c in ctoo.keys():
            if stack[-1] == ctoo[c]:
                stack.pop()
            else:
                return points[c]
    return 0 if len(stack) == 0 else -len(stack)


def part1(lines):
    score = 0

    for line in lines:
        score += syntax_score(line)

    return score


def get_stack(line):
    stack = collections.deque()
    for c in line:
        if c in ctoo.values():
            stack.append(c)
        elif c in ctoo.keys():
            if stack[-1] == ctoo[c]:
                stack.pop()
            else:
                return stack

    return stack


def part2(lines):

    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    incomplete = [x for x in lines if syntax_score(x) < 0]

    stacks = [get_stack(x) for x in incomplete]

    scores = []
    for s in stacks:
        score = 0
        for tok in reversed(s):
            score *= 5
            score += points[otoc[tok]]

        scores.append(score)

    scores.sort()
    middle = len(scores) // 2
    return scores[middle]


def tests():
    p1 = part1(parse_input('sample.txt'))
    print('{0}==26397'.format(p1))
    p2 = part2(parse_input('sample.txt'))
    print('{0}==288957'.format(p2))


def parse_input(name):
    return [x.strip() for x in open(name, 'r').readlines()]


if __name__ == '__main__':
    tests()
    print(part1(parse_input('input.txt')))
    print(part2(parse_input('input.txt')))

    # print(part2())
