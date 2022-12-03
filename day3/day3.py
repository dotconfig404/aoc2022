# part 1

with open("input") as f:
    sum = 0
    while (line := f.readline()):
        compartment1 = line[0:len(line)//2]
        compartment2 = line[len(line)//2:len(line)]
        for item in compartment1:
            if item in compartment2:
                if item.islower():
                    print(item,ord(item) - 96)
                    sum = sum + ord(item) - 96
                else:
                    print(item,ord(item) - 64 + 26)
                    sum = sum + ord(item) - 64 + 26
    print(sum)

# part 2

