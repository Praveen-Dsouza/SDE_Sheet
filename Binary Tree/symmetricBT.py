# O(n) time / O(n) space
def isSymmetric(self, root):
        return root is None or self.isSymmetricHelper(root.left, root.right)
    
def isSymmetricHelper(self, left, right):
    if left is None or right is None:
        return left == right
    
    if left.val != right.val: return False
    
    return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)