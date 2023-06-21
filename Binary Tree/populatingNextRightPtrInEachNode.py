# O(n) time / O(n) space bfs solution
def connect(root):
    if root is None: return
    queue = [(root, 0)]
    
    while queue:
        curr, level = queue.pop(0)
            
        if len(queue) and queue[0][1] == level:
            curr.nextRight = queue[0][0]
            
        if curr.left:
            queue.append((curr.left, level+1))
        if curr.right:
            queue.append((curr.right, level+1))
    return root

# O(n) time / O(1) space bfs solution
def connect(root):
    curr, nxt = root, root.left if root else None
    
    while nxt:
        curr.left.next = curr.right
        if curr.next:
            curr.right.next = curr.next.left
            
        curr = curr.next
        if not curr:
            curr = nxt
            nxt = curr.left
    return root