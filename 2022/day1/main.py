"""Module most_calories printing sum of calories."""

def most_calories(calories_list):
    """
        Finds the sum of the calories carried by the elf carrying the most calories.

        Parameters
        ----------
            calories_list : list[str]
                list of parsed calories
    """

    max_calories = 0
    running_max = 0

    for line in calories_list:
        if not line:
            if running_max > max_calories:
                max_calories = running_max

            # reset the running maximum for the next set of calories
            running_max = 0

            continue
        running_max += int(line)

    return max_calories

if __name__ == '__main__':
    with open('input.txt', encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]

        RESULT = most_calories(lines)
        print(RESULT)
