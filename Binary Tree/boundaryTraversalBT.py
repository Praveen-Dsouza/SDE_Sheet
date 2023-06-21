# O(n) time / O(n) space
def printBoundaryView(self, root):
    res = [root.data]
    if root.left is None and root.right is None:
        return res
    
    leftBNodes = []
    left = root.left
    while left:
        if left.left is None and left.right is None: # Excluding Leaf Node
            break
        leftBNodes.append(left.data)
        if left.left:
            left = left.left
        else:
            left = left.right
    
    leafNodes = []
    self.inorder(root, leafNodes)   #Get all leaf Nodes
    
    rightBNodes = []
    right = root.right
    while right:
        if right.left is None and right.right is None: # Excluding Leaf Node
            break
        rightBNodes.append(right.data)
        if right.right:
            right = right.right
        else:
            right = right.left
        
    res.extend(leftBNodes)
    res.extend(leafNodes)
    res.extend(rightBNodes[::-1])
    return res
    

def inorder(self, root, lst):
    if root:
        if root.left is None and root.right is None: # Including only leaf nodes
            lst.append(root.data)
        self.dfs(root.left, lst)
        self.dfs(root.right, lst)