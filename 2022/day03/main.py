"""Module priority sum rucksack searching."""

def find_priority_sum(rucksacks):
    """
        Finds the priority sum of the items from a rucksack.

        Parameters
        ----------
            rucksacks : list[str]
                list of items in rucksacks represented by strings
    """
    priority_sum = 0

    for rucksack in rucksacks:
        priority_sum += scan_rucksack(rucksack)

    return priority_sum

def scan_rucksack(rucksack):
    """
        Scans the rucksack for the same item in both compartments

        Parameters
        ----------
            rucksack : str
                list of items in rucksack represented by characters
    """
    first_compartment = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]

    for first_item in first_compartment:
        for second_item in second_compartment:
            if first_item == second_item:
                return get_priority(first_item)
    return 0

def get_priority(char):
    """
        Finds the priority given a string alphabet character.

        Parameters
        ----------
            char : str
                an alphabet character
    """
    if char.islower():
        return ord(char)-96

    return ord(char)-65+27

def find_badge_priority_sum(rucksacks):
    """
        Finds the priority sum of the badges from a rucksack.

        Parameters
        ----------
            rucksacks : list[str]
                list of items in rucksacks represented by strings
    """
    priority_sum = 0

    chunked = list(chunk_rucksacks(rucksacks))

    for group in chunked:
        priority_sum += find_badge_for_group(group)

    return priority_sum

def find_badge_for_group(group):
    """
        Finds the priority sum of the badges from a group.

        Parameters
        ----------
            group : list[str]
                list of rucksacks in a group represented by strings
    """

    items = set()
    for rucksack in group:
        if len(items) == 0:
            items = set(rucksack)
            continue

        items = items.intersection(rucksack)

    return get_priority(items)

def chunk_rucksacks(rucksacks):
    """
        Splits the rucksacks into groups of three rucksacks.

        Parameters
        ----------
            rucksacks : list[str]
                list of rucksacks total represented by strings
    """
    for i in range(0, len(rucksacks), 3):
        yield rucksacks[i:i+3]

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(REAL, encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]

    result = find_badge_priority_sum(lines)
    print(result)
