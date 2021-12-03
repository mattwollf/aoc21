
def part1():

    f = open("input.txt", "r")

    lines = list(map(int, f.readlines()))

    lines.sort()

    for i in lines:
        for j in lines:
            if i + j == 2020:
                print(i*j)


def part2():
    f = open("input.txt", "r")

    lines = list(map(int, f.readlines()))

    lines.sort()

    for i in lines:
        for j in lines:
            for k in lines:
                if i + j + k == 2020:
                    print(i * j * k)

if __name__ == "__main__":
    part2()
