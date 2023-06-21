# O(n^3) time / O(1) space
def shortest_distance(matrix):
    n = len(matrix) 
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 1e9
            if i == j: # diagonal /self
                matrix[i][j] = 0
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                
    # For negative cycle check
    for i in range(n):
        if matrix[i][j] < 0:
            return [-1]
            
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1e9:
                matrix[i][j] = -1