with open("4.txt") as f:
    lines = f.read().splitlines()

def map_input(lines):
    L = []
    R = []
    for line in lines:
        range_a, range_b = line.split(",")
        l_lb, l_ub = range_a.split("-")
        r_lb, r_ub = range_b.split("-")
        L.append((int(l_lb), int(l_ub)))
        R.append((int(r_lb), int(r_ub)))
    return L, R

L, R = map_input(lines)

def part1(L, R):
    counter = 0
    for (l_lb, l_ub), (r_lb, r_ub) in zip(L, R):
        if r_lb >= l_lb and r_ub <= l_ub or l_lb >= r_lb and l_ub <= r_ub:
            counter += 1 
    return counter


def part2(L, R):
    counter = 0
    for (l_lb, l_ub), (r_lb, r_ub) in zip(L, R):
        l_range = list(range(l_lb, l_ub + 1))
        r_range = list(range(r_lb, r_ub + 1))
        intersection = set(l_range).intersection(r_range)
        if intersection:
            counter += 1
    return counter


print(f"Part 1: {part1(L, R)}")
print(f"Part 2 {part2(L, R)}")