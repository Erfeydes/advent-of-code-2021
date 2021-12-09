import numpy

from scipy.signal import find_peaks
from scipy.ndimage import measurements

filename = "input.txt"
lines = [fl.rstrip() for fl in open(filename).readlines()]
data = numpy.array([numpy.array(list(i)) for i in lines]).astype(int)
data = numpy.pad(data, pad_width=1, constant_values=9)


def part1():
    m = numpy.zeros([102, 102])

    for i in range(len(data)):
        for j in find_peaks(-1 * data[i])[0]:
            m[i, j] += 1

    for i in range(len(data[0])):
        for j in find_peaks(-1 * data[:, i])[0]:
            m[j, i] += 1

    return sum(data[m > 1] + 1)


def part2():
    data[data != 9] = 1
    data[data == 9] = 0

    x, n = measurements.label(data)
    area = measurements.sum(data, x, index=numpy.arange(x.max() + 1))
    return int(numpy.product(numpy.sort(area)[-3:]))


print("Part 1 solution: ", part1(), "- Part 2 solution:", part2())
