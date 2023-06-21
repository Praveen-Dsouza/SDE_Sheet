# MEDIUM GFG
# O(nlogn) time / O(1) space
def verticalOrder(root): 
    queue, res, map, hd = [], [], {}, 0
    
    if root is None: return res
    
    queue.append([root, hd])
    while queue:
        temp = queue.pop(0)
        node, hd = temp[0], temp[1]
        
        if hd in map:
            map[hd].append(node.data)
        else:
            map[hd] = [node.data]

        if node.left:
            queue.append([node.left, hd-1])
        if node.right:
            queue.append([node.right, hd+1])
        
    for key in sorted(map):
        res += map[key]
        
    return res

# HARD LEETCODE
# O(nlogn) time / O(n) space
def verticalTraversal(root):
        queue, res, map = [[0, 0, root]], [], {}

        if root is None: return res

        while queue:
            v, level, node = queue.pop(0)

            if v in map:
                map[v].append([level, node.val])
            else:
                map[v]=[[level, node.val]]

            if node.left:
                queue.append((v-1, level+1, node.left))
            if node.right:
                queue.append([v+1, level+1, node.right])
                
        for i in sorted(map.keys()):
            col = [x[1] for x in sorted(map[i])]
            res.append(col)
        return res