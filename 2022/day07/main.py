"""Module file system item search"""

FILESYSTEM_SIZE = 70000000
MAX_TOTAL_SIZE = 100000
INSTALLATION_SIZE = 30000000

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.type = None
        self.size = None
        self.children = {}
        self.parent = parent

def parse_lines(lines):
    root = Node("/", None)
    root.type = "dir"
    current_node = root
    for line in lines:
        result = line.split()
        if "cd" in result and "/" in result:
            current_node = root
            continue

        if "cd" in result and ".." in result:
            current_node = current_node.parent
            continue

        if "cd" in result and ".." not in result:
            result_node = Node(result[2], current_node)
            result_node.type = "dir"
            result_node.parent = current_node
            current_node.children[result_node.name] = result_node
            current_node = result_node
            continue

        if "ls" in result:
            continue

        if "dir" in result:
            continue

        result_node = Node(result[1], current_node)
        result_node.size = int(result[0])
        result_node.type = "file"
        current_node.children[result_node.name] = result_node
    return root

def add_dir_size(root):
    current_dir_size = 0
    for node in root.children.values():
        if node.type == "file":
            current_dir_size += node.size
        if node.type == "dir":
            child_node = add_dir_size(node)
            current_dir_size += child_node.size
    root.size = current_dir_size
    return root

def sum_directory_size(root, limit):
    size = 0

    if root.size <= limit:
        size = root.size

    for node in root.children.values():
        if node.type == "dir":
            size += sum_directory_size(node, limit)

    return size

def get_directories_to_delete(root, space):
    directories = []

    if root.size >= space:
        directories.append(root)
    for node in root.children.values():
        if node.type == "dir":
            directories.extend(get_directories_to_delete(node, space))

    return directories

def get_min_size(directories):
    size = FILESYSTEM_SIZE
    for dir in directories:
        if dir.size < size:
            size = dir.size
    return size

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(REAL, encoding='UTF-8') as file:
        lines = [line for line in file]

    root = parse_lines(lines)
    root = add_dir_size(root)
    unused_space = FILESYSTEM_SIZE - root.size
    directories = get_directories_to_delete(root, INSTALLATION_SIZE - unused_space)
    print(get_min_size(directories))
