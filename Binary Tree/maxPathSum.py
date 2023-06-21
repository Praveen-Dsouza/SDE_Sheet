# O(n) time / O(n) space
def maxPathSum(self, root):
    maxi = [root.val]
    self.dfs(root, maxi)
    return maxi[0]

# return max path sum withot split
def dfs(self, root, maxi):
    if root is None: return 0

    leftMax = max(self.dfs(root.left, maxi), 0)
    rightMax = max(self.dfs(root.right, maxi), 0)

    # compute max path sum with split
    maxi[0]  = max(maxi[0], root.val + leftMax + rightMax)

    # return result without split
    return root.val + max(leftMax, rightMax)