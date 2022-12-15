def mostCalories(caloriesList):
    maxCalories = 0
    runningMax = 0

    for line in caloriesList:
        if line == '':
            if runningMax > maxCalories:
                maxCalories = runningMax

            # reset the running maximum for the next set of calories
            runningMax = 0

            continue
        
        runningMax += int(line)

    return maxCalories

if __name__ == '__main__':
    with open('input.txt') as file:
        lines = [line.rstrip() for line in file]

        result = mostCalories(lines)
        print(result)
