# O(n) time / O(n) space
def isBalanced(self, root):
    if root is None: return 0
    lh = self.isBalanced(root.left) 
    rh = self.isBalanced(root.right)
    if lh == -1 or rh == -1 or abs(lh - rh) > 1: return -1
    return 1 + max(lh, rh)

# O(n^2) time / O(n) space
def isBalanced(self, root):
    if root is None: return True
    lh = self.height(root.left)
    rh = self.height(root.right)

    if abs(rh-lh) > 1: return False

    # Return Bool
    left = self.isBalanced(root.left)
    right = self.isBalanced(root.right)

    if not left or not right: return False

    return True

def height(self, root):
    if root is None: return 0
    return 1 + max(self.height(root.left), self.height(root.right))