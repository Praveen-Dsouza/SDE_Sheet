# Recursive Approach:
# O(n) time / O(n) space
def __init__(self):
    self.prev = None
def flatten(self, root):
    if root is None: return
    self.flatten(root.right)
    self.flatten(root.left)
    root.right = self.prev
    root.left = None
    self.prev = root

# Iterative Approach:
# O(n) time / O(n) space
def flatten(root):
    if root is None: return
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        if stack:
            curr.right = stack[-1]
        curr.left = None    
    
# O(n) time / O(1) space
def flatten(root):
    curr = root
    while curr:
        if curr.left:
            prev = curr.left
            while prev.right:
                prev = prev.right
            prev.right = curr.right
            curr.right = curr.left
            curr.left = None
        curr = curr.right