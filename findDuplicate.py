# brute force
# O(nlogn) time / O(1) space
def findDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

# better
def findDuplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        else:
            seen[num] = True

def findDuplicate(nums):
    slow = fast = 0

    # when fast and slow meet
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break
        
    # when pointer meet,place fast at start and inc both by one
    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow