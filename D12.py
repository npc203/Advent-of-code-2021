with open("input.txt") as f:
    inp = f.read().split("\n")

from collections import defaultdict


def part1(inp):
    paths = defaultdict(list)
    pairs = []
    for line in inp:
        pair = line.split("-")
        pairs.append(pair)

    V = list(set(j for i in pairs for j in i))

    for key in V:
        for val in pairs:
            if key in val:

                paths[key].append(val[not val.index(key)])

    global cnt
    cnt = 0

    def dfs(s, e, path, visited):
        global cnt

        visited[V.index(s)] += 1
        path.append(s)
        if s == e:
            cnt += 1
        else:
            for edge in paths[s]:
                if visited[V.index(edge)] == 0 or edge.isupper():
                    dfs(edge, e, path, visited)

        path.pop()
        visited[V.index(s)] = False

    visited = [0] * len(V)
    dfs("start", "end", [], visited)
    print(cnt)


# INCOMPLETE PART2
def part2(inp):
    paths = defaultdict(list)
    pairs = []
    for line in inp:
        pair = line.split("-")
        pairs.append(pair)

    V = list(set(j for i in pairs for j in i))

    for key in V:
        for val in pairs:
            if key in val:

                paths[key].append(val[not val.index(key)])

    cnt = 0
    stack = []
    path = []
    visited = [0] * len(V)

    while stack:
        visited[V.index(s)] += 1
        path.append(s)
        if s == e:
            # print(*path,sep=",")
            cnt += 1
        else:
            for edge in paths[s]:
                if visited[V.index(edge)] == 0 or edge.isupper():
                    dfs(edge, e, path, visited)
                elif edge != "start":
                    if not any(i >= 2 for i in visited):
                        dfs(edge, e, path, visited)

        path.pop()
        visited[V.index(s)] = False

    dfs("start", "end", [], visited)
    print(cnt)


part1(inp)
part2(inp)
