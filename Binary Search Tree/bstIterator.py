# O(1) time / O(h) space
# @param root, a binary search tree's root node
def __init__(self, root):
    self.stack = []
    self.pushAll(root)

# @return an integer, the next smallest number
def next(self):
    curr = self.stack.pop()
    self.pushAll(curr.right)
    return curr.val

# @return a boolean, whether we have a next smallest number
def hasNext(self):
    return self.stack

def pushAll(self, root):
    while root:
        self.stack.append(root)
        root = root.left