# O(n*k) time / O(n) space
def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        currMax = float('-inf')
        for j in range(i, i + k):
            currMax = max(nums[j], currMax)
        res.append(currMax)
    
    return res

# O(n) time / O(k) space
import collections
def maxSlidingWindow(nums, k):
    queue = collections.deque()
    res = []
    left, right = 0, 0
    
    while right < len(nums):
        # we need to eliminate smallest value in queue
        # need to compare top val of queue with the current val
        # if smaller value exits in queue pop the value from queue
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        queue.append(right)
        
        # left Idx > leftmost val in queue remove left val from queue(window)
        if left > queue[0]:
            queue.popleft()
        
        # check if our window is atleast size k 
        # append maximum value to res arr
        # left will increament once our window is size k
        if right + 1 >= k:
            res.append(nums[queue[0]])
            left += 1
        right += 1
        
    return res