
def part1():
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

    groups = []

    from collections import defaultdict
    group = defaultdict(lambda: 0)
    for line in lines:
        if not line:
            groups.append(group)
            group = defaultdict(lambda: 0)
            continue

        for c in line:
            group[c] += 1

    print(sum([len(x) for x in groups]))


def part2():
    import string
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

    all_counts = []

    all_answered = set(string.ascii_lowercase)
    for line in lines:
        if not line:
            all_counts.append(len(all_answered))
            all_answered = set(string.ascii_lowercase)
            continue

        all_answered = all_answered.intersection(set(line))

    print(sum(all_counts))

if __name__ == "__main__":
    part1()
    part2()
