import numpy
from itertools import product

filename = "input.txt"
lines = [fl.rstrip() for fl in open(filename).readlines()]


def join(x, y):
    x_values, x_levels = x
    y_values, y_levels = y
    xy_values = numpy.append(x_values, y_values)
    xy_levels = numpy.append(x_levels, y_levels) + 1
    return xy_values, xy_levels


def explode(values, levels):
    check = False
    while numpy.size(numpy.where(levels > 4)) > 0:
        check = True
        x_pos, y_pos, *overflow = numpy.where(levels > 4)[0]
        if x_pos != 0:
            values[x_pos - 1] += values[x_pos]
        if y_pos != numpy.size(levels) - 1:
            values[y_pos + 1] += values[y_pos]
        values = numpy.delete(values, (x_pos, y_pos))
        values = numpy.insert(values, x_pos, 0)
        levels = numpy.delete(levels, (x_pos, y_pos))
        levels = numpy.insert(levels, x_pos, 4)
    return values, levels, check


def split(values, levels):
    check = False
    if numpy.size(numpy.where(values > 9)) > 0:
        check = True
        pos, *overflow = numpy.where(values > 9)[0]
        x_val, y_val = numpy.floor(values[pos] / 2), numpy.ceil(values[pos] / 2)
        level = levels[pos] + 1
        values = numpy.delete(values, pos)
        values = numpy.insert(values, pos, (x_val, y_val))
        levels = numpy.delete(levels, pos)
        levels = numpy.insert(levels, pos, (level, level))
    return values, levels, check


def magnitude(values, levels):
    if numpy.size(values) > 1:
        x_pos, y_pos, *overflow = numpy.where(levels == levels.max())[0]
        val = values[x_pos] * 3 + values[y_pos] * 2
        level = levels[x_pos] - 1
        values = numpy.delete(values, (x_pos, y_pos))
        values = numpy.insert(values, x_pos, val)
        levels = numpy.delete(levels, (x_pos, y_pos))
        levels = numpy.insert(levels, x_pos, level)
        values, levels = magnitude(values, levels)
    return values, levels


def decode(string):
    values = []
    levels = []
    level = 0
    for char in string.strip():
        if char == ",":
            continue
        elif char == "[":
            level += 1
        elif char == "]":
            level -= 1
        else:
            values.append(int(char))
            levels.append(level)
    return numpy.array(values), numpy.array(levels)


va, le = decode(lines[0])

for s in lines[1:]:
    va, le = join((va, le), decode(s))
    check_explode = True
    check_split = True
    while check_explode or check_split:
        va, le, check_explode = explode(va, le)
        va, le, check_split = split(va, le)

print("Part 1 solution:", magnitude(va, le)[0][0])

magnitude_list = []

print("The part 2 takes around 20 seconds to complete, will probably redo this day with a tree if I find some time")

for i, j in product(range(len(lines)), range(len(lines))):
    if i == j:
        continue

    va, le = join(decode(lines[i]), decode(lines[j]))
    check_explode = True
    check_split = True
    while check_explode or check_split:
        va, le, check_explode = explode(va, le)
        va, le, check_split = split(va, le)
    magnitude_list.append(magnitude(va, le)[0][0])

    va, le = join(decode(lines[j]), decode(lines[i]))
    check_explode = True
    check_split = True
    while check_explode or check_split:
        va, le, check_explode = explode(va, le)
        va, le, check_split = split(va, le)
    magnitude_list.append(magnitude(va, le)[0][0])

print("Part 2 solution:", max(magnitude_list))
