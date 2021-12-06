import collections

def next_day(d: dict[int:int]):
    ret = collections.defaultdict(lambda: 0)

    for (k, v) in d.items():
        if k == 0:
            ret[8] = ret[8] + v
            ret[6] = ret[6] + v
        else:
            ret[k-1] = ret[k-1] + v
    return ret


def part1():
    f = open("input.txt", "r")

    nums = [int(c) for c in [x.rstrip() for x in f][0].split(',')]

    num_count = collections.defaultdict(lambda: 0)
    for n in nums:
        num_count[n] = num_count[n] + 1

    for i in range(80):
        num_count = next_day(num_count)

    return sum(num_count.values())


def part2():
    f = open("input.txt", "r")

    nums = [int(c) for c in [x.rstrip() for x in f][0].split(',')]

    num_count = collections.defaultdict(lambda: 0)
    for n in nums:
        num_count[n] = num_count[n] + 1

    for i in range(256):
        num_count = next_day(num_count)

    return sum(num_count.values())


if __name__ == '__main__':

    print(part1())
    print(part2())
