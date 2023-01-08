# part 1

with open("input") as f:
    sum = 0
    while (line := f.readline()):
        compartment1 = line[0:len(line)//2]
        compartment2 = line[len(line)//2:len(line)]
        for item in compartment1:
            if item in compartment2:
                sum += (ord(item) - 96) % 58
                break
    print(sum)

# part 2

with open("input") as f:
    sum = 0

    group_counter = 0
    badges = []
    group = []

    while (line := f.readline()):
        group_counter = group_counter + 1
        group.append(line)

        if group_counter % 3 == 0:
            for item in group[0]:
                if item in group[1]:
                    if item in group[2]:
                        badges.append(item)
                        group = []
                        group_counter = 0
                        break

    for badge in badges:
        sum += (ord(badge) - 96) % 58
    print(sum)
