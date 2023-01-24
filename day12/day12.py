topo = []
f = open('input','r')
row = 0
start = end = (-1,-1)
while (line := f.readline()):
    topo.append([])
    for col, c in enumerate(line):
        if c == '\n':
            break
        if c == 'S':
            topo[row].append(ord('a'))
            start = (row, col)
        elif c == 'E':
            topo[row].append(ord('z'))
            end = (row, col)
        else:
            topo[row].append(ord(c))
    row = row + 1
f.close()

searched = [(20, 1)]
neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def is_valid_pos(r, c):
    if r < 0 or c < 0:
        return False
    elif r >= len(topo)-1 or c >= len(topo[r])-1:
        return False
    elif topo[r][c] == -1:
        return False
    return True

def is_valid_new_pos(old_pos, current_pos, new_pos):
    r1,c1 = old_pos
    r2,c2 = current_pos
    r3,c3 = new_pos

    if topo[r2][c2] + 1 < topo[r3][c3]:
        return False
    elif r1 == r3 and c1 == c3:
        return False
    if searched[r3][c3] == 3:
        return True
    elif searched[r3][c3] != 0:
        return False
    return True
import curses
screen = curses.initscr()

# Changes go in to the screen buffer and only get
# displayed after calling `refresh()` to update

curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)

def print_map(pos, new_pos, lvl):
    for i, row in enumerate(topo):
        for j, c in enumerate(row):
            if searched[i][j] == 1:
                screen.addch(i,j,chr(c), curses.color_pair(3))
            elif searched[i][j] == 2:
                screen.addch(i,j,chr(c), curses.color_pair(2))
            elif searched[i][j] == 3:
                screen.addch(i,j,chr(c), curses.color_pair(1))
            else:
                screen.addch(i,j,chr(c))
    screen.addstr(len(topo),0, "lvl"+ str(lvl))
    screen.addstr(len(topo) + 1, 0, "searching from " + str(pos) + " to " + str(new_pos))
    screen.refresh()

def print_map_vertically(pos, new_pos, lvl):
    for i, row in enumerate(topo):
        for j, c in enumerate(row):
            if searched[i][j] == 1:
                screen.addch(j,i,chr(c), curses.color_pair(3))
            elif searched[i][j] == 2:
                screen.addch(j,i,chr(c), curses.color_pair(2))
            elif searched[i][j] == 3:
                screen.addch(j,i,chr(c), curses.color_pair(1))
            else:
                screen.addch(j,i,chr(c))
    screen.addstr(len(topo),0, "lvl"+ str(lvl))
    screen.addstr(len(topo) + 1, 0, "searching from " + str(pos) + " to " + str(new_pos))
    screen.refresh()

import time
ti = 0.007
searched = [[0 for c in row] for row in topo]
searched[end[0]][end[1]] = 3
searched[start[0]][start[1]] = 2
def find_path(prev_pos, pos, lvl=0):
    lvl = lvl + 1
    r,c = pos[0],pos[1]
    # filtering locations
    new_positions = [(r + dr, c + dc) for dr, dc in neighbours if is_valid_pos(r + dr, c + dc)]
    new_positions = [(r,c) for r,c in new_positions if is_valid_new_pos(prev_pos, pos, (r,c))]


    # new positions blue
    for r,c in new_positions:
        searched[r][c] = 1

    if r == end[0] and c == end[1]:
        time.sleep(100)
    else:
        for new_pos in new_positions:
            time.sleep(ti)
            # current position green
            searched[new_pos[0]][new_pos[1]] = 2
            print_map_vertically(pos, new_pos, lvl)
            find_path(pos, new_pos, lvl)

x,y = 20, 20
heigh = 6
width = 40
win = curses.newwin(heigh, width, y,x)
#time.sleep(10000)

find_path(start, start)
curses.endwin()
