# O(n) time / O(n) space
def changeTree(root): 
    if root is None: return
    child = 0
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data
        
    if child > root.data: 
        root.data = child
    else:
        if root.left:
            root.left.data = root.data
        if root.right:
            root.right.data = root.data
    
    changeTree(root.left)
    changeTree(root.right)
    
    total = 0
    if root.left:
        total += root.left.data
    if root.right:
        total += root.right.data
    if root.left or root.right:
        root.data = total