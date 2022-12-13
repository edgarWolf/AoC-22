import ast

inp_file = "13.txt"

with open(inp_file) as f:
    blocks = f.read().split("\n\n")

def map_input(blocks):
    ret = []
    for block in blocks:
        first, second = block.split("\n")
        ret.append((ast.literal_eval(first), ast.literal_eval(second)))
    return ret


L = map_input(blocks)

INVALID = 0
VALID = 1
SAME = 2

def compare_ints(a, b):
    if a < b:
        return VALID
    if b < a:
        return INVALID
    return SAME

def compare_lists(L, R):
    max_iterations = -99
    if type(L) == list and type(R) == list:
        max_iterations = max(len(L), len(R))

    idx = 0
    for l, r in zip(L, R):
        idx += 1
        if type(l) == list and type(r) == list:
            comparison = compare_lists(l, r)
        elif type(l) == int and type(r) == int:
            comparison = compare_ints(l, r)
        elif type(l) == list and type(r) == int:
            comparison = compare_lists(l, [r])
        elif type(l) == int and type(r) == list:
            comparison = compare_lists([l], r)

        if comparison == INVALID or comparison == VALID:
            return comparison

    if idx < max_iterations:
        return VALID if len(L) < len(R) else INVALID
    
    return SAME

def part1(L):
    counter = 0
    for idx, (l1, l2) in enumerate(L, start=1):
        valid = compare_lists(l1, l2)
        if valid == VALID:
            counter += idx
    return counter

def part2(L):
    
    flattened_L = list(sum(L, ()))
    div1 = [[2]]
    div2 = [[6]]
    flattened_L.insert(0, div1)
    flattened_L.insert(1, div2)
    div1_pos = 0
    div2_pos = 1
    n = len(flattened_L)
    for i in range(0, n-1):
        for j in range(0, n - i - 1):

            l1 = flattened_L[j]
            l2 = flattened_L[j + 1]

            if compare_lists(l1, l2) == INVALID:
                flattened_L[j], flattened_L[j +1] = flattened_L[j + 1], flattened_L[j]

                if div1 == flattened_L[j]:
                    div1_pos = j
                elif div1 == flattened_L[j + 1]:
                    div1_pos = j + 1
                
                if div2 == flattened_L[j]:
                    div2_pos = j
                elif div2 == flattened_L[j + 1]:
                    div2_pos = j + 1

    return (div1_pos + 1) * (div2_pos + 1)



print("Part 1:", part1(L))
print("Part 1:", part2(L))