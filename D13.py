with open("input.txt") as f:
    inp = f.read().split("\n")


def debug(dots):
    x = max(dots, key=lambda i: i[0])[0] + 1
    y = max(dots, key=lambda i: i[1])[1] + 1

    arr = [["." for i in range(y)] for j in range(x)]
    for i, j in dots:
        arr[i][j] = "#"
    print(*("".join(i) for i in arr), sep="\n")
    print("-" * 25)


def part1(inp):
    dots = set()
    cmds = []

    for line in inp:
        if line.startswith("fold"):
            tmp = line.split()[-1]
            cmds.append(tmp.split("="))
        else:
            try:
                dots.add(tuple(int(i) for i in line.split(","))[::-1])
            except:  # jobless "\n" ruining my day smh
                pass

    i = cmds[0]
    axis = i[0] == "x"
    l = int(i[1])
    for d in dots.copy():
        if d[axis] >= l:
            if d[axis] > l:
                if not axis:  # x-axis flip
                    dots.add((2 * l - d[0], d[1]))
                else:  # y-axis flip
                    dots.add((d[0], 2 * l - d[1]))
            dots.remove(d)

    print(len(dots))


def part2(inp):
    dots = set()
    cmds = []

    for line in inp:
        if line.startswith("fold"):
            tmp = line.split()[-1]
            cmds.append(tmp.split("="))
        else:
            try:
                dots.add(tuple(int(i) for i in line.split(","))[::-1])
            except:
                pass

    for i in cmds:
        axis = i[0] == "x"
        l = int(i[1])
        for d in dots.copy():
            if d[axis] >= l:
                if d[axis] > l:
                    if not axis:  # x-axis flip
                        dots.add((2 * l - d[0], d[1]))
                    else:  # y-axis flip
                        dots.add((d[0], 2 * l - d[1]))
                dots.remove(d)

    debug(dots)


def part2_fun(inp):
    dots = set()
    cmds = []

    for line in inp:
        if line.startswith("fold"):
            tmp = line.split()[-1]
            cmds.append(tmp.split("="))
        else:
            try:
                dots.add(tuple(int(i) for i in line.split(","))[::-1])
            except:
                pass

    for i in cmds:
        axis = i[0] == "x"
        l = int(i[1])
        for d in dots.copy():
            if d[axis] >= l:
                if d[axis] > l:
                    if not axis:  # x-axis flip
                        dots.add((2 * l - d[0], d[1]))
                    else:  # y-axis flip
                        dots.add((d[0], 2 * l - d[1]))
                dots.remove(d)

    # Fun stuff to draw
    x = max(dots, key=lambda i: i[0])[0] + 1
    y = max(dots, key=lambda i: i[1])[1] + 1

    from PIL import Image, ImageDraw
    import pytesseract

    image = Image.new("RGB", (4 * y + 10, 4 * x + 10))
    img1 = ImageDraw.Draw(image)
    for i, j in dots:
        # image.putpixel((j*4+10,i*4+10),(255,255,255))
        r, c = 4 * j, 4 * i
        img1.rectangle(((r - 2 + 6, c - 2 + 6), (r + 2 + 6, c + 2 + 6)), fill="white")
    print(pytesseract.image_to_string(image))
    image.show()


part1(inp)
part2(inp)
