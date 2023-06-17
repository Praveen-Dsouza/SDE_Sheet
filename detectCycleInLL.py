# O(n) time / O(n) space
def hasCycle(head):
    hs = set()
    curr = head
    while curr:
        if curr in hs:
            return True
        hs.add(curr)
        curr = curr.next
    return False

# O(n) time / O(1) space
def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False