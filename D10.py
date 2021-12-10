with open("input.txt") as f:
    inp = f.read().split("\n")

import statistics


def part1(inp):
    hmap = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    openin = "{([<"
    closin = "})]>"
    for line in inp:
        stack = []
        for char in line:
            if char in openin:
                stack.append(char)
            else:
                if openin[closin.index(char)] == stack[-1]:
                    stack.pop(-1)
                else:
                    score += hmap[char]
                    break
    print(score)


def part2(inp):
    hmap = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    scores = []
    openin = "{([<"
    closin = "})]>"
    for line in inp:
        stack = []
        for char in line:
            if char in openin:
                stack.append(char)
            else:
                if openin[closin.index(char)] == stack[-1]:
                    stack.pop(-1)
                else:
                    break
        else:
            if stack:
                tmp = 0
                for val in stack[::-1]:
                    tmp = tmp * 5 + hmap[closin[openin.index(val)]]
                scores.append(tmp)
    print(statistics.median(scores))


part1(inp)
part2(inp)
