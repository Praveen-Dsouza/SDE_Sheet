# O(n) time / O(n) space
def serialize(self, root):
    res = []
    self.preorder(root, res)
    return ','.join(res)

def preorder(self, root, res):
    if root is None: 
        res.append('N')
        return
    res.append(str(root.val))
    self.preorder(root.left, res)
    self.preorder(root.right, res)

def deserialize(self, data):
    vals = data.split(',')
    self.i = 0
    return self.dfs(vals)

def dfs(self, vals):
    if vals[self.i] == 'N':
        self.i += 1
        return None
    root = TreeNode(int(vals[self.i]))
    self.i += 1
    root.left = self.dfs(vals)
    root.right = self.dfs(vals)
    return root