def zigzagLevelOrder(root):
    if root is None: return None
    queue, res, leftToRight = [], [], True
    queue.append(root)
    
    while queue:
        levelNodes, size = [], len(queue)
        for _ in range(size):
            node = queue.pop(0)
            levelNodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if leftToRight:
            res.append(levelNodes)
        else:
            res.append(levelNodes[::-1])
        leftToRight = not leftToRight
    return res