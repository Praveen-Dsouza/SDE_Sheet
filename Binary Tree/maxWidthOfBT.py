def widthOfBinaryTree(root):
    queue, width = [[root, 0]], 0

    if root is None: return 0

    while queue:
        firstIdx, lastIdx, size, mini = 0, 0, len(queue), queue[0][1]
        
        for i in range(size):
            node, currIdx = queue.pop(0)
            currIdx = currIdx - mini
            if i == 0: firstIdx = currIdx
            if i == size-1: lastIdx = currIdx

            if node.left: 
                queue.append([node.left, 2*currIdx + 1])
            if node.right: 
                queue.append([node.right, 2*currIdx + 2])

        width = max(width, lastIdx - firstIdx + 1)
    return width