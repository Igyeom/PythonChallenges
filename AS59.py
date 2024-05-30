l = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

for turn in range(9):
    print("\033c", end="\033[A")
    if turn % 2 == 0:
        symbol = "X"
    else:
        symbol = "O"
    print(symbol + "'s turn")
    for i in l:
        for j in i:
            if j == -1:
                print("_",end="")
                continue
            if j == 0:
                print("X",end="")
                continue
            if j == 1:
                print("O",end="")
                continue
        print()
    c, r = map(int, input("Which space? (e.g. '2 2' for middle, '1 3' for bottom-left): ").split())
    l[r-1][c-1] = turn
