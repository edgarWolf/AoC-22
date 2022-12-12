import string

inp_file = "12.txt"

with open(inp_file) as f:
    lines = f.read().splitlines()
    lines = [list(l) for l in lines]


class Node:
    def __init__(self, row, col, val) -> None:
        self.row = row
        self.col = col
        self.val = val
        self.visited = False
        self.pred = None
        self.children = []

    def __eq__(self, other: object) -> bool:
        return other is not None and self.row == other.row and self.col == other.col and self.val == other.val
    
    def get_adjacent_nodes(self, grid):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        adjacent = []
        for y_offset, x_offset in directions:
            y = self.row + y_offset
            x = self.col + x_offset
            if self._is_in_bounds(grid, y, x):
                adjacent.append(grid[y][x])
        return adjacent

    def _is_in_bounds(self, grid, i, j):
        H = len(grid)
        W = len(grid[0])
        return i >= 0 and i < H and j >= 0 and j < W  


def map_input(lines):
    letters = {char:p for p, char in enumerate(string.ascii_lowercase)}
    grid = []
    start_node = None
    target_node = None
    for i, line in enumerate(lines):
        nodes = []
        for j, val in enumerate(line):
            if val == "S":
                node = Node(i, j, letters["a"])
                start_node = node
            elif val == "E":
                node = Node(i, j, letters["z"])
                target_node = node
            else:
                node = Node(i, j, letters[val])
            nodes.append(node)
        grid.append(nodes)
    
    for row in grid:
        for n in row:
            n.children = n.get_adjacent_nodes(grid)
    return grid, start_node, target_node


def part1(start_node: Node, target_node: Node):
    # Bfs algorithm
    queue = [start_node]
    start_node.visited = True
    while True:
        if not queue:
            return 9999999 # Return some arbitrary large value, since we can't find a path for this node.
        curr = queue.pop(0)
        children = [c for c in curr.children if not c.visited and c.val - curr.val <= 1]

        for child in children:
            child.pred = curr
            child.visited = True
            queue.append(child)

        if target_node in children:
            break
        
    counter = 1
    pred = target_node.pred
    while pred.pred:
        pred = pred.pred
        counter += 1
    
    return counter


def part2(target_node: Node):
    queue = [target_node]
    target_node.visited = True
    found_node = []
    while True:
        curr = queue.pop(0)
        children = [c for c in curr.children if not c.visited and curr.val - c.val <= 1]

        for child in children:
            child.pred = curr
            child.visited = True
            queue.append(child)

        found_node = [c for c in children if c.val == 0]
        if found_node:
            found_node = found_node[0]
            break
        
    counter = 1
    pred = found_node.pred
    while pred.pred:
        pred = pred.pred
        counter += 1
    
    return counter
    
                
grid, start_node, target_node = map_input(lines)

print("Part 1: ", part1(start_node, target_node))

# Reset state of graph.
for row in grid:
        for n in row:
            n.visited = False
            n.pred = None

print("Part 2: ", part2(target_node))