filename = "input.txt"
lines = [fl.rstrip() for fl in open(filename).readlines()]

dots, folds = set(), []

for line in lines:
    if line.startswith("fold along"):
        _, _, f = line.split()
        direction, value = f.split("=")
        folds.append((0 if direction == "x" else 1, int(value)))
    elif line != "":
        dots.add(tuple(map(int, line.split(","))))


def fold(d, v):
    for dot in dots.copy():
        if dot[d] > v:
            tmp = list(dot)
            tmp[d] = 2 * v - tmp[d]
            dots.remove(dot)
            dots.add(tuple(tmp))


for f in folds:
    fold(*f)
    if f == folds[0]:
        print("Part 1 solution:", len(dots))

print("Part 2 solution:")
xm, ym = map(max, zip(*dots))
for y in range(ym + 1):
    for x in range(xm + 1):
        if (x, y) in dots:
            print("#", end='')
        else:
            print(" ", end='')
    print()
