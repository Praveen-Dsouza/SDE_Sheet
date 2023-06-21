# O(n) time / O(n) space
def findTarget(self, root, k):
    self.inOrder  = []
    self.inorder(root)
    l, r = 0, len(self.inOrder)-1
    while(l < r):
        target = self.inOrder[l] + self.inOrder[r]
        if target == k: return True
        elif target > k: r -= 1
        else: l += 1
    return False

def inorder(self, root):
    if root is None: return None
    self.inorder(root.left)
    self.inOrder.append(root.val)
    self.inorder(root.right)

# O(n) time / O(h) space
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root, isReverse):
        self.stack = []
        # reverse -> True -> before
        # reverse -> False -> next
        self.reverse = True
        self.reverse = isReverse
        self.pushAll(root)

    # @return an integer, the next smallest number
    def next(self):
        curr = self.stack.pop()
        if self.reverse == False: self.pushAll(curr.right)
        else: self.pushAll(curr.left)
        return curr.val

    def pushAll(self, root):
        while root:
            self.stack.append(root)
            if self.reverse == True:
                root = root.right
            else:
                root = root.left

class Solution:
    def findTarget(self, root, k):
        if root is None: return False
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)
        i, j = l.next(), r.next() # before

        while i < j:
            target = i + j
            if target == k: return True
            elif target < k: i = l.next()
            else: j = r.next()
        return False