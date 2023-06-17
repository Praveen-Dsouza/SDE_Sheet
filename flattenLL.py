# O(summation) / O(1) space
def mergeTwoLists(l1, l2):
    dummy = Node(0)
    curr = dummy
    
    while l1 and l2:
        # compare l1 and l2
        if l1.data < l2.data:
            dummy.bottom = l1
            dummy = dummy.bottom
            l1 = l1.bottom
        else:
            dummy.bottom = l2
            dummy = dummy.bottom
            l2 = l2.bottom
            
    if l1: 
        dummy.bottom = l1
    else: 
        dummy.bottom = l2
    return curr.bottom
        
def flatten(root):
    if root is None or root.next is None: return root
    # recursion for list on right
    root.next = flatten(root.next)
    # now merge
    root = mergeTwoLists(root, root.next)
    # return the root, it will inturn be merged with the left
    return root