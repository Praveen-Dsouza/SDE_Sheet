# O(n) time / O(n) recursion stack space
# Using Preorder Traversal
def getPath(self, root, res, targetNode):
    if root is None: return False
    res.append(root.val)

    if root.val == targetNode:
        return True
        
    if self.getPath(root.left, res, targetNode) or self.getPath(root.right, res, targetNode):
        return True
    
    res.pop()
    return False
    
def solve(self, A, B):
    res = []
    if A is None: return res
    self.getPath(A, res, B)
    return res