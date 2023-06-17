# O(n) time / O(1) space
def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def reverse(head):
    curr, prev = head, None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def isPalindrome(head):
    if head is None: return False
    mid = middle(head) # find middle
    last = reverse(mid) # reverse from mid
    curr = head
    while last: # traverse from start and end
        if last.val != curr.val:
            return False
        last = last.next
        curr = curr.next
    return True