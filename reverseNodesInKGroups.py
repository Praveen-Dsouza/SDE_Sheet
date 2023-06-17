# O(n) time / O(1) time
def reverseKGroup(head, k):
    if head is None or k == 1: return head
    
    dummy = ListNode(0)
    dummy.next = head
    curr = nextNode = prev = dummy
    count = 0
    
    while curr:
        curr = curr.next
        count += 1
        
    while count > k:
        curr = prev.next
        nextNode = curr.next
        
        for i in range(1, k):
            curr.next = nextNode.next
            nextNode.next = prev.next
            prev.next = nextNode
            nextNode = curr.next
        
        prev = curr
        count -= k
        
    return dummy.next