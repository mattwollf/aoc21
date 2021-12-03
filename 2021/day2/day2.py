
def part1():

    f = open("input.txt", "r")

    x, y = 0, 0

    for cmd in f:
        cur = str(cmd)
        parts = cur.split(" ")

        direction = parts[0]
        distance = int(parts[1])

        if direction == "forward":
            x += distance
        elif direction == "down":
            y += distance
        elif direction == "up":
            y -= distance

    print(x*y)


def part2():
    f = open("input.txt", "r")

    x, y = 0, 0

    aim = 0
    for cmd in f:
        cur = str(cmd)
        parts = cur.split(" ")

        direction = parts[0]
        distance = int(parts[1])

        if direction == "forward":
            x += distance
            y += distance * aim
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    print(x*y)


if __name__ == '__main__':
    part2()
