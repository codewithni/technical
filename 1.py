rows = int(input("Enter number :- "))
for row in range(0, rows+1):
    num = 0
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=' ')
        else:
            print(2 * num + 1, end=' ')
            num += 1
    print("")
for row in range(rows,0,-1):
    num = 0
    for j in range(rows, 0, -1):
        if j < row:
            print(2 * num + 1, end=' ')
            num += 1
        else:
            print(" ", end=' ')
    print("")