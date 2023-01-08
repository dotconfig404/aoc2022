# part 1

with open("input") as f:
    score = 0
    while (line := f.readline()):
        elf = int(line[0], 13) - 9
        me = int(line[2], 36) - 32
        score += me + (((me-elf) % 3 + 1) % 3 * 3)

    print(score)

# part 2

with open("input") as f:
    score = 0
    while (line := f.readline()):
        elf_shape = int(line[0], 13) - 10
        outcome_mapping = int(line[2], 36) - 33
        outcome_score = outcome_mapping * 3
        me_shape = (elf_shape + (outcome_mapping + 2)) % 3
        score += outcome_score + me_shape + 1

    print(score)
