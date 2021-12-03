
def part1():

    f = open("input", "r")

    increasing = 0
    previous = int(f.readline())


    for depth in f:
        cur = int(depth)
        if cur > previous:
            increasing += 1
        previous = cur

    print(increasing)

def part2():
    f = open("input", "r")

    depths = list(map(int, f.readlines()))

    increasing = 0

    previous = sum(depths[0:3])
    for i in range(2, len(depths) - 1):
        depth_window = depths[i-1:i+2]
        cur = sum(depth_window)
        if cur > previous:
            increasing += 1
        previous = cur

    print(increasing)

if __name__ == '__main__':
    part2()
