# Iterative: O(n) time / O(1) space
def reverseList(head):
    if not head.next: return head
    
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# Recursive: O(n) time / O(n) space
def reverseList(head):
    if not head: return None
    
    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    
    head.next = None
    return newHead