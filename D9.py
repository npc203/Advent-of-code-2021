with open("input.txt") as f:
    inp = f.read().split("\n")

from math import prod


def part1(inp):
    arr = []
    for line in inp:
        arr.append([int(val) for val in line])

    m = len(arr)
    n = len(arr[0])
    lowest = []

    def valid(i, j):
        return 0 <= i < m and 0 <= j < n

    for i in range(m):
        for j in range(n):
            for check in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if valid(*check):
                    if arr[i][j] >= arr[check[0]][check[1]]:
                        break
            else:
                lowest.append(arr[i][j] + 1)
    print(sum(lowest))


def part2(inp):
    arr = []
    for line in inp:
        arr.append([int(val) for val in line])

    m = len(arr)
    n = len(arr[0])
    basins = []

    def valid(i, j):
        return 0 <= i < m and 0 <= j < n

    for i in range(m):
        for j in range(n):
            for check in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if valid(*check):
                    if arr[i][j] >= arr[check[0]][check[1]]:
                        break
            else:
                # basin finding thing
                def near(i, j):
                    return set(
                        (row, col)
                        for row, col in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
                        if valid(row, col)
                    )

                # moving spinny boi
                def bfs(x, y, visited):
                    visited.add((x, y))
                    near_coords = near(x, y) - visited
                    for i, j in near_coords:
                        if not (arr[i][j] in visited or arr[i][j] == 9):
                            visited.union(bfs(i, j, visited))
                    return visited

                basins.append(len(bfs(i, j, set())))

    max_3 = []
    for _ in range(3):
        m = max(basins)
        max_3.append(m)
        basins.remove(m)

    print(prod(max_3))


part1(inp)
part2(inp)
