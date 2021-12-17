from re import findall

filename = "input.txt"
xmin, xmax, ymin, ymax = map(int, findall(r"[-\d]+", open(filename).read()))


def compute(vx, vy, px=0, py=0):
    if px > xmax or py < ymin:
        return 0
    elif px >= xmin and py <= ymax:
        return 1
    else:
        return compute(vx - (vx > 0), vy - 1, px + vx, py + vy)


hits = [compute(x, y) for x in range(1, 1 + xmax) for y in range(ymin, -ymin)]

print("Part 1 solution:", abs(ymin) * abs(ymin + 1) // 2, "Part 2 solution:", sum(hits))
