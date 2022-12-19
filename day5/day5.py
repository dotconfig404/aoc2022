with open('input','r') as f:
    stacks = [[],[],[],[],[],[],[],[],[]]
    reading_layout = True
    while (line := f.readline()):
        # reading the stack layout
        if reading_layout:
            if line[1] == '1':
                reading_layout = False
                continue

            for i,c in enumerate(line):
                if ((i+3)%4 == 0) and c.isupper():
                    stacks[(i+3)//4-1].append(c)
            continue

        if line == '\n':
            continue

        # getting instruction
        instr = []
        for word in line.split():
            if word.isdigit():
                instr.append(int(word))

        # applying instruction
        for _ in range(instr[0]):
            stacks[instr[2]-1].insert(0, stacks[instr[1]-1][0])
            stacks[instr[1]-1].pop(0)

    for stack in stacks:
        print(stack)

# part 2
with open('input', 'r') as f:
    stacks = [[],[],[],[],[],[],[],[],[]]
    reading_layout = True
    while (line := f.readline()):
        # reading the stack layout
        if reading_layout:
            if line[1] == '1':
                reading_layout = False
                continue

            for i,c in enumerate(line):
                if ((i+3)%4 == 0) and c.isupper():
                    stacks[(i+3)//4-1].append(c)
            continue

        if line == '\n':
            continue

        # getting instruction
        instr = []
        for word in line.split():
            if word.isdigit():
                instr.append(int(word))

        # applying instruction
        for i in range(instr[0]):
            stacks[instr[2]-1].insert(i, stacks[instr[1]-1][0])
            stacks[instr[1]-1].pop(0)

    for stack in stacks:
        print(stack)
