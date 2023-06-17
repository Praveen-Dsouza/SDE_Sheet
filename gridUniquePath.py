from functools import cache

# O(2 ^ m + n) time / O(m + n) space
def uniquePaths(self, m, n, i = 0, j = 0):
    if i >= m or j >= n:      return 0
    if i == m-1 and j == n-1: return 1
    return self.uniquePaths(m, n, i + 1, j) + self.uniquePaths(m, n, i, j + 1)

# O(m * n) time / O(m * n) space
# Using Memoization:
def uniquePaths(self, m, n, i = 0, j = 0):
    @cache
    def dfs(i, j):
        if i >= m or j >= n:      return 0
        if i == m-1 and j == n-1: return 1
        return dfs(i+1, j) + dfs(i, j+1)
    return dfs(0, 0)

# Using Tabulation
def uniquePaths(self, m, n, i = 0, j = 0):
    dp = [[1] * n for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

# O(m * n) time / O(n) space
# We are only keeping two rows of length n giving space complexity of O(n)
def uniquePaths(self, m, n):
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]

# O(min(m, n)) time / O(1) space
def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(n):
            fact += fact * i
            i += 1
        return fact

def uniquePaths(m, n):
    return factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1)
