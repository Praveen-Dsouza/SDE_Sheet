# O(n^2) time / O(n) space
def getPermutation(self, n, k):
    nums = [str(i) for i in range(1, n+1)]
    result = ''
    while(n):
        fact = self.factorial(n-1)
        idx = (k-1) // fact 
        result += str(nums[idx])
        nums.remove(nums[idx])
        n -= 1
        k %= fact
    return result

def factorial(self, n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact