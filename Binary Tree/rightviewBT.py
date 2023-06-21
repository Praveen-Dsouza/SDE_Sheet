# O(n) time / O(n) auxillary space
def rightSideView(self, root, level = 0):
    res = []
    self.rightViewUtil(root, level, res)
    return res

def rightViewUtil(self, root, level, res):
    if root is None: return
    if level == len(res):
        res.append(root.val)
    self.rightViewUtil(root.right, level + 1, res)
    self.rightViewUtil(root.left, level + 1, res)