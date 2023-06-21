# RECURSIVE APPROACH:
# O(n) time / O(n) auxillary space
def postorderTraversal(self, root):
    if root is None: return []
    return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

# ITERATIVE APPROACH
def postorderTraversal(root):
    if root is None: return []

    res, st = [], [(root, False)]
    while st:
        node, visited = st.pop()
        if node:
            if visited:
                # add to result if visited
                res.append(node.val)
            else:
                # post-order
                st.append((node, True))
                st.append((node.right, False))
                st.append((node.left, False))

    return res