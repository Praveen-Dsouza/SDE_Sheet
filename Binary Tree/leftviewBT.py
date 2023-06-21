# O(n) time / O(n) auxillary space
def leftSideView(self, root, level = 0):
    res = []
    self.leftViewUtil(root, level, res)
    return res

def leftViewUtil(self, root, level, res):
    if root is None: return
    if level == len(res):
        res.append(root.val)
    self.leftViewUtil(root.left, level + 1, res)
    self.leftViewUtil(root.right, level + 1, res)