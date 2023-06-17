# O(m * n) time / O(1) space
def searchMatrix(matrix, target):
    if not matrix or target is None: return False

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
    return False

# O(m + n) time / O(1) space
def searchMatrix(matrix, target):
    if not matrix or target is None: return False
    
    row, col = 0, len(matrix[0]) - 1 # first row, last col first row
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target: 
            return True
        elif matrix[row][col] < target: 
            row += 1
        elif matrix[row][col] > target: 
            col -= 1
    
    return False

 # O(logn) time / O(1) space
def searchMatrix(matrix, target):
    if not matrix or target is None: return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1 # start row, last col 
    
    while low <= high:
        mid = (low + high) // 2
        num = matrix[mid // cols][mid % cols]

        if num == target:
            return True
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False