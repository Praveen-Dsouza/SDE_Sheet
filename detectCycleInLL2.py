# O(n) time / O(n) space
def hasCycle(head):
    hs = set()
    curr = head
    while curr:
        if curr in hs:
            return curr
        hs.add(curr)
        curr = curr.next
    return curr

# O(n) time / O(1) space
def detectCycle(head):
    if head is None or head.next is None: return None
    
    slow = fast = entry = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            while slow != entry:
                entry = entry.next
                slow = slow.next
            return entry
    return None