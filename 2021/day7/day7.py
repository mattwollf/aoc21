import collections


def next_day(d: dict[int:int]):
    ret = collections.defaultdict(lambda: 0)

    for (k, v) in d.items():
        if k == 0:
            ret[8] = v
            ret[6] = ret[6] + v
        else:
            ret[k-1] = ret[k-1] + v
    return ret


def next_day_generator(d: dict[int:int]):
    ret = collections.defaultdict(lambda: 0)

    ret[8] = d[0]
    ret[6] = ret[6] + d[0]

    for (k, v) in (x for x in d.items() if x[0] != 0):
        ret[k-1] = ret[k-1] + v
    return ret


def next_day_arr(fish):
    reset = fish[0]
    fish[0] = 0
    for c in range(1, 9):
        fish[c-1] = fish[c]

    fish[8] = reset
    fish[6] = fish[6] + reset
    return fish


def part1_arr():
    f = open("input.txt", "r")

    nums = [int(c) for c in [x.rstrip() for x in f][0].split(',')]

    fish = [0] * 9

    for days_left in nums:
        fish[days_left] += 1

    for _ in range(80):
        next_day_arr(fish)
    return sum(fish)


def part2_arr(init):
    fish_buckets = [0] * 9

    for i in init:
        fish_buckets[i] += 1

    for _ in range(256):
        births = fish_buckets[0]

        fish_buckets = fish_buckets[1:9] + [births]
        fish_buckets[6] = fish_buckets[6] + births

    return sum(fish_buckets)


def part1():
    f = open("input.txt", "r")

    nums = [int(c) for c in [x.rstrip() for x in f][0].split(',')]

    num_count = collections.defaultdict(lambda: 0)
    for n in nums:
        num_count[n] = num_count[n] + 1

    for i in range(80):
        num_count = next_day(num_count)

    return sum(num_count.values())


def part2(nums):
    num_count = collections.defaultdict(lambda: 0)
    for n in nums:
        num_count[n] = num_count[n] + 1

    for _ in range(256):
        # num_count = next_day_generator(num_count)
        num_count = next_day(num_count)

    return sum(num_count.values())


def count(f, n=10000):
    import time
    start = time.time()
    for _ in range(n):
        f()
    end = time.time()
    print((end-start) / n)


if __name__ == '__main__':

    f = open("input.txt", "r")

    initial = [int(c) for c in [x for x in f][0].split(',')]
    f.close()
    print(part2(initial))
    print(part2_arr(initial))

    rerun = 10000
    count(lambda: part2(initial))
    count(lambda: part2_arr(initial), rerun)

