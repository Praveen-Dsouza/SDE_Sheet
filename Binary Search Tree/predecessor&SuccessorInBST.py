# O(n) time / O(1) space
def findPreSuc(root, predecessor, successor, node):
    findPre(root, predecessor, node)
    findSuc(root, successor, node)

# right => update predecessor
def findPre(root, predecessor, node):
    while root:
        if node >= root.key:
            root = root.left
        else:
            predecessor = root
            root = root.right
    return predecessor
        
# left => update successor
def findSuc(root, successor, node):
    while root:
        if node <= root.key:
            root = root.right
        else:
            successor = root
            root = root.left
    return successor