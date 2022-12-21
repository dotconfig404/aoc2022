class Monkey():
    def __init__(self):
        self.items = []
        self.operation = None
        self.test = None
        self.inspect_times = 0

    def addItem(self, item):
        self.items.append(item)

    def setOperation(self, operation):
        self.operation = operation

    def setTest(self, test):
        self.test = test

    def playWith(self, monkeys):
        for _ in range(len((self.items))):
            worry = self.operation(self.items[0])
            self.inspect_times = self.inspect_times + 1
            dest = self.test(worry)
            monkeys[dest].addItem(worry)
            self.items.pop(0)


monkeys = []
divisor = -1
true_outcome = -1
false_outcome = -1
f = open('input', 'r')

while (line := f.readline()):
    line = line.split()

    if len(line) == 0:
        continue

    elif line[0] == 'Monkey':
        monkey = Monkey()

    elif line[0] == 'Starting':
        for i in range(2, len(line)):
            monkey.addItem(int(line[i].strip(',')))

    elif line[0] == 'Operation:':
        if line[5].isnumeric():
            arg = int(line[5])
            if line[4] == '+':
                monkey.setOperation(lambda x,a=arg: (x + a) // 3)
            else:
                monkey.setOperation(lambda x,a=arg: x * a // 3)
        else:
            monkey.setOperation(lambda x: x * x // 3)

    elif line[0] == 'Test:':
        divisor = int(line[3])

    elif line[1] == 'true:':
        true_outcome = int(line[5])

    elif line[1] == 'false:':
        false_outcome = int(line[5])
        monkey.setTest(lambda x, t=true_outcome, d=divisor,
            f=false_outcome: t if x % d == 0 else f)
        monkeys.append(monkey)

f.close()

for _ in range(20):
    for monkey in monkeys:
        monkey.playWith(monkeys)

inspect_times = []
for monkey in monkeys:
    inspect_times.append(monkey.inspect_times)

inspect_times.sort()
print(inspect_times[len(inspect_times)-2]*inspect_times[len(inspect_times)-1])

# part 2
# huge numbers incoming. idea: manage using them using mod division with the least common multiple
class Monkey():
    def __init__(self):
        self.items = []
        self.operation = None
        self.test = None
        self.inspect_times = 0
        self.gcd = 1

    def addItem(self, item):
        self.items.append(item)

    def setOperation(self, operation):
        self.operation = operation

    def setTest(self, test):
        self.test = test

    def playWith(self, monkeys):
        for _ in range(len((self.items))):
            self.inspect_times = self.inspect_times + 1
            worry = self.operation(self.items[0])
            dest = self.test(worry)
            monkeys[dest].addItem(worry % lcm)
            self.items.pop(0)

    def setLcm(self, lcm):
        self.lcm = lcm

monkeys = []
divisor = -1
divisors = []
true_outcome = -1
false_outcome = -1
f = open('input', 'r')

while (line := f.readline()):
    line = line.split()

    if len(line) == 0:
        continue

    elif line[0] == 'Monkey':
        monkey = Monkey()

    elif line[0] == 'Starting':
        for i in range(2, len(line)):
            monkey.addItem(int(line[i].strip(',')))

    elif line[0] == 'Operation:':
        if line[5].isnumeric():
            arg = int(line[5])
            if line[4] == '+':
                monkey.setOperation(lambda x,a=arg: x + a)
            else:
                monkey.setOperation(lambda x,a=arg: x * a)
        else:
            monkey.setOperation(lambda x: x * x)

    elif line[0] == 'Test:':
        divisor = int(line[3])
        divisors.append(divisor)

    elif line[1] == 'true:':
        true_outcome = int(line[5])

    elif line[1] == 'false:':
        false_outcome = int(line[5])
        monkey.setTest(lambda x, t=true_outcome, d=divisor,
            f=false_outcome: t if x % d == 0 else f)
        monkeys.append(monkey)

f.close()

lcm = 1
for divisor in divisors:
    lcm = lcm * divisor

for monkey in monkeys:
    monkey.setLcm(lcm)

for _ in range(10000):
    for monkey in monkeys:
        monkey.playWith(monkeys)

inspect_times = []
for monkey in monkeys:
    inspect_times.append(monkey.inspect_times)

inspect_times.sort()
print(inspect_times[len(inspect_times)-2]*inspect_times[len(inspect_times)-1])

