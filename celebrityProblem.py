 # O(n^2) time / O(n) space
def celebrity(M, n):
    celb_in = [0] * n
    celb_out = [0] * n
    
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1: # i (celb) know j
                celb_in[j] += 1
                celb_out[i] += 1
    
    # celebrity check 
    # i is known to everyone(in[i] == n-1) but 
    # i does not know anyone (out[i] == 0)
    for i in range(n):
        if celb_in[i] == n-1 and celb_out[i] == 0:
            return i
    return -1

# O(n) time / O(1) space
def celebrity(M, n):
    c = 0
    for i in range(1, n):
        if M[c][i] == 1:
            c = i
        
    for i in range(n):
        if i != c and (M[c][i] == 1 or M[i][c] == 0):
            return -1
    return c