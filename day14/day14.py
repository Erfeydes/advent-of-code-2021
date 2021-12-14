from collections import Counter, defaultdict

filename = "input.txt"
lines = [fl.rstrip() for fl in open(filename).readlines()]
template = lines[0]
rules = {}

for line in lines[2:]:
    (a, b), c = line.split(' -> ')
    rules[a, b] = ((a, c), (c, b))


def solve(p, r, n, last):
    for _ in range(n):
        tmp_p = defaultdict(int)
        for pair in p:
            products = r.get(pair)

            if products:
                n = p[pair]
                tmp_p[products[0]] += n
                tmp_p[products[1]] += n
            else:
                tmp_p[pair] = p[pair]
        p = tmp_p

    counts = defaultdict(int, {last: 1})
    for (x, _), n in p.items():
        counts[x] += n
    return max(counts.values()) - min(counts.values())


polymer = Counter(zip(template, template[1:]))
print("Part 1 solution", solve(polymer, rules, 10, template[-1]),
      "- Part 2 solution", solve(polymer, rules, 40, template[-1]))
