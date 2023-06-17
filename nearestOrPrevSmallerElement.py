# O(n^2) time / O(n) space
def prevSmaller(nums):
    n = len(nums)
    res = [-1] * n
    
    for i in range(n):
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i]:
                res[i] = nums[j]
                break
    return res
    
# O(n) time / O(n) space
def prevSmaller(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[i] <= stack[-1]: # remove all large elements
            stack.pop()
        if stack: # top most smallest element in stack
            res[i] = stack[-1]
        stack.append(nums[i]) # append curr element
    return res
