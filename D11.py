with open("input.txt") as f:
    inp = f.read().split("\n")


def part1(inp):
    arr = [[int(j) for j in i] for i in inp]
    m = len(arr)
    n = len(arr[0])

    def valid(i, j):
        return 0 <= i < m and 0 <= j < n

    def flash(i, j, flashed):
        flashed.add((i, j))
        to_flash = []
        for r in (i - 1, i, i + 1):
            for c in (j - 1, j, j + 1):
                if valid(r, c) and not (r == i and c == j) and (r, c) not in flashed:
                    arr[r][c] += 1
                    if arr[r][c] > 9:
                        flash(r, c, flashed=flashed)

        return flashed

    def step():
        flashed = set()
        for i in range(m):
            for j in range(n):
                arr[i][j] += 1

        for i in range(m):
            for j in range(n):
                if arr[i][j] > 9:
                    flashed = flash(i, j, flashed)
                    for x, y in flashed:
                        arr[x][y] = 0

        return len(flashed)

    flashes = 0
    for i in range(100):
        flashes += step()
    # print(*arr,sep="\n",end="\n\n")
    print(flashes)


def part2(inp):
    arr = [[int(j) for j in i] for i in inp]
    m = len(arr)
    n = len(arr[0])

    def valid(i, j):
        return 0 <= i < m and 0 <= j < n

    def flash(i, j, flashed):
        flashed.add((i, j))
        to_flash = []
        for r in (i - 1, i, i + 1):
            for c in (j - 1, j, j + 1):
                if valid(r, c) and not (r == i and c == j) and (r, c) not in flashed:
                    arr[r][c] += 1
                    if arr[r][c] > 9:
                        flash(r, c, flashed=flashed)

        return flashed

    def step():
        flashed = set()
        for i in range(m):
            for j in range(n):
                arr[i][j] += 1

        for i in range(m):
            for j in range(n):
                if arr[i][j] > 9:
                    flashed = flash(i, j, flashed)
                    for x, y in flashed:
                        arr[x][y] = 0

    i = 1
    while True:
        step()
        if all(all(i == 0 for i in j) for j in arr):
            break
        i += 1
    # print(*arr,sep="\n",end="\n\n")
    print(i)


part1(inp)
part2(inp)
