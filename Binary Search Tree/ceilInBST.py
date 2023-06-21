# O(n) time / O(1) space
def findCeil(root, key):
    ceil = -1
    while root:
        if root.val == key:
            ceil = root.val
            return ceil
        
        if key > root.val:
            root = root.right
        else:
            ceil = root.val
            root = root.left
    return ceil