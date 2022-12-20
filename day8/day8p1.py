# part 1
f = open('input', 'r')
forest = []
while (line := f.readline()):
    row = [int(c) for c in line if c.isnumeric()]
    forest.append(row)
f.close()

left = []
right = []
for y, row in enumerate(forest):

# from left
    prev_t = -1
    for x, t in enumerate(row):
        if t > prev_t:
            left.append((x,y))
            prev_t = t

# from right
    prev_t = -1
    for x, t in enumerate(reversed(row)):
        if t > prev_t:
            right.append((98-x,y))
            prev_t = t


total = left + right

# transposing
forest = [[row[n] for row in forest] for n, _ in enumerate(forest)]

left = []
right = []
for y, row in enumerate(forest):

# from left
    prev_t = -1
    for x, t in enumerate(row):
        if t > prev_t:
            left.append((y,x))
            prev_t = t

# from right
    prev_t = -1
    for x, t in enumerate(reversed(row)):
        if t > prev_t:
            right.append((y,98-x))
            prev_t = t

total = total + left + right
print(len(set(total)))

