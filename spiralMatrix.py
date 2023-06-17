# O(m * n) time / O(1) space
def spiralOrder(matrix):
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []
    
    while left < right and top < bottom:
        # get every i in top row ->
        for i in range(left, right): 
            res.append(matrix[top][i])
        top += 1
        
        # get every i from right col |
        for i in range(top, bottom):
            res.append(matrix[i][right - 1]) # since right out of bound
        right -= 1
        
        if not (left < right and top < bottom):
            break
        
        # get every i from bottom row _
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i]) # since bottom out of bound
        bottom -= 1
        
        # get every i from left <-
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
        
    return res