# O(n) time / O(1) space
def searchBST(root, val):
    if root is None or val is None: return None
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root