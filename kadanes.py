# Brute Force:
# O(n^2) time / O(1) space
def maxSubArray(nums):
    maxSum, currSum = float('-inf'), 0
    for i in range(len(nums)):
        currSum += nums[i]
        for j in range(i + 1, len(nums)):
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
    return maxSum

# O(n) time / O(1) space
def maxSubArray(nums):
    maxSum = float('-inf')
    currentSum = 0
    for i in range(len(nums)):
        currentSum += nums[i]
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum