# O(n) time / O(n) space
def __init__(self):
    self.prev = None
    self.head = None
    
def flatten(self, root):
    if root is None: return
    self.flatten(root.left)
    if self.prev is None: 
        self.head = root
    else:
        root.left = self.prev
        self.prev.right = root
    self.prev = root
    self.flatten(root.right)
    
def bToDLL(self, root):
    self.flatten(root)
    return self.head