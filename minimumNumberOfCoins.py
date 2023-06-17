# O(n) time / O(1) space
def minPartition(N):
    if N == 0: return 0
    coins = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    res = []
    
    for coin in coins:
        while coin <= N:
            N -= coin
            res.append(coin)
    return res