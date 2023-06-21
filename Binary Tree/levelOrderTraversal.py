# O(n) time / O(n) space
def levelOrder(root):
    if root is None: return
    queue, res = [], []
    queue.append(root)
    while queue:
        levelNodes, levelSize = [], len(queue)
        for i in range(levelSize):
            rootNode = queue.pop(0)
            levelNodes.append(rootNode.val)
            if rootNode.left:
                queue.append(rootNode.left)
            if rootNode.right:
                queue.append(rootNode.right)
        res.append(levelNodes)
    return res