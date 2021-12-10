with open("input.txt") as f:
    inp = f.read().split("\n")


def calc_fuel_p1(pos, place):
    fuel = 0
    for crab in pos:
        fuel += abs(crab - place)
    return fuel


def calc_fuel_p2(pos, place):
    fuel = 0
    for crab in pos:
        n = abs(crab - place)
        fuel += n * (n + 1) // 2
    return fuel


def part1(inp):
    pos = [int(i) for i in inp[0].split(",")]
    cost = []
    for place in range(min(pos), max(pos) + 1):
        cost.append(calc_fuel_p1(pos, place))
    print(min(cost))


def part2(inp):
    pos = [int(i) for i in inp[0].split(",")]
    cost = []
    for place in range(min(pos), max(pos) + 1):
        cost.append(calc_fuel_p2(pos, place))
    print(min(cost))


part1(inp)
part2(inp)
