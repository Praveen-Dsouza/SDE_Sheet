 # O(n) time / O(1) space
def findMaxConsecutiveOnes(nums):
    maxOnes = count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        maxOnes = max(maxOnes, count)    
    return maxOnes