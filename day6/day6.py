# part 1
f = open('input', 'r')

marker = []
marker.append(f.read(1))
marker.append(f.read(1))
marker.append(f.read(1))
marker.append(f.read(1))
marker_end = 4
marker_positions = []
while (char := f.read(1)):
    not_marker = False
    for i,c in enumerate(marker):
        if not_marker:
            break

        if i == 3:
            marker_positions.append(marker_end)

        for d in marker[i+1:]:
            if c == d:
                not_marker = True

    marker_end = marker_end + 1
    marker.append(char)
    marker.pop(0)

print(marker_positions[0])
f.close()


# part 2
f = open('input', 'r')

marker = []
for _ in range(14):
    marker.append(f.read(1))
marker_end = 14
marker_positions = []
while (char := f.read(1)):
    not_marker = False
    for i,c in enumerate(marker):
        if not_marker:
            break

        if i == 13:
            marker_positions.append(marker_end)

        for d in marker[i+1:]:
            if c == d:
                not_marker = True

    marker_end = marker_end + 1
    marker.append(char)
    marker.pop(0)

print(marker_positions[0])
f.close()
