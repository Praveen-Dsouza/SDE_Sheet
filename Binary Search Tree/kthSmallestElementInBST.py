#  O(n) time / O(1) space
def __init__(self):
    self.counter = 0
    
def KthSmallest(self, root, k): 
    return self.KthSmallestUtil(root, k)
    
def KthSmallestUtil(self, root, k):
    if root is None: return -1
    left = self.KthSmallestUtil(root.left, k)
    if left is not -1: return left
    self.counter += 1
    if self.counter == k: return root.data
    return self.KthSmallestUtil(root.right, k)