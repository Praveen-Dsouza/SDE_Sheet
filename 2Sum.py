# O(n ^ 2) time / O(1) space
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j] # [nums[i], nums[j]]
    return []

# O(nlogn) time / O(1) space
def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    
    while l < r:
        currentSum = nums[l] + nums[r]
        if currentSum == target:
            return [nums[l], nums[r]]
        elif currentSum < target:
            l += 1
        else:
            r -= 1
    
    return []

# O(n) time / O(n) space
def twoSum(nums, target):
    seen = {}
    for idx, num in enumerate(nums):
        pm = target - num
        if pm in seen:
            return [seen[pm], idx]
        else:
            seen[num] = idx
    return []