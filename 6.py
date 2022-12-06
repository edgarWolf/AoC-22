with open("6.txt") as f:
    line = f.read()

def part1(line, length=4):
    n = len(line)
    for i in range(n):
        substr = line[i:min(i + length, n)]
        set_substr = set(substr)
        if len(set_substr) == length:
            return min(i + length, n)
    return None

print(f"Part 1: {part1(line)}")
print(f"Part 2: {part1(line, length=14)}")
