filename = "input.txt"
lines = [fl.rstrip() for fl in open(filename).readlines()]

opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
error_score = 0
scores = []

for line in lines:
    s = []
    valid = True
    for c in line:
        if c in opening:
            s.append(c)
        else:
            tmp = s.pop()
            if opening.index(tmp) != closing.index(c):
                error_score += points[c]
                valid = False
                break
    if valid:
        score = 0
        for v in reversed(s):
            score *= 5
            score += opening.index(v) + 1
        scores.append(score)
scores.sort()

print("Part 1 solution: ", error_score, "- Part 2 solution:", scores[len(scores) // 2])
