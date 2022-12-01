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

# part 2

import bisect
top_3 = [0,0,0]

with open("input") as f:
    current_calories = 0
    while (line := f.readline()):
        if len(line) == 1:
            if current_calories > top_3[0]:
                bisect.insort(top_3, current_calories)
                top_3.pop(0)
            current_calories = 0
        else:
            current_calories = current_calories + int(line)
    print(top_3[0] + top_3[1] + top_3[2])