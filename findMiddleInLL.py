# O(n) + O(n / 2) space
def getLen(head):
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next

    return length

def middleNode(head):
    if head:
        length = getLen(head)
        curr = head

        midIdx = length // 2
        while midIdx != 0:
            curr = curr.next
            midIdx -= 1
    return curr 

# O(n) time / O(1) space
def middleNode(head):
    slow = fast = head
    
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
        
    return slow