# O(n^2) time / O(n) space
def buildTree(self, inorder, postorder):
    if not inorder or not postorder: return None
    root = TreeNode(postorder.pop())
    idx = inorder.index(root.val) # O(n), since we lineraly traverse inorder array
    root.right = self.buildTree(inorder[idx+1:], postorder) # creates subarray
    root.left = self.buildTree(inorder[:idx], postorder)
    return root

# O(n) time / O(n) space
def buildTree(self, inorder, postorder):
    return self.buildTreeHelper(inorder, postorder, 0, len(inorder)-1)

def buildTreeHelper(self, inorder, postorder, l, r):
    if l > r: return None
    inorderIdx = { v:i for i, v in enumerate(inorder) } # map to store index, value of inorder
    root = TreeNode(postorder.pop())
    idx = inorderIdx[root.val] # O(1)
    root.right = self.buildTreeHelper(inorder, postorder, idx+1, r)
    root.left = self.buildTreeHelper(inorder, postorder, l, idx-1)
    return root

# O(n) time / O(n) space
def buildTree(self, inorder, postorder):
    hm = {  v:i for i, v in enumerate(inorder) }
    return self.buildTreeHelper(0, len(inorder)-1, inorder, 0, len(postorder)-1, postorder, hm)

def buildTreeHelper(self, inst, ine, inorder, pst, pe, postorder, hm):
    if inst > ine or pst > pe: return None
    
    root = TreeNode(postorder[pe])
    
    inroot = hm[postorder[pe]]
    numsLeft = inroot - inst
    
    root.left = self.buildTreeHelper(inst, inroot-1, inorder, pst, pst + numsLeft - 1, postorder, hm)
    root.right = self.buildTreeHelper(inroot+1, ine, inorder, pst + numsLeft, pe-1, postorder, hm)
    
    return root