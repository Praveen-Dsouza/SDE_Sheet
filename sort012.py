def sortColors(nums):
    l, m, r = 0, 0, len(nums) - 1
    while m <= r:
        if nums[m] == 0:
            nums[m], nums[l] = nums[l], nums[m]
            l += 1
            m += 1
        elif nums[m] == 2:
            nums[m], nums[r] = nums[r], nums[m]
            r -= 1
        else:
            m += 1 
        