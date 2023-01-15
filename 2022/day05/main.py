"""Module crate stacking."""

import re

def parse(lines):
    num_stacks = len(lines[0])//4
    new_list = [[] for x in range(num_stacks)]
    for _, line in enumerate(lines):
        if '[' in line:
            new_list = create_stacks(line, new_list, num_stacks)
        elif line[0:2].strip().isdigit():
            continue
        elif line[0] == '\n':
            continue
        elif line[0:4] == 'move':
            new_list = execute_moves(line, new_list)
    top_crates = get_top_crates(new_list)
    return top_crates

def create_stacks(line, stacks, num_stacks):
    elements = get_elements(line) # ['0','D','0']
    for i in range(0, num_stacks):
        if elements[i].isalpha():
            stacks[i].insert(0, elements[i])

    return stacks

def get_elements(line):
    stack = list()
    for i in range(0, len(line), 4):
        current_range = line[i:i+4]
        if '[' in current_range:
            element = current_range.strip('[] \n')
            stack.append(element)
            continue
        stack.append('0')
    return stack

def execute_moves(line, stacks):
    # number of crates moved, src, dst
    instructions = re.split(r'\D+', line)
    num_crates = int(instructions[1])
    src = int(instructions[2])
    dst = int(instructions[3])

    for _ in range(0, num_crates):
        element = stacks[src-1].pop()
        stacks[dst-1].append(element)
    return stacks

def get_top_crates(stacks):
    top_crates = ""
    for stack in stacks:
        top_crates += stack[-1]

    return top_crates

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(TEST, encoding='UTF-8') as file:
        lines = [line for line in file]

    RESULT = parse(lines)
    print(RESULT)
