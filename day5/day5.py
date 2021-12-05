from numpy import sign


filename = "input.txt"
lines = [fl.rstrip() for fl in open(filename).readlines()]


def process_lines(diagonals=False):
    graph = {}
    for line in lines:
        coords = line.split(" -> ")
        x1, y1 = map(int, coords[0].split(","))
        x2, y2 = map(int, coords[1].split(","))

        if x1 != x2 and y1 != y2 and not diagonals:
            continue

        v1, v2 = x2 - x1, y2 - y1

        for i in range(0, max(abs(v1), abs(v2))):
            px = i * sign(v1)
            py = i * sign(v2)
            graph[(x1 + px, y1 + py)] = graph.get((x1 + px, y1 + py), 0) + 1

        graph[(x2, y2)] = graph.get((x2, y2), 0) + 1
    return len([v for v in graph.values() if v > 1])


print("Part 1 solution: ", process_lines(), "- Part 2 solution:", process_lines(True))