# O(n) time / O(1) space
def __init__(self):
    self.counter = 0
    
def kthLargestUtil(self, root, k):
    if root is None: return -1
    right = self.kthLargestUtil(root.right, k)
    if right != -1: return right
    self.counter += 1
    if self.counter == k:
        return root.data
    return self.kthLargestUtil(root.left, k)

def kthLargest(self,root, k):
    return self.kthLargestUtil(root, k)