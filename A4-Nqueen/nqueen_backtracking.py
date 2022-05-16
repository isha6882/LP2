def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print("\n")


def isSafe(board, row, col):
    for i in range(N):
        if board[row][i] == 1:
            return False
        if board[i][col] == 1:
            return False
    # Check top right direction diagonally
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # Check top left direction diagonally
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    return True


def solveNQUtil(board, row):
    if row == N:
        global sol
        printSolution(board)
        sol += 1
        return
    for i in range(N):
        if isSafe(board, row, i):
            board[row][i] = 1
            solveNQUtil(board, row + 1)
            board[row][i] = 0
    return


sol = 0
N = int(input("Enter N: "))
board = [[0 for col in range(N)] for row in range(N)]
solveNQUtil(board, 0)
print("Number of solutions : ", sol)
