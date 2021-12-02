f = open("input.txt", "r")
numbers = list(map(int, f.read().splitlines()))
f.close()

part1 = sum(b > a for a, b in zip(numbers, numbers[1:]))
part2 = sum(b > a for a, b in zip(numbers, numbers[3:]))

print("Part 1 solution:", part1, "- Part 2 solution:", part2)