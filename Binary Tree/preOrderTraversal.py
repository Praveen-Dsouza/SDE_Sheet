# RECURSIVE APPROACH:
# O(n) time / O(n) auxillary space
def preorderTraversal(self, root):
    if root is None: return []
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# ITERATIVE APPROACH
def preorderTraversal(root):
    if root is None: return []

    st, res = [], []
    st.append(root)
    while st:
        root = st[-1]
        st.pop()
        res.append(root.val)
        if root.right: st.append(root.right)
        if root.left: st.append(root.left)
    return res