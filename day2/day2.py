# part 1

with open("input") as f:
    score = 0
    while (line := f.readline()):
        if line[0] == "A":
            if line[2] == "X":
                score = score + 1 + 3
            elif line[2] == "Y":
                score = score + 2 + 6
            elif line[2] == "Z":
                score = score + 3

        elif line[0] == "B":
            if line[2] == "X":
                score = score + 1
            elif line[2] == "Y":
                score = score + 2 + 3
            elif line[2] == "Z":
                score = score + 3 + 6

        elif line[0] == "C":
            if line[2] == "X":
                score = score + 1 + 6
            elif line[2] == "Y":
                score = score + 2
            elif line[2] == "Z":
                score = score + 3 + 3

    print(score)

# part 2

with open("input") as f:
    score = 0
    while (line := f.readline()):
        if line[0] == "A":
            if line[2] == "X":
                score = score + 0 + 3
            elif line[2] == "Y":
                score = score + 3 + 1
            elif line[2] == "Z":
                score = score + 6 + 2

        elif line[0] == "B":
            if line[2] == "X":
                score = score + 0 + 1
            elif line[2] == "Y":
                score = score + 3 + 2
            elif line[2] == "Z":
                score = score + 6 + 3

        elif line[0] == "C":
            if line[2] == "X":
                score = score + 0 + 2
            elif line[2] == "Y":
                score = score + 3 + 3
            elif line[2] == "Z":
                score = score + 6 + 1

    print(score)
