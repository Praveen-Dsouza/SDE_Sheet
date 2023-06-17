# O(n^2) time / O(1) space
def trap(height):
    if not height: return 0
    res, n = 0, len(height)
    
    for i in range(1, n - 1):
        # Find the maximum element on its left
        left = height[i]
        for j in range(i):
            left = max(left, height[j])

        # Find the maximum element on its right
        right = height[i]

        for j in range(i + 1, n):
            right = max(right, height[j])

        # Update the maximum water
        res += min(left, right) - height[i]

    return res         

# O(n) time / O(n) space
def trap(height):
    if not height: return 0
    water, n = 0, len(height)
    left, right = [0]*n, [0]*n

    # Fill left array
    left[0] = height[0]
    for i in range(1, n):
        left[i] = max(left[i-1], height[i])

    # Fill right array
    right[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], height[i])

    for i in range(n):
        water += min(left[i], right[i]) - height[i]

    return water

# O(n) time / O(1) space
def trap(height):
    if not height: return 0
    
    left, right = 0, len(height) - 1
    leftMax, rightMax = height[left], height[right]
    result = 0
    
    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, height[left])
            result += leftMax - height[left]
        else:
            right -= 1
            rightMax = max(rightMax, height[right])
            result += rightMax - height[right]
    return result