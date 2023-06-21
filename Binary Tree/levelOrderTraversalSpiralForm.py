# O(n) time / O(n) space
def findSpiral(root):
    if root is None: return []
    s1, s2, res = [], [], []
    s1.append(root)
    
    while len(s1) or len(s2):
        while len(s1):
            node = s1[-1]
            s1.pop()
            res.append(node.data)
            if node.right:
                s2.append(node.right)
            if node.left:
                s2.append(node.left)
    
        while len(s2):
            node = s2[-1]
            s2.pop()
            res.append(node.data)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
                
    return res