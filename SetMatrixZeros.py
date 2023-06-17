# O(mn) time / O(1) space
def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rowZero = False # first row is not zero
    
    # determine which rows/cols needs to be zero
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0 # set first row in that col to zero
                
                if r > 0:
                    matrix[r][0] = 0 # set first col in that row to zero
                else:
                    rowZero = True
    
    # convert the row/col zero
    for r in range(1, rows):
        for c in range(1, cols):
            # if curr row or col is zero set curr pos to zero
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    
    # we are not gonna zero out the first row, col
    if matrix[0][0] == 0:
        # zero out the first col of matrix
        for r in range(rows):
            matrix[r][0] = 0
        
    # if rowZero is True, we need to zero out first row
    if rowZero:
        for c in range(cols):
            matrix[0][c] = 0

        