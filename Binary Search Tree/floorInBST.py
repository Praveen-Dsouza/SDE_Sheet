# O(n) time / O(1) space
def floor(self, root, key):
    floor =  -1
    
    while root:
        # if key equal no need to go left and right
        if root.data == key:
            floor = root.data
            return floor
        
        # if key greater move right else left
        if key > root.data:
            floor = root.data
            root = root.right
        else:
            root = root.left
    return floor