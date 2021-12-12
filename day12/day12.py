from collections import defaultdict

filename = "input.txt"
neighbours = defaultdict(list)

for line in open(filename):
    a, b = line.strip().split('-')
    neighbours[a] += [b]
    neighbours[b] += [a]


def search(part, known=set(), cave="start"):
    if cave == "end":
        return 1
    if cave in known:
        if cave == "start":
            return 0
        if cave.islower():
            if part == 1:
                return 0
            else:
                part = 1

    return sum(search(part, known | {cave}, n) for n in neighbours[cave])


print("Part 1 solution", search(part=1), "- Part 2 solution", search(part=2))
