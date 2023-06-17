# brute Force:
# O(m * n) time / O(m * n) space
def rotate(matrix):
    rows, cols = len(matrix), len(matrix[0])
    copy = [[0 for j in range(cols)] for i in range(rows)]

    # row of org mat to col of copy mat
    for i in range(rows):
        for j in range(cols):
            matrix[i][j], copy[j][rows -1 -i] = copy[j][rows -1 -i], matrix[i][j]
        
    # copy values to matrix
    for i in range(rows):
        for j in range(cols):
            matrix[i][j], copy[i][j] = copy[i][j], matrix[i][j]

# Optimal
# O(m * n) time / O(1) space
def rotate(matrix):
    rows = len(matrix)
    # transpose
    for i in range(rows):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # reverse every rows
    for i in range(rows):
        matrix[i] = matrix[i][::-1]