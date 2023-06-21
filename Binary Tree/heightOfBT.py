# Recursive Approach
# O(n) time / O(n) auxillary space
def maxDepth(self, root):
    if root is None: return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Using Level Order Traversal
# O(n) time / O(n) space
def maxDepth(root):
    if root is None: return 0

    queue, depth = [], 0
    queue.append(root)

    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)

            if node.left: 
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        depth += 1
    return depth