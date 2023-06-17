# O(n! * n) time / O(n) space
def solveNQueens(self, n):
    res = []
    board = [["." for c in range(n)] for r in range(n)]
    leftRow = [0 for i in range(n)]
    upperDiag = [0 for i in range(2*n - 1)]
    lowerDiag = [0 for i in range(2*n - 1)]
    self.solve(0, board, res, leftRow, upperDiag, lowerDiag, n)
    return res

def solve(self, col, board, res, leftRow, upperDiag, lowerDiag, n):
    if col == n:
        # becasue res has to be in string rather then a cell
        res.append([''.join(i) for i in board]) 
        return

    for row in range(n): # iterating through all the columns of  passed row
        if leftRow[row] == 0 and lowerDiag[row+col] == 0 and upperDiag[n-1 + col - row] == 0:
            board[row][col] = "Q"
            leftRow[row] = 1
            lowerDiag[row+col] = 1
            upperDiag[n-1 + col - row] = 1
            self.solve(col+1, board, res, leftRow, upperDiag, lowerDiag, n)
            board[row][col] = "."
            leftRow[row] = 0
            lowerDiag[row+col] = 0
            upperDiag[n-1 + col - row] = 0

# O(n! * n) time / O(n^2) space
def isSafe(self, row, col, board, n):
    dupRow, dupCol = row, col

    # check upper diagonal
    while row >= 0 and col >= 0:
        if board[row][col] == "Q": return False
        row -= 1
        col -= 1

    # check left 
    row, col = dupRow, dupCol
    while col >= 0:
        if board[row][col] == "Q": return False
        col -= 1

    # check lower diagonal
    row, col = dupRow, dupCol
    while row < n and col >= 0:
        if board[row][col] == "Q": return False
        row += 1
        col -= 1

    return True

def solve(self, col, board, res, n):
    if col == n:
        # becasue res has to be in string rather then a cell
        res.append([''.join(i) for i in board]) 
        return
    for row in range(n): # iterating through all the columns of  passed row
        if self.isSafe(row, col, board, n):
            board[row][col] = "Q"
            self.solve(col+1, board, res, n) # start next col from 0th row
            board[row][col] = "." # backtracking

def solveNQueens(self, n):
    res = []
    board = [["." for c in range(n)] for r in range(n)]
    self.solve(0, board, res, n)
    return res

