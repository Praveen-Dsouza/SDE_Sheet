# O(n) time / O(1) space
def rotateRight(head, k):
    if head is None or head.next is None or k == 0: return head
    
    curr, length = head, 1
    # Calculate length
    while curr.next:
        length += 1
        curr = curr.next

    # link last node next to head
    curr.next = head
    
    # Traverse through k
    k = k % length
    k = length - k # remove for rotate from left
    while k:
        k -= 1
        curr = curr.next
        
    # break the link
    head = curr.next
    curr.next = None
    return head