import re
import string
import copy

UPPER_CASE_LETTERS = string.ascii_uppercase

with open("5.txt") as f:
    lines = f.read().splitlines()

drawing = lines[:9]
# Line 9 is empty
instructions = lines[10:]

def map_instructions(instructions):
    ret = []
    for instruction in instructions:
        matches = re.search(r"move (\d+) from (\d+) to (\d+)", instruction)
        amount = int(matches.group(1))
        from_pos = int(matches.group(2))
        to_pos = int(matches.group(3))
        ret.append((from_pos, to_pos, amount))
    return ret


def map_drawing(drawing):
    ret = []
    indices = drawing[-1]
    indicies_w_spaces = indices.replace(" ", "")
    stack_indices = [indices.index(i) for i in indicies_w_spaces]
    
    # Column wise
    n = len(drawing) - 1
    for index in stack_indices:
        vals = []
        for i in range(n):
            letter = drawing[i]
            if letter[index] in UPPER_CASE_LETTERS:
                vals.append((letter[index], i))
        ret.append(vals)

    return ret


def part1(instructions, stacks):
    # Copy for no mutation for next task.
    stacks_copy = copy.deepcopy(stacks)
    for from_pos, to_pos, amount in instructions:
        stack_from = stacks_copy[from_pos - 1]
        stack_to = stacks_copy[to_pos - 1]
        items = stack_from[:amount]
        for item in items:
            stack_to.insert(0, item)
            stack_from.remove(item)
    top_items = [stack[0][0] for stack in stacks_copy]
    return ''.join(top_items)


def part2(instructions, stacks):
    stacks_copy = copy.deepcopy(stacks)
    for from_pos, to_pos, amount in instructions:
        stack_from = stacks_copy[from_pos - 1]
        stack_to = stacks_copy[to_pos - 1]
        items = list(reversed(stack_from[:amount]))
        for item in items:
            stack_to.insert(0, item)
            stack_from.remove(item)
    top_items = [stack[0][0] for stack in stacks_copy]
    return ''.join(top_items)


instructions = map_instructions(instructions)
stacks = map_drawing(drawing)


print(f"Part 1: {part1(instructions, stacks)}")
print(f"Part 2: {part2(instructions, stacks)}")