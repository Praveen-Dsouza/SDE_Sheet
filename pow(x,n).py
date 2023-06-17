# O(n) time / O(1) space
def myPow(x, n):
    res, nn = 1, n
    
    if nn < 0: 
        nn = -1 * nn
        
    for i in range(nn):
        res = res * x
        
    return 1 / res if n < 0 else res

# Language specific
# O(logn) time / O(1) space
def myPow(x, n):
    return x**n
    return pow(x, n)

# O(logn) time / O(1) space
def myPow(x, n):
    res, nn = 1, n
    
    if nn < 0: 
        nn = -1 * nn
        
    while nn > 0:
        # n positive
        if nn % 2 == 1:
            res = res * x
            nn -= 1
        else: # n negative
            x = x * x
            nn = nn / 2
    return 1 / res if n < 0 else res