# O(n) time / O(n) auxillary space or if aux space ignored O(1) space
class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize

class Solution:      
    def largestBst(self, root):
        return self.largestBstHelper(root).maxSize

    def largestBstHelper(self, root):
        # an empty bst of size 0
        if root is None: return NodeValue(float('inf'), float('-inf'), 0)

        # get values from left and right subtree of current tree
        left = self.largestBstHelper(root.left)
        right = self.largestBstHelper(root.right)

        # current node is greater than max in left and smaller than min in right, it is a BST
        if left.maxNode < root.data and root.data < right.minNode:
            # It is a BST
            return NodeValue(min(root.data, left.minNode), max(root.data, right.maxNode), 1 + left.maxSize + right.maxSize)
        
        # Otherwise, return [-inf, inf] so the parent can't be valid BST
        return NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))
