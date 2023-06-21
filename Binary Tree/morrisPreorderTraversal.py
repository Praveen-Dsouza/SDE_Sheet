# O(n) time / O(1) space
def preorderTraversal(root):
    curr, res = root, []
    while curr:
        # case 1
        if curr.left is None:
            res.append(curr.val)
            curr = curr.right
        # case 2
        else:
            prev = curr.left
            # right exists and thread does not point to himself(curr)
            while prev.right and prev.right != curr:
                prev = prev.right

            if prev.right is None:
                prev.right = curr # form thread
                res.append(curr.val)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return res