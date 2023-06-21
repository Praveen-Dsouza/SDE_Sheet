# RECURSIVE APPROACH:
# O(n) time / O(n) space => O(n) auxillary space
def inorderTraversal(self, root):
    if root is None: return []
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# ITERATIVE APPROACH
def inorderTraversal(root):
    if root is None: return []

    st, res, curr = [], [], root
    while True:
        if curr:
            st.append(curr)
            curr = curr.left
        else:
            if st == []: break
            curr = st[-1]
            st.pop()
            res.append(curr.val)
            curr = curr.right
    return res