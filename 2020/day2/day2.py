
def part1():

    f = open("input.txt", "r")

    lines = f.readlines()

    total = 0
    for l in lines:
        split = l.split(" ")
        lower, upper = split[0].split("-")
        lower, upper = int(lower), int(upper)
        lim = split[1].rstrip(":")

        pw = split[2]
        count = pw.count(lim)
        test = lower <= count <= upper
        if test:
            total += 1
    print(total)


def part2():
    from operator import xor
    f = open("input.txt", "r")

    lines = f.readlines()

    total = 0
    for l in lines:
        split = l.split(" ")
        lower, upper = split[0].split("-")
        lower, upper = int(lower), int(upper)
        lim = split[1].rstrip(":")

        pw = split[2]
        lower_match = pw[lower - 1] == lim
        upper_match = pw[upper - 1] == lim
        if xor(lower_match, upper_match):
            total += 1

    print(total)


if __name__ == "__main__":
    part2()
