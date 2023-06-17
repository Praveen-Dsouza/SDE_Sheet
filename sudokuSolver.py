# O(9^(n^2)) time / O(1) space
def solveSudoku(self, board):
    rows, cols = len(board), len(board[0])

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == ".":
                # check whether we can place num from 1-9 in row
                for num in range(1, 10):
                    num = str(num)
                    if self.isValid(board, row, col, num): # check valid num position
                        board[row][col] = num
                        # recursive call for the valid num position
                        if self.solveSudoku(board) == True: 
                            return True
                        else: 
                            board[row][col] = "."
                return False
    return True

def isValid(self, board, row, col, num):
    for i in range(9):
        if board[i][col] == num: # check col of matrix
            return False
        if board[row][i] == num: # check row of matrix
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num: # check submatrix
            return False
    return True