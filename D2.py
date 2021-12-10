with open("input.txt") as f:
    inp = f.read().split("\n")


def part1(inp):
    d = 0
    h = 0
    for i in inp:
        t = i.split()
        if t[0][0] == "f":
            h += int(t[1])
        elif t[0][0] == "d":
            d += int(t[1])
        else:
            d -= int(t[1])
    print(h * d)


def part2(inp):
    d = 0
    h = 0
    aim = 0
    for i in inp:
        t = i.split()
        if t[0][0] == "f":
            h += int(t[1])
            d += aim * int(t[1])
        elif t[0][0] == "d":
            aim += int(t[1])
        else:
            aim -= int(t[1])
    print(h * d)


part1(inp)
part2(inp)
