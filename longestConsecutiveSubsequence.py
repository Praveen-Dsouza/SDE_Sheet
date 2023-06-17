# O(nlogn) time / O(1) space
def longestConsecutive(nums):
    if len(nums) == 0: return 0
    
    nums.sort()
    count = maxCount = 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 1:
            count += 1
            maxCount = max(maxCount, count)
        elif nums[i] == nums[i - 1]: continue
        else: count = 1
    return maxCount

# Using hashmap
def longestConsecutive(nums):
    freq = {}
    if len(nums) <= 0: return 0

    for num in nums: freq[num] = 1
    
    for num in nums:
        if num - 1 in freq:
            freq[num] = 0
        
    maxCount = 1
    for num in nums:
        if freq[num] == 1:
            count = 1
            while(num + count in nums):
                count += 1
            maxCount = max(maxCount, count)
    return maxCount
    
# Using hashset
def longestConsecutive(nums):
    freq, maxCount = set(nums), 0
    for num in freq:
        if num - 1 in freq: continue
        currLen = 1
        while num + currLen in freq: 
            currLen += 1
        maxCount = max(maxCount, currLen)
    return maxCount