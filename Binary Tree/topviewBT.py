# O(nlogn) time / O(n) space
def topView(root):
    map, queue, res, hd = {}, [], [], 0
    if root is None: return  

    queue.append((root, 0))
    while queue:
        curr, hd = queue.pop(0)
        if hd not in map.keys():
            map[hd] = [curr.data]

        if curr.left:
            queue.append((curr.left, hd-1))

        if curr.right:
            queue.append((curr.right, hd+1))

    for i in sorted(map):
        res += map[i]
    return res