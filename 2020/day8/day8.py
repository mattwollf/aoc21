
def part1():
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [line.rstrip(".\n") for line in lines]

    hit = [False] * len(lines)

    state = {
        'accumulator': 0,
        'pc': 0,
    }

    def accumulate(n, s):
        s['accumulator'] = s['accumulator'] + n
        s['pc'] = s['pc'] + 1

    def jump(n, s):
        s['pc'] = s['pc'] + n

    def nop(n, s):
        s['pc'] = s['pc'] + 1

    opmap = {
        'acc': accumulate,
        'jmp': jump,
        'nop': nop,
    }

    while state['pc'] < len(lines):
        i = state['pc']
        line = lines[state['pc']]
        if hit[i]:
            print(state['accumulator'])
            return

        hit[i] = True
        op, arg = line.split(' ')
        n = int(arg)
        opmap[op](n, state)


def part2():
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [line.rstrip(".\n") for line in lines]

    instructions = [x.split(' ') for x in lines]

    def accumulate(n, s):
        s['accumulator'] = s['accumulator'] + n
        s['pc'] = s['pc'] + 1

    def jump(n, s):
        s['pc'] = s['pc'] + n

    def nop(n, s):
        s['pc'] = s['pc'] + 1

    opmap = {
        'acc': accumulate,
        'jmp': jump,
        'nop': nop,
    }

    for i in range(len(instructions)):

        if instructions[i][0] not in ('nop', 'jmp'):
            continue

        hit = [False] * len(lines)

        cur = instructions[i][0]

        if cur == 'nop':
            instructions[i][0] = 'jmp'
        elif cur == 'jmp':
            instructions[i][0] = 'nop'

        state = {
            'accumulator': 0,
            'pc': 0,
        }

        infinite = False
        while state['pc'] < len(instructions):
            op, arg = instructions[state['pc']]
            if hit[state['pc']]:
                infinite = True
                print("Replacing {0} with {1} on line {2} did not work.".format(cur, instructions[i][0], i))
                break

            hit[state['pc']] = True
            opmap[op](int(arg), state)

        if infinite:
            continue
        print(state['accumulator'])
        return


if __name__ == "__main__":
    part1()
    part2()
