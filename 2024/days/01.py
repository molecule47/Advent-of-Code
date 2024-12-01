with open('../data/01.txt') as file:
    inputs = [_ for _ in file.read().strip().split('\n')]

left = []
right = []
for line in inputs:
    l, r = line.split('   ')
    left.append(int(l))
    right.append(int(r))


def part1():
    sright = sorted(right)
    sleft = sorted(left)

    diffs = []
    for i in range(len(sleft)):
        if sright[i] > sleft[i]:
            diff = sright[i] - sleft[i]
        else:
            diff =  sleft[i] - sright[i]
        diffs.append(diff)

    print(sum(diffs))


def part2():
    sims = []
    for dig in left:
        count = 0
        for simd in right:
            if dig == simd:
                count += 1
        sim = dig * count
        sims.append(sim)

    print(sum(sims))


part1() # part 1
part2() # part 2