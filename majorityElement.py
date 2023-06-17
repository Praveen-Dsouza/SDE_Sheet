# O(n^2) time / O(1) space
def majorityElement(nums):
    maxCount, count, index = 0, 0, -1
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        
        if count > maxCount:
            maxCount = count
            index = i
            
    return nums[index] if maxCount > len(nums) // 2 else -1

#  if there exists a majority element
# O(nlogn) time / O(1) space
def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]

# O(n) time / O(n) space
def majorityElement(nums):
    freq = {}

    for i in nums:
        freq[i] = 1 + freq.get(i, 0)
        if freq[i] > len(nums) // 2:
            return i

    return -1

# O(n) time / O(1) space
def majorityElement(nums):
    candidate = count = 0
    
    for num in nums:
        if num == candidate:
            count += 1
        elif count == 0:
            candidate = num
        else:
            count -= 1
            
    return candidate