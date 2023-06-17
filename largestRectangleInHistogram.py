# O(n) time / O(n) space
def largestRectangleArea(heights):
    heights.append(0)
    maxArea, stack, n = 0, [], len(heights)

    for i in range(n):
        while stack and (i == n-1 or heights[stack[-1]] >= heights[i]):
            height = heights[stack[-1]]
            stack.pop()
            if not stack: width = i
            else: width = i - stack[-1] - 1
            maxArea = max(maxArea, width * height)
        stack.append(i)
    
    return maxArea

# O(4n) time / O(3n) space
def largestRectangleArea(heights):
    n = len(heights)
    stack, leftSmall, rightSmall = [], [-1]*n, [-1]*n
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if not stack: leftSmall[i] = 0
        else: leftSmall[i] = stack[-1] + 1
        stack.append(i)

    # clear the stack to be reused
    while stack: stack.pop()

    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if not stack: rightSmall[i] = n - 1
        else: rightSmall[i] = stack[-1] - 1
        stack.append(i)

    maxArea = 0
    for i in range(n):
        maxArea = max(maxArea, heights[i] * (rightSmall[i] - leftSmall[i] + 1))
    
    return maxArea