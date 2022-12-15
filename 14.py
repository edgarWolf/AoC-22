from collections import defaultdict

inp_file = "14.txt"

ROCK_SYMOBL = "#"
SAND_SYMBOL = "o"
DOT_SYMBOL = "."

with open(inp_file) as f:
    paths = f.read().splitlines()


def map_input(paths):
    ret = [p.split("->") for p in paths]
    ret = [[list(map(int, p.split(","))) for p in path] for path in ret]
    ret = [[tuple(p) for p in path] for path in ret]
    return ret

def get_arr_measures(paths):
    min_x = min([min(p)[0] for p in paths])
    max_x = max([max(p)[0] for p in paths])
    max_y = max([max(p, key=lambda t: t[1])[1] for p in paths])
    return min_x, max_x, 0, max_y


def create_map(paths):
    sand_map = defaultdict(lambda: DOT_SYMBOL)
    sand_map[(0, 500)] = DOT_SYMBOL

    for path in paths:
        for i  in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]

            if x1 != x2:
                g = max(x1, x2)
                m = min(x1, x2)
                for k in range(m, g + 1):
                    sand_map[(y1, k)] = ROCK_SYMOBL
            if y1 != y2:
                g = max(y1, y2)
                m = min(y1, y2)
                for k in range(m, g + 1):
                    sand_map[(k, x1)] = ROCK_SYMOBL
    return sand_map




def in_bounds(pos, W, H):
    y, x = pos
    return 0 <= y <= H and 0 <= x <= W


def is_blocked(sand_map, pos, W, H):
    y, x = pos
    dy, dx = (y + 1, x)
    if in_bounds((dy, dx), W, H) and (sand_map[(dy, dx)] == ROCK_SYMOBL or sand_map[(dy, dx)] == SAND_SYMBOL):
        dy, dx = (y + 1, x - 1)
        if in_bounds((dy, dx), W, H) and (sand_map[(dy, dx)] == ROCK_SYMOBL or sand_map[(dy, dx)] == SAND_SYMBOL):
            dy, dx = (y + 1, x + 1)
            if in_bounds((dy, dx), W, H) and (sand_map[(dy, dx)] == ROCK_SYMOBL or sand_map[(dy, dx)] == SAND_SYMBOL):
                return True
    return False

def is_horizontal_blocked(sand_map, pos, H):
    y, x = pos
    dy, dx = (y + 1, x)
    if 0 <= dy <= H and (sand_map[(dy, dx)] == ROCK_SYMOBL or sand_map[(dy, dx)] == SAND_SYMBOL):
        dy, dx = (y + 1, x - 1)
        if 0 <= dy <= H and (sand_map[(dy, dx)] == ROCK_SYMOBL or sand_map[(dy, dx)] == SAND_SYMBOL):
            dy, dx = (y + 1, x + 1)
            if 0 <= dy <= H and (sand_map[(dy, dx)] == ROCK_SYMOBL or sand_map[(dy, dx)] == SAND_SYMBOL):
                return True
    return False



def part1(sand_map, W, H):
    counter = 0
    y = 0
    x = 500
    while True:
        if is_blocked(sand_map, (y, x), W, H):
            sand_map[(y, x)] = SAND_SYMBOL
            counter += 1
            # Reset sand pos
            y = 0
            x = 500
        else:

            is_in_bounds = in_bounds((y + 1, x), W, H)
            if not is_in_bounds:
                break 

            is_down_free = sand_map[(y + 1, x)] == DOT_SYMBOL
            if is_down_free:
                y += 1
                continue

            is_in_bounds = in_bounds((y + 1, x - 1), W, H)
            if not is_in_bounds:
                break

            is_left_free = sand_map[(y + 1, x - 1)]== DOT_SYMBOL
            if is_left_free:
                y += 1
                x -= 1
                continue

            is_in_bounds = in_bounds((y + 1, x + 1), W, H)
            if not is_in_bounds:
                break

            is_right_free = sand_map[(y + 1, x + 1)] == DOT_SYMBOL
            if is_right_free:
                y += 1
                x += 1
                continue
                        
    return counter


def part2(sand_map, H):
    counter = 0
    y, x = 0, 500
    max_depth = H + 2

    while True:

        # Break condition.
        if sand_map[(0, 500)] == SAND_SYMBOL:
            break
        
        # Add bottom rock line if hit max_depth
        if y + 1 == max_depth:
            sand_map[(y + 1, x)] = ROCK_SYMOBL
            sand_map[(y + 1, x - 1)] = ROCK_SYMOBL
            sand_map[(y + 1, x + 1)] = ROCK_SYMOBL

        if is_horizontal_blocked(sand_map, (y, x), max_depth):
            sand_map[(y, x)] = SAND_SYMBOL
            counter += 1
            # Reset sand pos
            y = 0
            x = 500

        else:
            is_down_free = y + 1 < max_depth and sand_map[(y + 1, x)] == DOT_SYMBOL
            if is_down_free:
                y += 1
                continue

            is_left_free = y + 1 < max_depth and sand_map[(y + 1, x - 1)] == DOT_SYMBOL
            if is_left_free:
                y += 1
                x -= 1
                continue

            is_right_free = y + 1 < max_depth and sand_map[(y + 1, x + 1)] == DOT_SYMBOL
            if is_right_free:
                y += 1
                x += 1
                continue

    return counter
    

paths = map_input(paths)
min_x, max_x, min_y, max_y = get_arr_measures(paths)



sand_map = create_map(paths)
print("Part 1:", part1(sand_map, max_x, max_y))
sand_map = create_map(paths)
print("Part 2:", part2(sand_map, max_y))

