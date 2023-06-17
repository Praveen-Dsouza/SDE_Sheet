# O(n ^ 3) time / O(n) space
def threeSum(nums):
    triplets = set() # use set to append unique pairs
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                currentSum = nums[i] + nums[j] + nums[k]
                if currentSum == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
    return triplets

# O(n ^ 2) time / O(n) space
def threeSum(nums):
    nums.sort()
    triplets = set()
    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) -1 
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if currentSum == 0:
                triplets.add((nums[i], nums[left], nums[right]))
                # Jump duplicates
                while left < right and nums[left] == nums[left + 1]: left += 1
                while left < right and nums[right] == nums[right - 1]: right -= 1
                left += 1
                right -= 1
            elif currentSum < 0:
                left += 1
            elif currentSum > 0:
                right -= 1
    return triplets