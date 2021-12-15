from queue import PriorityQueue
from collections import defaultdict
from math import inf

filename = "input.txt"
numbers = [[int(n) for n in fl.rstrip()] for fl in open(filename).readlines()]


def get_direction(point, matrix):
    x, y = point
    directions = []
    if x - 1 >= 0:
        directions.append((x - 1, y))
    if x + 1 < len(matrix[0]):
        directions.append((x + 1, y))
    if y + 1 < len(matrix):
        directions.append((x, y + 1))
    if y - 1 >= 0:
        directions.append((x, y - 1))
    return directions


def create_graph(matrix):
    graph = {}
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            point = (x, y)
            graph[point] = {}
            for pn in get_direction(point, matrix):
                xn, yn = pn
                graph[point][pn] = matrix[yn][xn]
    return graph


def dijkstra(graph, source, destination):
    visited = defaultdict(bool)
    visited[source] = True

    priority = {}
    for n in graph.keys():
        if n == source:
            priority[n] = 0
        else:
            priority[n] = inf

    queue = PriorityQueue()
    queue.put((0, source))

    current = source

    while current != destination:
        point, current = queue.get()
        for neigh in graph[current].keys():
            if not visited[neigh]:
                if priority[neigh] > point + graph[current][neigh]:
                    priority[neigh] = point + graph[current][neigh]
                    queue.put((priority[neigh], neigh))
    return priority[destination]


print("Part 1 solution:", dijkstra(create_graph(numbers), (0, 0), (len(numbers[0]) - 1, len(numbers) - 1)))

w = len(numbers)
h = len(numbers[0])

for _ in range(4):
    for row in numbers:
        tail = row[-w:]
        row.extend((x + 1) if x < 9 else 1 for x in tail)

for _ in range(4):
    for row in numbers[-h:]:
        row = [(x + 1) if x < 9 else 1 for x in row]
        numbers.append(row)

print("Part 2 solution:", dijkstra(create_graph(numbers), (0, 0), (len(numbers[0]) - 1, len(numbers) - 1)))
