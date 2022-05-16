class NQueens_Backtrack:
    def __init__(self, n) -> None:
        self.n = n
        self.matrix = [["-"]*n for _ in range(n)]
        self.count = 0
        # self.solutions = []

    def printSolution(self):
        for row in range(self.n):
            print(*self.matrix[row])

    def isSafe(self, row, col):
        #Check the column
        for r in range(self.n):
            if self.matrix[r][col] == "Q":
                return False
        
        #Check top left direction diagonally
        i,j = row,col
        while i >= 0 and j >= 0:
            if self.matrix[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        
        #Check top right direction diagonally
        i,j = row,col
        while i >= 0 and j < self.n:
            if self.matrix[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True
    
    def nQueens(self,row):
        if row == self.n:
            self.count += 1
            print()
            self.printSolution()
            print()
            return
        for i in range(self.n):
            if self.isSafe(row,i) == True:
                self.matrix[row][i] = 'Q'
                self.nQueens(row+1)
                self.matrix[row][i] = "-"


class NQueens_Branch_Bound:
    def __init__(self,n) -> None:
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.slashCode = [[0 for i in range(n)] for j in range(n)]
        self.backslashCode = [[0 for i in range(n)] for j in range(n)]
        self.rowLookUp = [False] * n
        x = 2 * n - 1
        self.slashCodeLookup = [False] * x
        self.backslashCodeLookup = [False] * x
    def printBoard(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    print("Q",end=" ")
                else:
                    print("-",end=" ")
            print()
    def isSafe(self,row,col):
        if self.slashCodeLookup[self.slashCode[row][col]] or self.backslashCodeLookup[self.backslashCode[row][col]] or self.rowLookUp[row]:
            return False
        return True
    
    def recursive(self,col):
        if col >= self.n:
            return True
        for i in range(self.n):
            if self.isSafe(i,col):
                self.board[i][col] = 1
                self.rowLookUp[i] = True
                self.slashCodeLookup[self.slashCode[i][col]] = True
                self.backslashCodeLookup[self.backslashCode[i][col]] = True
                if self.recursive(col+1):
                    return True
                self.board[i][col] = 0
                self.rowLookUp[i] = False
                self.slashCodeLookup[self.slashCode[i][col]] = False
                self.backslashCodeLookup[self.backslashCode[i][col]] = False
        return False
    
    def solve(self):
        for i in range(self.n):
            for j in range(self.n):
                self.slashCode[i][j] = i + j
                self.backslashCode[i][j] = i - j + self.n - 1
        if self.recursive(0) == False:
            return False
        self.printBoard()
        return True
    
while True:
    print(
        "Select Choice\n",
        "1>Backtracking\n",
        "2>Branch and Bound\n",
        "3>Exit"
    )
    choice = int(input("Enter choice:"))
    if choice == 1:
        n = int(input("Enter number of queens:"))
        solver = NQueens_Backtrack(n)
        solver.nQueens(0)
        print(f"Number of solutions: {solver.count}")
    elif choice == 2:
        n = int(input("Enter number of queens:"))
        solver = NQueens_Branch_Bound(n)
        solver.solve()
    else:
        break