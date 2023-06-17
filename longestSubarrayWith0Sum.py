# O(n ^ 2) time / O(1) space
def maxLen(arr):
    maxLen = 0
    for i in range(len(arr)):
        currentSum = 0
        for j in range(i, len(arr)):
            currentSum += arr[j]
            
            if currentSum == 0:
                maxLen = max(maxLen, j - i + 1)
    return maxLen

# O(n) time / O(n) space
def maxLen(arr):
    summation = {}
    subarraySum = currentSum = 0
    for i in range(len(arr)):
        currentSum += arr[i]
        if currentSum == 0:
            subarraySum = i + 1
        else:
            if currentSum in summation:
                subarraySum = max(subarraySum, i - summation[currentSum])
            else:
                summation[currentSum] = i
    return subarraySum