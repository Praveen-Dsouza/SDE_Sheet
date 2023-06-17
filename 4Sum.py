 # O(n ^ 4) time / O(1) space
def fourSum(nums, target):
    result, n = set(), len(nums)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    currentSum = nums[i] + nums[j] + nums[k] + nums[l]
                    if currentSum == target:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
    return result

# O(n ^ 3) time / O(1) space
def fourSum(nums, target):
    result = set()
    n = len(nums)
    nums.sort()
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            while left < right:
                currentSum = nums[i] + nums[j] + nums[left] + nums[right]
                if currentSum == target:
                    result.add((nums[i], nums[j], nums[left], nums[right]))
                    # Jump duplicates
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif currentSum < target:
                    left += 1
                else :
                    right -= 1
    return result