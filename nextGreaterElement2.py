# O(n^2) time / O(n) space
def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n

    for i in range(n):
        for j in range(i+1, 2 * n - 1):
            if nums[j % n] > nums[i]:
                res[i] = nums[j % n]
                break
    return res

# O(n) time / O(n) space (loop twice)
def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(2 * n - 1, -1, -1):
        while stack and nums[i % n] >= stack[-1]: # remove all small elements
            stack.pop()
        if i < n and stack: # top most large element in stack
            res[i] = stack[-1]
        stack.append(nums[i % n]) # append curr element
    return res

# Alternate Solution
def nextGreaterElements(nums):
    n = len(nums)
    stack = nums[::-1] # copy of array
    res = [-1] * n

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack: 
            res[i] = stack[-1]
        stack.append(nums[i])
    return res