# O(n + m) time / O(n + m) auxillary space
def mergeTrees(self, root1, root2):
    if root1 is None and root2 is None: return None
    v1 = root1.val if root1 else 0
    v2 = root2.val if root2 else 0
    root = TreeNode(v1 + v2)

    root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    return root