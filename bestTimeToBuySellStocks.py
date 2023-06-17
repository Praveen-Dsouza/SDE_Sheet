# Brute Force:
# O(n^2) time / O(1) space
def maxProfit(prices):
    maxProfit = float('-inf')
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[i]:
                maxProfit = max(maxProfit, prices[j] - prices[i])
    return maxProfit

# Optimal:
# O(n) time / O(1) space
def maxProfit(prices):
    maxProfit = 0
    minProfit = float('inf')
    for i in range(len(prices)):
        minProfit = min(minProfit, prices[i])
        maxProfit = max(maxProfit, prices[i] - minProfit)
    return maxProfit