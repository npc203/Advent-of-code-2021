with open("input.txt") as f:
    inp = f.read().split("\n")

from collections import Counter, defaultdict


def part1(inp):
    p = inp[0]
    rules = {}
    for i in inp[2:]:
        tmp = i.split(" -> ")
        rules[tmp[0]] = tmp[1]

    for _ in range(10):
        new_pol = ""
        for i in range(0, len(p) - 1):
            new_pol += p[i] + rules[p[i] + p[i + 1]]
        new_pol += p[-1]
        p = new_pol

    c = Counter(p)
    print(c[max(c, key=lambda x: c[x])] - c[min(c, key=lambda x: c[x])])


def part2(inp):
    p = inp[0]
    rules = {}
    for i in inp[2:]:
        tmp = i.split(" -> ")
        rules[tmp[0]] = tmp[1]

    pairs = defaultdict(int)
    for i in range(0, len(p) - 1):
        pairs[p[i] + p[i + 1]] += 1

    for _ in range(40):
        for key, val in pairs.copy().items():
            new_val = rules[key]
            pairs[key] -= val
            pairs[key[0] + new_val] += val
            pairs[new_val + key[1]] += val

    score = Counter(p[0])
    for k, v in pairs.items():
        score[k[1]] += v
    common = score.most_common()
    print(common[0][1] - common[-1][1])


part1(inp)
part2(inp)
