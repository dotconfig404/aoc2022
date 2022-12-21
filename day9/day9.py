from math import dist

def follow(h, t):
    for i in range(len(h)):
        if h[i] > t[i] + 1:
            t[i] = t[i] + 1
            if h[(i+1)%2] > t[(i+1)%2]:
                t[(i+1)%2] = t[(i+1)%2] + 1
            if h[(i+1)%2] < t[(i+1)%2]:
                t[(i+1)%2] = t[(i+1)%2] - 1
        elif h[i] < t[i] - 1:
            t[i] = t[i] - 1
            if h[(i+1)%2] > t[(i+1)%2]:
                t[(i+1)%2] = t[(i+1)%2] + 1
            if h[(i+1)%2] < t[(i+1)%2]:
                t[(i+1)%2] = t[(i+1)%2] - 1
    return t


f = open('input', 'r')
h = [0,0]
t = [0,0]
squares = {tuple(t)}
while (line := f.readline()):
    l = line.split()

    if l[0] == "U":
        for i in range(int(l[1])):
            h[1] = h[1] + 1
            if dist(h,t) > 1:
                t = follow(h,t)
                squares.add(tuple(t))

    elif l[0] == "D":
        for i in range(int(l[1])):
            h[1] = h[1] - 1
            if dist(h,t) > 1:
                t = follow(h,t)
                squares.add(tuple(t))


    elif l[0] == "R":
        for i in range(int(l[1])):
            h[0] = h[0] + 1
            if dist(h,t) > 1:
                t = follow(h,t)
                squares.add(tuple(t))


    elif l[0] == "L":
        for i in range(int(l[1])):
            h[0] = h[0] - 1
            if dist(h,t) > 1:
                t = follow(h,t)
                squares.add(tuple(t))

f.close()


print(len(squares))

# part 2
# ok, so were doing snake basically. yea im just gonna spaghetti my other solution until it works ¯\_(ツ)_/¯
f = open('input', 'r')
snake = [[0,0] for i in range(10)]
squares = {tuple(snake[1])}
while (line := f.readline()):
    l = line.split()

    if l[0] == "U":
        for i in range(int(l[1])):
            snake[0][1] = snake[0][1] + 1
            for j in range(1,len(snake)):
                if dist(snake[j-1], snake[j]) > 1:
                    snake[j] = follow(snake[j-1], snake[j])
                    if j == len(snake)-1:
                        squares.add(tuple(snake[j]))

    elif l[0] == "D":
        for i in range(int(l[1])):
            snake[0][1] = snake[0][1] - 1
            for j in range(1,len(snake)):
                if dist(snake[j-1], snake[j]) > 1:
                    snake[j] = follow(snake[j-1], snake[j])
                    if j == len(snake)-1:
                        squares.add(tuple(snake[j]))


    elif l[0] == "R":
        for i in range(int(l[1])):
            snake[0][0] = snake[0][0] + 1
            for j in range(1,len(snake)):
                if dist(snake[j-1], snake[j]) > 1:
                    snake[j] = follow(snake[j-1], snake[j])
                    if j == len(snake)-1:
                        squares.add(tuple(snake[j]))


    elif l[0] == "L":
        for i in range(int(l[1])):
            snake[0][0] = snake[0][0] - 1
            for j in range(1,len(snake)):
                if dist(snake[j-1], snake[j]) > 1:
                    snake[j] = follow(snake[j-1], snake[j])
                    if j == len(snake)-1:
                        squares.add(tuple(snake[j]))

f.close()

print(len(squares))
# definitly could be refactored... maybe later (read: never)
