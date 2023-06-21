# O(2n) time / O(2n) space
def lca(self, root, p, q):
    path1, path2 = [], []

    if not self.getPath(root, path1, p) or not self.getPath(root, path2, q):
        return False

    # Compare the paths to get the first different value
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

def getPath(self, root, path, x):
    if root is None: return False

    path.append(root)

    if root.data == x: return True

    if (root.left and self.getPath(root.left, path, x)) or (root.right and self.getPath(root.right, path, x)):
        return True

    path.pop()
    return False

# O(n) time / O(n) auxillary space
def lowestCommonAncestor(self, root, p, q):
    if root is None or root == p or root == q:
        return root
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    
    if left is None:
        return right
    elif right is None:
        return left
    else: # both left and right is not null, we found our result
        return root