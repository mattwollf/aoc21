import collections


def get_bag(line: str):
    return " ".join(line.split(" ")[0:2])


def get_child_tuples(line: str):

    if 'no other bags' in line:
        return None

    rhs = line.split('contain ', 1)[1]
    tuples = rhs.split(', ')
    tuples = (tuple(x.split(' ', 1)) for x in tuples)
    tuples = [(int(x[0]), " ".join(x[1].split(' ')[0:2])) for x in tuples]

    return tuples


def part1():
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [line.rstrip(".\n") for line in lines]

    root_bags = {}

    for line in lines:
        key_bag = get_bag(line)
        child_tuples = get_child_tuples(line)
        root_bags[key_bag] = child_tuples

    bag_count = 0

    d = collections.deque()

    for k in root_bags:
        v = root_bags[k]
        if v is None:
            continue

        d.extend(v)

        while d:
            cur = d.popleft()
            if root_bags[cur[1]] is None:
                continue
            elif cur[1] == 'shiny gold':
                bag_count += 1
                d.clear()
            else:
                d.extend(root_bags[cur[1]])

    print(bag_count)


def recurse(root: dict, key: str, mult_state: int):

    entry = root[key]
    if entry is None:
        return mult_state

    return mult_state + sum([recurse(root, x[1], mult_state * x[0]) for x in entry])


def part2():
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [line.rstrip(".\n") for line in lines]

    root_bags = {}

    for line in lines:
        key_bag = get_bag(line)
        child_tuples = get_child_tuples(line)
        root_bags[key_bag] = child_tuples

    print(recurse(root_bags, 'shiny gold', 1) - 1)


if __name__ == "__main__":
    part1()
    part2()
