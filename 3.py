import string

with open("3.txt") as f:
    lines = f.read().splitlines()

alphabet = {char: p + 1 for p, char in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

def part1(lines):
    prio = 0
    for line in lines:
        n = len(line)
        a = line[:n//2]
        b = line[n//2:]
        common_chars = ''.join(set(a).intersection(b))
        prio += sum(alphabet[c] for c in common_chars)
    return prio


def part2(lines):
    prio = 0
    for i in range(0, len(lines), 3):
        a, b, c = lines[i:i+3]
        common_chars = ''.join(set(a).intersection(b).intersection(c))
        prio += sum(alphabet[c] for c in common_chars)
    return prio


print(f"Part 1: {part1(lines)}")
print(f"Part 2: {part2(lines)}")
