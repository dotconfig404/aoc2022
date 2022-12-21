# part 1
f = open('input', 'r')

x = 1
cycle = 0
signal_strength = 0
while (line := f.readline()):
    line = line.split()
    cycle = cycle + 1
    if (cycle + 20) % 40 == 0 and cycle <= 220:
       signal_strength = signal_strength + x*cycle

    if len(line) > 1:
        cycle = cycle + 1
        if (cycle + 20) % 40 == 0 and cycle <= 220:
            signal_strength = signal_strength + x*cycle
        x = x + int(line[1])

f.close()

print(signal_strength)


# part 2
import math
screen = [[False for pixel in range(40)] for row in range(6)]
def print_screen():
    for row in screen:
        for pixel in row:
            if pixel:
                print('#', end='')
            else:
                print('.', end='')
        print()

def draw_pixel(cycle, x):
    pixel_col = cycle % 40
    pixel_row = cycle // 40 % 6
    if pixel_col == x - 1 or pixel_col == x or pixel_col == x + 1:
        screen[pixel_row][pixel_col] = True

f = open('input', 'r')

x = 1
cycle = 0
signal_strength = 0
while (line := f.readline()):
    line = line.split()
    cycle = cycle + 1
    draw_pixel(cycle, x)

    if len(line) > 1:
        cycle = cycle + 1
        x = x + int(line[1])
        draw_pixel(cycle, x)

f.close()

print_screen()
