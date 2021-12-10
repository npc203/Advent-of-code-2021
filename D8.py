with open("input.txt") as f:
    inp = f.read().split("\n")


def part1(inp):
    data_raw = {1: 2, 4: 4, 7: 3, 8: 7}
    data = {j: i for i, j in data_raw.items()}

    count = 0
    for line in inp:
        op = line.split("|")[1]
        count += sum(1 for val in op.split() if data.get(n, 0))
    print(count)


def part2(inp):
    data_raw = {1: 2, 4: 4, 7: 3, 8: 7}
    data = {j: i for i, j in data_raw.items()}

    def code(value):
        phrases = [None] * 10

        for phrase in value.split():
            if k := data.get(len(phrase)):
                phrases[k] = phrase

        def get_match(inp, target):
            return sum(val in inp for val in phrases[target])

        # six seg: 0,6,9
        # five seg: 2,3,5

        for phrase in value.split():
            if get_match(phrase, 8) == 6:
                # find 9
                if get_match(phrase, 4) == 4:
                    res = 9
                # find 0
                elif get_match(phrase, 7) == 3:
                    res = 0
                # find 6
                else:
                    res = 6
                phrases[res] = phrase

            if get_match(phrase, 8) == 5:
                # find 2
                if get_match(phrase, 4) == 2:
                    res = 2
                # find 3
                elif get_match(phrase, 7) == 3:
                    res = 3
                else:
                    res = 5
                phrases[res] = phrase

        return phrases

    final_sum = 0
    for line in inp:
        op = line.split("|")
        pattern = ["".join(sorted(i)) for i in code(op[0])]
        decoded = ""
        for val in op[1].split():
            decoded += str(pattern.index("".join(sorted(val))))
        final_sum += int(decoded)
    print(final_sum)


# part1(inp)
part2(inp)
