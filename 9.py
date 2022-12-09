inp_file = "9.txt"

with open(inp_file) as f:
    lines = f.read().splitlines()

def map_input(lines):
    ret = []
    for line in lines:
        directionn = line[0]
        amount = int(line[2:])
        ret.append((directionn, amount))
    return ret


commands = map_input(lines)

def is_touching(head_pos, tail_pos):
    x_h, y_h = head_pos
    x_t, y_t = tail_pos
    return abs(x_h - x_t) <= 1 and abs(y_h - y_t) <= 1

def position_diff(head_pos, tail_pos):
    x_diff = head_pos[0] - tail_pos[0]
    y_diff = head_pos[1] - tail_pos[1]
    return (x_diff, y_diff)


def handle_tail_move(diff, tail):
    y_diff, x_diff = diff
    # Move right
    if x_diff > 0 and y_diff == 0:
        tail[1] += 1
    # Move left
    elif x_diff < 0 and y_diff == 0:
        tail[1] -= 1
    # Move up:
    elif x_diff == 0 and y_diff > 0:
        tail[0] += 1
    # Move down
    elif x_diff == 0 and y_diff < 0:
        tail[0] -= 1
    
    # Move Northwest
    elif x_diff < 0 and y_diff > 0:
        tail[0] += 1
        tail[1] -= 1
    # Move Northeast
    elif x_diff > 0 and y_diff > 0:
        tail[0] += 1
        tail[1] += 1
    # Move Southwest
    elif x_diff < 0 and y_diff < 0:
        tail[0] -= 1
        tail[1] -= 1
    # Move Southeast
    elif x_diff > 0 and y_diff < 0:
        tail[0] -= 1
        tail[1] += 1
    
    

def part1(commands):
    positions = set()
    head_pos = [0, 0]
    tail_pos = [0, 0]
    positions.add((0, 0))
    for direction, amount in commands:

        if direction == "L":
            for _ in range(amount):
                head_pos[1] -= 1
                if not is_touching(head_pos, tail_pos):
                    pos_diff = position_diff(head_pos, tail_pos)
                    handle_tail_move(pos_diff, tail_pos)
                positions.add(tuple(tail_pos))


        elif direction == "R":
            for _ in range(amount):
                head_pos[1] += 1
                if not is_touching(head_pos, tail_pos):
                    pos_diff = position_diff(head_pos, tail_pos)
                    handle_tail_move(pos_diff, tail_pos)
                positions.add(tuple(tail_pos))

        elif direction == "U":
            for _ in range(amount):
                head_pos[0] += 1
                if not is_touching(head_pos, tail_pos):
                    pos_diff = position_diff(head_pos, tail_pos)
                    handle_tail_move(pos_diff, tail_pos)
                positions.add(tuple(tail_pos))

        elif direction == "D":
            for _ in range(amount):
                head_pos[0] -= 1
                if not is_touching(head_pos, tail_pos):
                    pos_diff = position_diff(head_pos, tail_pos)
                    handle_tail_move(pos_diff, tail_pos)
                positions.add(tuple(tail_pos))

    return len(positions)



def part2(commands):
    positions = set()
    elements = [[0, 0] for _ in range(10)]
    positions.add((0, 0))
    real_head = elements[0]
    for direction, amount in commands:
        if direction == "L":
            for _ in range(amount):
                real_head[1] -= 1
                for i in range(9):
                    head_pos = elements[i]
                    tail_pos = elements[i + 1]
                    if not is_touching(head_pos, tail_pos):
                        pos_diff = position_diff(head_pos, tail_pos)
                        handle_tail_move(pos_diff, tail_pos)
                    if i + 1 == 9:
                        positions.add(tuple(tail_pos))


        elif direction == "R":
            for _ in range(amount):
                real_head[1] += 1
                for i in range(9):
                    head_pos = elements[i]
                    tail_pos = elements[i + 1]
                    if not is_touching(head_pos, tail_pos):
                        pos_diff = position_diff(head_pos, tail_pos)
                        handle_tail_move(pos_diff, tail_pos)
                    if i + 1 == 9:
                        positions.add(tuple(tail_pos))

        elif direction == "U":
            for _ in range(amount):
                real_head[0] += 1
                for i in range(9):
                    head_pos = elements[i]
                    tail_pos = elements[i + 1]
                    if not is_touching(head_pos, tail_pos):
                        pos_diff = position_diff(head_pos, tail_pos)
                        handle_tail_move(pos_diff, tail_pos)
                    if i + 1 == 9:
                        positions.add(tuple(tail_pos))

        elif direction == "D":
            for _ in range(amount):
                real_head[0] -= 1
                for i in range(9):
                    head_pos = elements[i]
                    tail_pos = elements[i + 1]
                    if not is_touching(head_pos, tail_pos):
                        pos_diff = position_diff(head_pos, tail_pos)
                        handle_tail_move(pos_diff, tail_pos)
                    if i + 1 == 9:
                        positions.add(tuple(tail_pos))
        
    return len(positions)

print("Part 1: ", part1(commands))
print("Part 2: ", part2(commands))