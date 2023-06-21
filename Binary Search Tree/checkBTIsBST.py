# O(n) time / O(n) space
def helper(self, root, minValue = float('-inf'), maxValue = float('inf')):
    if root is None: return True
    val = root.val
    if val <= minValue or val >= maxValue: return False
    if not self.helper(root.left, minValue, val): return False
    if not self.helper(root.right, val, maxValue): return False
    return True

def isValidBST(self, root):
    return self.helper(root)