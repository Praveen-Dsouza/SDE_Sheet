# O(n) time / O(n) space
# Iterative Approach: 
def mirror(self,root):
    if not root: return root
    queue = [root]
    while queue:
        node = queue.pop(0)
        self.swapLeftAndRight(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root
    
# Recursive Approach: Level order
def mirror(self,root):
    if root is None: return None
    self.swapLeftAndRight(root)
    self.mirror(root.left)
    self.mirror(root.right)
    return root
    
def swapLeftAndRight(self, root):
    root.left, root.right = root.right, root.left