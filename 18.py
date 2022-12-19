inp_file = "18.txt"

with open(inp_file) as f:
    lines = f.read().splitlines()


def map_input(lines):
    ret = []
    for line in lines:
        x, y, z = list(map(int, line.split(",")))
        ret.append((x, y, z))
    return ret

def get_adjacent_coords(coords):
    x, y, z = coords
    # X
    x_left_adj = (x - 1, y, z)
    x_right_adj = (x + 1, y, z)

    # Y
    y_down_adj = (x, y - 1, z)
    y_up_adj = (x, y + 1, z)

    # Z
    z_adj_near = (x, y, z - 1)
    z_adj_away = (x, y, z + 1)

    return [x_left_adj, x_right_adj, y_down_adj, y_up_adj, z_adj_near, z_adj_away]
    
coords = map_input(lines)


def part1(coords_list):
    areas = [6 for  _ in coords_list]
    for i, coord in enumerate(coords_list):
        adjacent = get_adjacent_coords(coord)
        contained = [c for c in coords_list if c in adjacent]
        areas[i] -= len(contained)
    return sum(areas)

def part2(coords_list):
    all_cubes = {}
    min_val = -1
    max_val = 21
    for x in range(min_val, max_val):
        for y in range(min_val, max_val):
            for z in range(min_val, max_val):
                if (x, y, z) not in coords_list:
                    all_cubes[(x, y, z)] = False
    start = (-1, -1, -1)
    cube_queue = [start]
    while cube_queue:
        coord = cube_queue.pop(0)
        all_cubes[coord] = True
        adj = [a for a in get_adjacent_coords(coord) if a in all_cubes and not all_cubes[a] and a not in cube_queue]
        for a in adj:
                cube_queue.append(a)

    cubes_flooded = [c for c in all_cubes if not all_cubes[c]]
    return part1(coords_list) - part1(cubes_flooded)



print("Part 1:", part1(coords))
print("Part 2:", part2(coords))