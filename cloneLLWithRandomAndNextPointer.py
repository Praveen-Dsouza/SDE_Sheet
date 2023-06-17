# O(n) time / O(n) space
def copyRandomList(head):
    oldToCopy = { None: None }
    
    curr = head
    while curr:
        copy = Node(curr.val)
        oldToCopy[curr] = copy
        curr = curr.next
        
    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next
        
    return oldToCopy[head]

# O(n) time / O(1) space
def copyRandomList(head):
    # Inserting new Nodes between old LinkedList 
    curr = head
    while curr:
        temp = curr.next
        curr.next = Node(curr.val)
        curr.next.next = temp
        curr = temp
    curr = head
    
    # Setting random ptrs of new Nodes
    while curr:
        if curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
        curr = curr.next.next
    
    # seprating both LinkedList
    orig = head
    copy = head.next if head else None
    temp = copy
    while orig:
        orig.next = orig.next.next
        if copy.next:
            copy.next = copy.next.next
        else:
            copy.next = None
        orig = orig.next
        copy = copy.next
    return temp

