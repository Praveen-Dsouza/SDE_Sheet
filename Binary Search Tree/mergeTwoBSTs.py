# O(n + m) time / O(n + m) space
def inorder(root, inOrder):
    if root is None: return
    inorder(root.left, inOrder)
    inOrder.append(root.data)
    inorder(root.right, inOrder)
    
def mergeTwoSortedArrays(arr1, arr2):
    i, j, res = 0, 0, []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res

def inorderToBST(s, e, inOrder):
    if s > e: return None
    mid = (s + e) // 2
    root = TreeNode(inOrder[mid])
    root.left = inorderToBST(s, mid-1, inOrder)
    root.right = inorderToBST(mid+1, e, inOrder)
    return root

def mergeBST(root1, root2):
	# store inorder
    bst1, bst2 = [], []
    inorder(root1, bst1)
    inorder(root2, bst2)
    
    # merge two sorted arrays
    mergeArray = mergeTwoSortedArrays(bst1, bst2)

    # Convert inorder or sorted array to bst
    s, e = 0, len(mergeArray)-1
    return inorderToBST(s, e, mergeArray)