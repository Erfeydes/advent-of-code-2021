import numpy
from scipy.signal import convolve

filename = "input.txt"
octopuses = numpy.genfromtxt(open(filename), delimiter=1)

m = numpy.matrix("1 1 1; 1 0 1; 1 1 1")
count = 0

for i in range(1, 1000):
    octopuses += 1
    base_value = octopuses
    while True:
        flash = octopuses > 9
        octopuses = base_value + convolve(flash, m, "same")
        if (flash == (octopuses > 9)).all():
            count += flash.sum()
            octopuses[flash] = 0
            break

    if i == 100:
        print("Part 1 solution:", count)
    if flash.all():
        print("Part 2 solution:", i)
        break
