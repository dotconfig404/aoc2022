f = open('input', 'r')
forest = []
while (line := f.readline()):
    row = [int(c) for c in line if c.isnumeric()]
    forest.append(row)
f.close()

scores = [[0 for _ in forest[0]] for _ in forest]

for row in range(len(forest)):
    for col in range(len(forest[0])):

        # checking left view
        lcol_score = 0
        for lcol in range(col - 1, -1, -1):
            lcol_score = lcol_score + 1
            if forest[row][col] <= forest[row][lcol]:
                break

        # checking right view
        rcol_score = 0
        for rcol in range(col + 1, len(forest[0])):
            rcol_score = rcol_score + 1
            if forest[row][col] <= forest[row][rcol]:
               break

        # checking upper view
        urow_score = 0
        for urow in range(row - 1, -1, -1):
            urow_score = urow_score + 1
            if forest[row][col] <= forest[urow][col]:
               break

        # checking lower view
        lrow_score = 0
        for lrow in range(row + 1, len(forest)):
            lrow_score = lrow_score + 1
            if forest[row][col] <= forest[lrow][col]:
               break

        scores[row][col] = lcol_score * rcol_score * urow_score * lrow_score

print(max([max(row) for row in scores]))
