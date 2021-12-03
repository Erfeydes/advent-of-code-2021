filename = "input.txt"
binaries = [fl.rstrip() for fl in open(filename).readlines()]


def common(i, b):
    bits = [x[i] for x in b]
    if bits.count("0") > bits.count("1"):
        return "0"
    else:
        return "1"


def uncommon(i, b):
    return str(1 - int(common(i, b)))


def part1():
    gamma = epsilon = ""
    for i in range(len(binaries[0])):
        gamma += common(i, binaries)
        epsilon += uncommon(i, binaries)
    return int(gamma, 2) * int(epsilon, 2)


def filter_bits(b, rating_func):
    for i in range(len(binaries[0])):
        bit = rating_func(i, b)
        b = [x for x in b if x[i] == bit]
        if len(b) == 1:
            return b[0]


def part2():
    o2 = filter_bits(binaries, common)
    co2 = filter_bits(binaries, uncommon)
    return int(o2, 2) * int(co2, 2)


print("Part 1 solution:", part1(), "- Part 2 solution:", part2())
