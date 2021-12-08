def part1(lines):
    lines = unique_count_replacement(lines)

    result = 0
    for sides in lines:
        rhs = sides[1]
        result += len(list(filter(lambda x: type(x) == int, rhs)))
    return result


def unique_count_replacement(lines):

    mapping = {
        2:1,
        3:7,
        4:4,
        7:8,
    }

    for sides in lines:
        for s in sides:
            for i in range(len(s)):
                sigsize = len(s[i])
                if sigsize in mapping:
                    s[i] = mapping[sigsize]

    return lines


def find_sig(line, number):

    len_to_num = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }

    return next(e for e in line if len(e) in len_to_num.keys() and len_to_num[len(e)] == number)


def part2(lines):
    result = 0
    for count, line in enumerate(lines):

        lhs, rhs = line

        sig1 = find_sig(lhs, 1)
        sig4 = find_sig(lhs, 4)
        sig7 = find_sig(lhs, 7)
        sig8 = find_sig(lhs, 8)

        zero_six_nine = set([e for e in lhs if len(e) == 6])
        sig6 = next(x for x in zero_six_nine if len(set(sig1).difference(set(x))) == 1)
        zero_nine = zero_six_nine.difference({''.join(sorted(sig6))})
        letter_top_right = next(iter(set(sig1).difference(set(sig6))))
        two_three_five = set([e for e in lhs if len(e) == 5])
        four_without_top_right = set(sig4).difference(set(letter_top_right))
        sig5 = next(
            x for x in two_three_five if set(x).intersection(four_without_top_right) == four_without_top_right
        )
        letter_bottom_right = next(iter(set(sig1).difference(set(letter_top_right))))
        sig2 = next(x for x in two_three_five if letter_bottom_right not in x)
        sig3 = next(iter(two_three_five.difference({''.join(sorted(sig5)), ''.join(sorted(sig2))})))
        sig9 = next(x for x in zero_nine if set(x).intersection(four_without_top_right) == four_without_top_right)
        sig0 = zero_nine.difference({sig9})

        mapping = {
            ''.join(sorted(sig1)): 1,
            ''.join(sorted(sig2)): 2,
            ''.join(sorted(sig3)): 3,
            ''.join(sorted(sig4)): 4,
            ''.join(sorted(sig5)): 5,
            ''.join(sorted(sig6)): 6,
            ''.join(sorted(sig7)): 7,
            ''.join(sorted(sig8)): 8,
            ''.join(sorted(sig9)): 9,
            ''.join(sorted(sig0)): 0,
        }

        digits = [str(mapping[x]) for x in rhs]
        result += int(''.join(digits))
    return result


def tests():
    lines = parse_input('sample.txt')
    assert part1(lines) == 26
    lines = parse_input('sample.txt')
    assert part2(lines) == 61229


def parse_input(name):
    with open(name, 'r') as f:

        result = []
        for line in f.readlines():
            lhs, rhs = line.split(' | ')
            lhs = lhs.split(' ')
            rhs = rhs.rstrip().split(' ')
            lhs = [''.join(sorted(list(x))) for x in lhs]
            rhs = [''.join(sorted(list(x))) for x in rhs]
            result.append([lhs, rhs])
        return result


if __name__ == '__main__':
    i = parse_input('input.txt')
    tests()
    print(part1(i))
    i2 = parse_input('input.txt')
    print(part2(i2))

    # print(part2())
