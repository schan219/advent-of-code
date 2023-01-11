"""Module cleaning schedule."""

def check_pairs_contain(assignments):
    """
        Loops through the assignments and checks the pairs.

        Parameters
        ----------
            assignments : list[str]
                list of range of numbers represented by string
    """
    num_encapsulating_ranges = 0
    for pairs in assignments:
        arr = pairs.split(",")
        if fully_contains(arr[0], arr[1]):
            num_encapsulating_ranges += 1
    return num_encapsulating_ranges

def fully_contains(first_range, second_range):
    """
        Checks if one range fully contains the other.

        Parameters
        ----------
            first_range : str
                range of numbers represented by string

            second_range : str
                range of numbers represented by string
    """
    first_range_list = first_range.split("-")
    second_range_list = second_range.split("-")
    first_pair_min = int(first_range_list[0])
    first_pair_max = int(first_range_list[1])
    second_pair_min = int(second_range_list[0])
    second_pair_max = int(second_range_list[1])

    if first_pair_min <= second_pair_min <= second_pair_max <= first_pair_max:
        return True

    if second_pair_min <= first_pair_min <= first_pair_max <= second_pair_max:
        return True

    return False

def check_pairs_overlap(assignments):
    """
        Loops through the assignments and checks the pairs if there is overlap.

        Parameters
        ----------
            assignments : list[str]
                list of range of numbers represented by string
    """
    num_overlapping_ranges = 0
    for pairs in assignments:
        arr = pairs.split(",")
        if overlaps(arr[0], arr[1]):
            num_overlapping_ranges += 1
    return num_overlapping_ranges

def overlaps(first_range, second_range):
    """
        Checks if the ranges overlaps.

        Parameters
        ----------
            first_range : str
                range of numbers represented by string

            second_range : str
                range of numbers represented by string
    """
    first_range_list = first_range.split("-")
    second_range_list = second_range.split("-")
    first_pair_min = int(first_range_list[0])
    first_pair_max = int(first_range_list[1])
    second_pair_min = int(second_range_list[0])
    second_pair_max = int(second_range_list[1])

    if first_pair_min <= second_pair_min <= first_pair_max:
        return True

    if first_pair_min <= second_pair_max <= first_pair_max:
        return True

    if second_pair_min <= first_pair_min <= second_pair_max:
        return True

    if second_pair_min <= first_pair_max <= second_pair_max:
        return True

    return False

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(REAL, encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]

    RESULT = check_pairs_overlap(lines)
    print(RESULT)
