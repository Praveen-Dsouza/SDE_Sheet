# O(n) time / O(n) space
def __init__(self):
    self.diameter = 0

def height(self, root):
    if root is None: return 0

    lh = self.height(root.left)
    rh = self.height(root.right)
    self.diameter = max(self.diameter, lh+rh)
    return 1 + max(lh, rh)

def diameterOfBinaryTree(self, root):
    self.height(root)
    return self.diameter

# O(n^2) time / O(n) space
def diameterOfBinaryTree(self, root):
    if root is None: return 0
    dl = self.diameterOfBinaryTree(root.left)
    dr = self.diameterOfBinaryTree(root.right)
    curr = self.height(root.left) + self.height(root.right)
    return max(curr, max(dl, dr))

def height(self, root):
    if root is None: return 0
    return 1 + max(self.height(root.left), self.height(root.right))