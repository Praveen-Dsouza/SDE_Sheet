# Recursive Approach:
# O(n) time / O(n) auxillary space
def lowestCommonAncestor(self, root, p, q):
    if root is None: return None
    curr = root.val
    if curr > p.val and curr > q.val: 
        return self.lowestCommonAncestor(root.left, p, q)
    if curr < p.val and curr < q.val: 
        return self.lowestCommonAncestor(root.right, p, q)
    return root

# Iterative Approach:
# O(n) time / O(1) space
def lowestCommonAncestor(root, p, q):
    if root is None: return None
    while root:
        curr = root.val
        if curr > p.val and curr > q.val:
            root = root.left
        elif curr < p.val and curr < q.val:
            root = root.right
        else:
            return root