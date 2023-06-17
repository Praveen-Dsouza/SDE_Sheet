def repeatedStringMatch(a, b):
    n = ceil(len(b) / len(a)) # 8/4 = 2
    if b in a*n: # 8 in abcd * 2 = abcdabcd
        return n # 2
    elif b in a*(n+1): # 8 in abcd * (2 + 1) = abcd * 3 = abcdabcdabcd
        return n+1 # 3
    return -1