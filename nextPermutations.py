def nextPermutation(nums):
    # Step 1: Find first non-increasing digit from right, say at i-1 index
    # Step 2: Find first non-decreasing digit from i-1 then swap i-1 and digit index (say j)
    # Step 3: Reverse the digits from index i
    
    i = j = len(nums) - 1
    
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1
        
    if i > 0:
        while nums[j] <= nums[i - 1]:
            j -= 1
        
        # swap
        nums[j], nums[i - 1] = nums[i - 1], nums[j]
        
    #reverse    
    nums[i:] = nums[i:][::-1]
    return nums