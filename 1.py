with open("1.txt") as f:
    lines = f.read().split("\n\n")


def map_input(lines):
    return [[int(n) for n in block_str.split("\n")] for block_str in lines]

blocks = map_input(lines)

def part_1(blocks):
    calories = [sum(block) for block in blocks]
    return max(calories)


print(part_1(blocks))


def part_2(blocks):
    calories = [sum(block) for block in blocks]
    calories = list(sorted(calories))
    return sum(c for c in calories[-3:])


print(part_2(blocks))
