
def gamma(l: list[dict]):
    digits = [int(max(d.items(), key=lambda x: x[1])[0]) for d in l]
    return digits


def epsilon(l: list[dict]):
    digits = [int(min(d.items(), key=lambda x: x[1])[0]) for d in l]
    return digits


def part1():
    f = open("input.txt", "r")

    lines = [x.rstrip() for x in f]

    counts = []

    for i in range(12):
        count = {
            '0': 0,
            '1': 0,
        }

        for b in lines:
            count[b[i]] += 1

        counts.append(count)

    ga = gamma(counts)
    ep = epsilon(counts)

    ga_dec = 0
    ep_dec = 0

    power = 0
    for i in ga[::-1]:
        ga_dec += i * (2 ** power)
        power += 1

    power = 0
    for i in ep[::-1]:
        ep_dec += i * (2 ** power)
        power += 1

    print(ga_dec * ep_dec)


def compute_counts(lines):
    counts = []

    for i in range(12):
        count = {
            '0': 0,
            '1': 0,
        }

        for b in lines:
            count[b[i]] += 1

        counts.append(count)
    return counts


def part2():
    f = open("input.txt", "r")

    lines = [x.rstrip() for x in f]

    counts = compute_counts(lines)

    oxygen_candidates = list(lines)
    co2_candidates = list(lines)

    ga = gamma(counts)
    ep = epsilon(counts)

    print(ga)
    print(ep)

    for i in range(12):
        if len(oxygen_candidates) == 1:
            break
        smaller_counts = compute_counts(oxygen_candidates)
        bitpair = smaller_counts[i]
        upper = max(bitpair.items(), key=lambda x: x[1])[0]
        lower = min(bitpair.items(), key=lambda x: x[1])[0]

        if upper == lower:
            oxygen_candidates = list(filter(
                lambda x: x[i] == '1',
                oxygen_candidates
            ))
        else:
            oxygen_candidates = list(filter(
                lambda x: x[i] == upper,
                oxygen_candidates))

    for i in range(12):
        if len(co2_candidates) == 1:
            break
        smaller_counts = compute_counts(co2_candidates)
        bitpair = smaller_counts[i]
        upper = max(bitpair.items(), key=lambda x: x[1])[0]
        lower = min(bitpair.items(), key=lambda x: x[1])[0]


        if upper == lower:
            co2_candidates = list(filter(
                lambda x: x[i] == '0',
                co2_candidates
            ))
        else:
            co2_candidates = list(filter(
                lambda x: x[i] == lower,
                co2_candidates))


    oxy_dec = 0
    co2_dec = 0

    power = 0
    for i in oxygen_candidates[0][::-1]:
        oxy_dec += int(i) * (2 ** power)
        power += 1

    power = 0
    for i in co2_candidates[0][::-1]:
        co2_dec += int(i) * (2 ** power)
        power += 1

    print(oxygen_candidates[0])
    print(co2_candidates[0])
    print(oxy_dec)
    print(co2_dec)
    print(oxy_dec * co2_dec)


if __name__ == '__main__':
    part1()
    part2()
