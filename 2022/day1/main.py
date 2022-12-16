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

    if running_max > 0 and running_max > max_calories:
        max_calories = running_max

    return max_calories

def top_three_most_calories(calories_list):
    """
        Finds the sum of the calories carried by the top three elves carrying the most calories.

        Parameters
        ----------
            calories_list : list[str]
                list of parsed calories
    """

    first_max_calories = 0
    second_max_calories = 0
    third_max_calories = 0
    running_max = 0

    for line in calories_list:
        if not line:
            # code to determine which max calories variable to store in.
            arr = [third_max_calories, second_max_calories, first_max_calories]
            arr = sorted(arr, reverse=True)

            first_max_calories = arr[0]
            second_max_calories = arr[1]
            third_max_calories = arr[2]

            if running_max > arr[2]:
                third_max_calories = running_max

            running_max = 0

            continue

        running_max += int(line)

    if running_max > 0:
            arr = [third_max_calories, second_max_calories, first_max_calories]
            arr = sorted(arr, reverse=True)

            first_max_calories = arr[0]
            second_max_calories = arr[1]
            third_max_calories = arr[2]

            if running_max > arr[2]:
                third_max_calories = running_max


    return first_max_calories + second_max_calories + third_max_calories

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(REAL, encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]

        RESULT = most_calories(lines)
        print(RESULT)

        RESULT = top_three_most_calories(lines)
        print(RESULT)
