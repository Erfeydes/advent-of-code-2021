filename = "input.txt"
instructions = [fl.rstrip().split(" ") for fl in open(filename).readlines()]


def solve(has_aim):
    position = depth = aim = 0
    for (instr, val) in instructions:
        match instr:
            case "forward":
                position += int(val)
                if has_aim:
                    depth += int(val) * aim
            case "down":
                if has_aim:
                    aim += int(val)
                else:
                    depth += int(val)
            case "up":
                if has_aim:
                    aim -= int(val)
                else:
                    depth -= int(val)

    return position * depth


print("Part 1 solution:", solve(False), "- Part 2 solution:", solve(True))

