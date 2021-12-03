def validate_passport1(passport: dict):
    fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
        # 'cid',
    }

    keys = passport.keys()
    result = list(map(lambda x: x in keys, fields))
    return all(result)


def part1():
    f = open("input.txt", "r")

    lines = f.readlines()
    # lines = list(map(lambda x: x.rstrip(), lines))

    passports = []

    passport = {}
    for line in lines:

        if line == "\n":
            passports.append(passport)
            passport = {}
            continue

        fields = line.split(" ")
        for field in fields:
            split = field.split(":")
            k, v = split
            passport[k] = v

    validated = [validate_passport1(x) for x in passports]
    print(sum(validated))


def validate_passport2(passport: dict):
    def byr(p: dict):
        return 1920 <= int(p['byr']) <= 2002

    def iyr(p: dict):
        return 2010 <= int(p['iyr']) <= 2020

    def eyr(p: dict):
        return 2020 <= int(p['eyr']) <= 2030

    def hgt(p: dict):
        v = p['hgt']
        unit = v[-2:]

        if unit not in {'cm', 'in'}:
            return False

        number = int(v[:-2])
        if unit == 'cm':
            return 150 <= number <= 193
        elif unit == 'in':
            return 59 <= number <= 76

    def hcl(p: dict):
        v = p['hcl']
        first = v[0] == '#'
        number = v[1:7]

        if not first:
            return False

        chars = '0123456789abcdef'

        return all([x in chars for x in number])

    def ecl(p: dict):

        vals = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

        return p['ecl'] in vals

    def pid(p: dict):
        v = p['pid']
        return len(v) == 9 and v.isnumeric()

    fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
        # 'cid',
    }

    present = all(map(lambda x: x in passport.keys(), fields))
    if not present:
        return False

    validations = [byr, iyr, eyr, hgt, hcl, ecl, pid]
    computed = [x(passport) for x in validations]
    return all(computed)


def part2():
    f = open("input.txt", "r")

    lines = f.readlines()
    # lines = list(map(lambda x: x.rstrip(), lines))

    passports = []

    passport = {}
    for line in lines:

        if line == "\n":
            passports.append(passport)
            passport = {}
            continue

        fields = line.rstrip().split(" ")
        for field in fields:
            split = field.split(":")
            k, v = split
            passport[k] = v

    validated = [validate_passport2(x) for x in passports]
    print(sum(validated))


if __name__ == "__main__":
    part1()
    part2()
