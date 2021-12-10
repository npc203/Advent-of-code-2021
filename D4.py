with open("input.txt") as f:
    inp = f.read().split("\n")


def check_winner(board):
    for i in range(5):
        if all(board[i * 5 + j] == -1 for j in range(5)):
            return True
        if all(board[j * 5 + i] == -1 for j in range(5)):
            return True
    return False


def sum_board(board):
    return sum(i for i in board if i != -1)


def part1(inp):
    move = inp[0].split(",")
    boards = []
    i = 2

    while i < len(inp):
        tmp = []
        for x in range(5):
            for value in inp[i + x].split():
                tmp.append(int(value))
        boards.append(tmp)
        i += 6

    for val in move:
        val = int(val)
        for ind, board in enumerate(boards):
            try:
                x = board.index(val)
                board[x] = -1
            except ValueError:
                continue

            if check_winner(board):
                print(val * sum_board(board))
                return


def part2(inp):
    move = inp[0].split(",")
    boards = []
    i = 2

    while i < len(inp):
        tmp = []
        for x in range(5):
            for value in inp[i + x].split():
                tmp.append(int(value))
        boards.append(tmp)
        i += 6

    a = [0 for i in range(len(boards))]
    for val in move:
        val = int(val)
        for ind, board in enumerate(boards):
            try:
                x = board.index(val)
                board[x] = -1
            except ValueError:
                continue

            if check_winner(board):
                a[ind] = 1
                if all(a):
                    print(val * sum_board(board))
                    return


part1(inp)
part2(inp)
