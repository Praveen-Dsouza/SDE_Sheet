def getTreeTraversal(root):
    preOrd, inOrd, postOrd, stack = [], [], [], [[root, 1]]

    if root is None: return []
    while stack:
        n = stack.pop()
        # Preorder Traversal
        if n[1] == 1:
            preOrd.append(n[0].val)
            n[1] += 1
            stack.append(n)
            if n[0].left:
                stack.append([n[0].left, 1])

        # Inorder Traversal
        elif n[1] == 2:
            inOrd.append(n[0].val)
            n[1] += 1
            stack.append(n)
            if n[0].right:
                stack.append([n[0].right, 1])

        # Postorder Traversal
        else:
            postOrd.append(n[0].val)
    return inOrd, preOrd, postOrd