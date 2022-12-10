inp_file = "10.txt"

with open(inp_file) as f:
    lines = f.read().splitlines()

def map_input(lines):
    ret = []
    for line in lines:
        if line == "noop":
            ret.append((line, 0))
        else:
            add, amount = line.split()
            ret.append((add, int(amount)))
    return ret


commands = map_input(lines)


def part1(commands):
    x = 1
    cycle = 1
    ret = []
    cycles = [i for i in range(20, 220 + 1, 40)]
    curr_cycle_idx = 0
    curr_cycle = cycles[curr_cycle_idx]
    for cmd, amount in commands:
        if cmd == "noop":
            cycle += 1
            if cycle == curr_cycle:
                ret.append(cycle * x)
                curr_cycle_idx = min(curr_cycle_idx + 1, len(cycles) - 1)
                curr_cycle = cycles[curr_cycle_idx] 
        else:
            cycle += 1
            if cycle == curr_cycle:
                ret.append(cycle * x)
                curr_cycle_idx = min(curr_cycle_idx + 1, len(cycles) - 1)
                curr_cycle = cycles[curr_cycle_idx] 
            x += amount
            cycle += 1
            if cycle == curr_cycle:
                ret.append(cycle * x)
                curr_cycle_idx = min(curr_cycle_idx + 1, len(cycles) - 1)
                curr_cycle = cycles[curr_cycle_idx]
    return sum(ret)


def update_crt_position(position):
    row, col = position
    if (col+ 1) % 40 == 0:
        row += 1
        col = 0
    else:
        col += 1
    return [row, col]


def part2(commands):
    # Other symbols, for better readability
    letter_symbol = "██"

    blank_symbol = "░░"

    CRT = [[letter_symbol if i == 0 or i == 39 else blank_symbol for i in range(40)] for j in range(6)]
    x = 1
    cycle = 1
    pos = [-1, 39]
    add_amount = None
    to_add = False
    for cmd, amount in commands:

        pos = update_crt_position(pos)
        pos_in_row = pos[1]
        if to_add:
            if abs(x - pos_in_row) <= 1:
                CRT[pos[0]][pos[1]] = letter_symbol
            else:
                CRT[pos[0]][pos[1]] = blank_symbol
            x += add_amount
            to_add = False
            pos = update_crt_position(pos)
            pos_in_row = pos[1]
            cycle += 1

        if cmd == "noop":
            if abs(x - pos_in_row) <= 1:
                CRT[pos[0]][pos[1]] = letter_symbol
            else:
                CRT[pos[0]][pos[1]] = blank_symbol
            cycle += 1
        else:
            if abs(x - pos_in_row) <= 1:
                CRT[pos[0]][pos[1]] = letter_symbol
            else:
                CRT[pos[0]][pos[1]] = blank_symbol
            add_amount = amount
            to_add = True
            cycle += 1
    return CRT

def print_crt(CRT):
    for row in CRT:
        for val in row:
            print(val, end="")
        print("\n")


print("Part 1: ", part1(commands))
print("Part 2: ")
print_crt(part2(commands))