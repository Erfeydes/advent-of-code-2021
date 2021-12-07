filename = "input.txt"
f = open(filename, "r")
crabs = sorted(list(map(int, f.readline().rstrip().split(","))))


def part1():
    total_crabs = len(crabs)
    median = crabs[total_crabs//2]
    return sum(abs(c - median) for c in crabs)


def part2():
    total_crabs = len(crabs)
    mean = sum(crabs) // total_crabs
    return sum(abs(c - mean) * (abs(c - mean) + 1) // 2 for c in crabs)


print("Part 1 solution: ", part1(), "- Part 2 solution:", part2())
