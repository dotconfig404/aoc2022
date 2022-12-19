class Direc:
    def __init__(self, parent, name):
        self.parent = parent
        self.size = 0
        self.subs = []
        self.name = name

    def addSub(self, sub):
        self.subs.append(sub)

    def setSize(self, size):
        self.size = size

    def getSub(self, sub_direc):
        for direc in self.subs:
            if sub_direc == direc.name:
                return direc
        new_sub = Direc(self, sub_direc)
        self.addSub(new_sub)
        return new_sub

f = open('input', 'r')

root_root = Direc(None,None)
active_direc = root_root
while (line := f.readline()):
    # changing direc, creates directory if not found in subs
    if line[0:4] == "$ cd":
        if line[5:] == "..\n":
            active_direc = active_direc.parent
            continue

        active_direc = active_direc.getSub(line[5:])
        continue

    # interpreting ls output (ls is ignored)
    content = line.split()
    if content[0].isnumeric():
        active_direc.setSize(active_direc.size + int(content[0]))

f.close()

# part 1
def getSumAndTotalSize(sum, direc):
    total_size = direc.size
    for sub in direc.subs:
        sum, sub_size = getSumAndTotalSize(sum, sub)
        total_size = total_size + sub_size
    if total_size <= 100000:
        sum = sum + total_size
    return sum, total_size

print(getSumAndTotalSize(0,root_root.subs[0])[0])

# part 2
def getAllSizes(sizes, direc):
    total_size = direc.size
    for sub in direc.subs:
        sizes, sub_size = getAllSizes(sizes, sub)
        total_size = total_size + sub_size
    sizes.append(total_size)
    return sizes, total_size

sizes = getAllSizes([], root_root.subs[0])[0]
space_to_free = 30000000+sizes[len(sizes)-1]-70000000

target = sizes[len(sizes)-1]
for size in sizes:
    if size >= space_to_free and target >= size:
        target = size

print(target)
