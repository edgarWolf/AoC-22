inp_file = "8.txt"

with open(inp_file) as f:
    lines = f.read().splitlines()

def map_input(lines):
    return [list(map(int, list(l))) for l in lines]

trees = map_input(lines)

def part1(trees):
    counter = 0
    rows = len(trees)
    cols = len(trees[0])
    counter += 2 * rows + 2 * (cols - 2)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            curr_tree = trees[i][j]
            left_range = list(range(j))
            right_range = list(range(j + 1, cols))
            up_range = list(range(i))
            down_range = list(range(i + 1, cols))
            is_left_visible = is_right_visible = is_up_visible = is_down_visible = True
            for l in left_range:
                t = trees[i][l]
                if t >= curr_tree:
                    is_left_visible = False
                    break
            for r in right_range:
                t = trees[i][r]
                if t >= curr_tree:
                    is_right_visible = False
                    break
            for u in up_range:
                t = trees[u][j]
                if t >= curr_tree:
                    is_up_visible = False
                    break
            for d in down_range:
                t = trees[d][j]
                if t >= curr_tree:
                    is_down_visible = False
                    break
            if is_left_visible or is_right_visible or is_up_visible or is_down_visible:
                counter += 1
    return counter


def part2(trees):
    distances = []
    rows = len(trees)
    cols = len(trees[0])
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            curr_tree = trees[i][j]
            left_range = list(range(j))[::-1]
            right_range = list(range(j + 1, cols))
            up_range = list(range(i))[::-1]
            down_range = list(range(i + 1, cols))
            left_distance = right_distance = up_distance = down_distance = 0
            for l in left_range:
                t = trees[i][l]
                left_distance += 1
                if t >= curr_tree:
                    break
            for r in right_range:
                t = trees[i][r]
                right_distance += 1
                if t >= curr_tree:
                    break
            for u in up_range:
                t = trees[u][j]
                up_distance += 1
                if t >= curr_tree:
                    break
            for d in down_range:
                t = trees[d][j]
                down_distance += 1
                if t >= curr_tree:
                    break
            distances.append(left_distance * right_distance * up_distance * down_distance)
    return max(distances)

print(f"Part 1: {part1(trees)}")
print(f"Part 2: {part2(trees)}")
