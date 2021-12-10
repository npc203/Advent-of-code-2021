with open("input.txt") as f:
    inp = f.read().split("\n")


def part1(inp):
    fin = 0
    prev = None
    for i in inp:
        x = int(i)
        if prev and x > prev:
            fin += 1
        prev = x
    print(fin)


def part2(inp):
    inp = [int(i) for i in inp]
    proc = []
    for i in range(0, len(inp) - 2):
        proc.append(inp[i] + inp[i + 1] + inp[i + 2])
    part1(proc)


part1(inp)
part2(inp)
