from collections import Counter, deque

filename = "input.txt"
f = open(filename, "r")
lanternfishes = list(map(int, f.readline().rstrip().split(",")))


def get_fishes(fishes_list):
    c = Counter(fishes_list)
    fishes = deque([0 for _ in range(9)])
    for i in c:
        fishes[i] = c[i]
    return fishes


def new_day(fishes):
    breed = fishes.popleft()
    fishes[-2] += breed
    fishes.append(breed)
    return fishes


def simulation(fishes, nb_days):
    for i in range(nb_days):
        fishes = new_day(fishes)
    return sum(fishes)


print("Part 1 solution: ", simulation(get_fishes(lanternfishes), 80),
      "- Part 2 solution:", simulation(get_fishes(lanternfishes), 256))
