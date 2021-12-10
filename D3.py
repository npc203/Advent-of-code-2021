with open("input.txt") as f:
    inp = f.read().split("\n")

from collections import Counter


def part1():
    gamma = ""
    epsilon = ""
    for i in range(len(inp[0])):
        a = Counter("".join(v[i] for v in inp))
        gamma += str(int(a["0"] < a["1"]))
        epsilon += str(int(a["0"] > a["1"]))
    print(int(gamma, 2) * int(epsilon, 2))


def part2():
    def solve(most):
        val = ""
        tmp = inp.copy()
        for col_ind in range(len(inp[0])):
            col_array = "".join(v[col_ind] for v in tmp)
            count = Counter(col_array)

            if count["0"] == count["1"]:
                num = str(int(most))
            else:
                num = str(int(count["0"] > count["1"]) ^ most)
            val += num

            new_tmp = []
            for ind, val in enumerate(col_array):
                if val == num:
                    new_tmp.append(tmp[ind])
            tmp = new_tmp

            if len(tmp) == 1:
                val = tmp[0]
                break
        return val

    o2 = solve(most=True)
    co2 = solve(most=False)
    print(int(o2, 2) * int(co2, 2))


part1()
part2()
