# O(n) time / O(n) space
# Return tree node
def sortedArrayToBST(self, nums):
    return self.sortedArrayToBSTHelper(0, len(nums) - 1, nums)
    
def sortedArrayToBSTHelper(self, left, right, nums):
        if left > right: return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTHelper(left, mid-1, nums)
        root.right = self.sortedArrayToBSTHelper(mid+1, right, nums)
        return root

# Return array of node val
def sortedArrayToBST(self, nums):
    res = []
    self.sortedArrayToBSTHelper(res, 0, len(nums)-1, nums)
    return res
    
def sortedArrayToBSTHelper(self, res, left, right, nums):
        if left > right: return None
        mid = (left + right) // 2
        res.append(nums[mid])
        self.sortedArrayToBSTHelper(res, left, mid - 1, nums)
        self.sortedArrayToBSTHelper(res, mid + 1, right, nums)