import math
import numpy
from copy import deepcopy
from itertools import combinations

filename = "input.txt"
reports = open(filename).read().split("\n\n")
scanners = []

for report in reports:
    values = numpy.array([[int(i) for i in line.split(",")] for line in report.splitlines()[1:]])
    scanners.append(values)


def rotations():
    vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    vectors = list(map(numpy.array, vectors))
    for vi in vectors:
        for vj in vectors:
            if vi.dot(vj) == 0:
                vk = numpy.cross(vi, vj)
                yield lambda x: \
                    numpy.matmul(x, numpy.array([vi, vj, vk]))


def find_alignment(s, hashes, i, j, v):
    s1, s2 = s[i], s[j]
    for rot in rotations():
        s2t = rot(s2)
        p = hashes[i][v][0]
        for q in hashes[j][v]:
            diff = s1[p, :] - s2t[q, :]
            if len((b := set(map(tuple, s2t + diff))) & set(map(tuple, s1))) >= 12:
                return diff, b, rot


def hashmap(coords):
    s = {
        tuple(sorted(map(abs, coords[i, :] - coords[j, :]))): (i, j)
        for i, j in combinations(range(len(coords)), 2)
    }
    return s


def find_overlapping(hashes):
    for i, j in combinations(range(len(hashes)), 2):
        if len(m := set(hashes[i]) & set(hashes[j])) >= math.comb(12, 2):
            yield i, j, next(iter(m))


def solve(s):
    scanners_copy = deepcopy(s)
    p = {0: (0, 0, 0)}
    hashes = list(map(hashmap, scanners_copy))
    b = set(map(tuple, scanners_copy[0]))
    while len(p) < len(scanners_copy):
        for i, j, v in find_overlapping(hashes):
            if not (i in p) ^ (j in p):
                continue
            elif j in p:
                i, j = j, i
            p[j], new_beacons, rot = find_alignment(scanners_copy, hashes, i, j, v)
            scanners_copy[j] = rot(scanners_copy[j]) + p[j]
            b |= new_beacons
    return [p[i] for i in range(len(scanners_copy))], b


positions, beacons = solve(scanners)
print("Part 1 solution:", len(beacons),
      "- Part 2 solution:", max(numpy.abs(x - y).sum() for x, y in combinations(positions, 2)))
