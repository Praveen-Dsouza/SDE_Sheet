# O(n) time / O(n) auxillary space
def bstFromPreorder(self, preorder):
    self.i = 0
    return self.build(preorder, self.i, float('inf'))

def build(self, preorder, i, bound):
    if self.i == len(preorder) or preorder[i] > bound: return None
    root = TreeNode(preorder[self.i])
    self.i+=1
    root.left = self.build(preorder, self.i, root.val)
    root.right = self.build(preorder, self.i, bound)
    return root