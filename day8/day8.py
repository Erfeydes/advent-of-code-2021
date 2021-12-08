from collections import Counter
from itertools import chain


filename = "input.txt"
lines = [fl.rstrip() for fl in open(filename).readlines()]


def part1():
    outputs = [line.split("|")[1].split() for line in lines]
    count = Counter(map(len, chain.from_iterable(outputs)))
    return sum(count[i] for i in [2, 3, 4, 7])


def part2():
    count = 0
    for signals, outputs in [line.split("|") for line in lines]:
        l = {len(seg): set(seg) for seg in signals.split()}
        num = ""
        for output in map(set, outputs.split()):
            match len(output), len(output & l[4]), len(output & l[2]):
                case 2, _, _:
                    num += "1"
                case 3, _, _:
                    num += "7"
                case 4, _, _:
                    num += "4"
                case 5, 2, _:
                    num += "2"
                case 5, 3, 1:
                    num += "5"
                case 5, 3, 2:
                    num += "3"
                case 6, 4, _:
                    num += "9"
                case 6, 3, 1:
                    num += "6"
                case 6, 3, 2:
                    num += "0"
                case 7, _, _:
                    num += "8"
        count += int(num)
    return count

print("Part 1 solution: ", part1(), "- Part 2 solution:", part2())
