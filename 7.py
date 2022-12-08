inp_file = "7.txt"

# Recursive structures
class FileElement:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size


class DirectoryElement(FileElement):
    def __init__(self, name, parent) -> None:
        super().__init__(name, 0)
        self.parent = parent
        self.files = {}
    
    def add_file(self, f):
        self.files[f.name] = f
    
    def get_parent(self):
        return self.parent
    
    def get_size(self):
        return sum(f.get_size() for f in self.files.values())
    
    def get_subfolder(self, name):
        return self.files[name]
        

with open(inp_file) as f:
    lines = f.read().splitlines()


def map_input(lines):
    commands = [l.replace("$", "").strip() for l in lines]
    commands = [l for l in commands if l != "ls"]
    root = DirectoryElement("/", parent=None)
    directories = [root]
    current = root
    for command in commands[1:]:
        if command.startswith("cd"):
            _, to = command.split()
            if to == "..":
                current = current.get_parent()
            else:
                current = current.get_subfolder(to)
        elif command.startswith("dir"):
            dir_name = command[4:]
            directory = DirectoryElement(dir_name, parent=current)
            current.add_file(directory)
            directories.append(directory)
        elif command[0].isdigit():
            size, name = command.split()
            f = FileElement(name, int(size))
            current.add_file(f)
    return directories


directories = map_input(lines)
    
def part1(directories):
    sizes = [d.get_size() for d in directories]
    sizes = [s for s in sizes if s <= 100000]
    return sum(sizes)

def part2(directories):
    total_space = 70000000
    needed_space = 30000000
    root = directories[0]
    current_total_space = root.get_size()
    current_free_space = total_space - current_total_space
    current_diff_space = needed_space - current_free_space
    options = []
    for directory in directories[1:]:
        curr_space = directory.get_size()
        if curr_space >= current_diff_space:
            options.append(curr_space)
    return min(options)


print(f"Part 1: {part1(directories)}")
print(f"Part 2: {part2(directories)}")