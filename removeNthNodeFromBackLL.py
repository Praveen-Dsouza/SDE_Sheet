# O(n) time / O(1) space
def getLength(head):
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    return length
    
# O(2n) time / O(1) space
def removeNthFromEnd(head, n): 
    curr = head
    totalLength = getLength(curr)
    
    if n == totalLength: return head.next
    
    if totalLength == 1: return None
    
    length = totalLength - n
    counter = 1
    while curr and counter < length:
        curr = curr.next
        counter += 1
    curr.next = curr.next.next        
    return head

def removeNthFromEnd(head, n):     
    dummy = ListNode()
    dummy.next = head
    fast = slow = dummy
    
    for i in range(n):
        fast = fast.next
        
    while fast.next:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    return dummy.next