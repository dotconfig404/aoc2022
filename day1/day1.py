# part 1

with open("input") as f:
    current_calories = calories_high = 0
    while (line := f.readline()):
        if len(line) == 1:
            if calories_high < current_calories:
                calories_high = current_calories
            current_calories = 0
        else:
            current_calories = current_calories + int(line)
    print(calories_high)