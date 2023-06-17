def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    
    while l1 or l2 or carry != 0:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        # new digit
        sumVal = v1 + v2 + carry # node val
        newVal = sumVal % 10
        carry = sumVal // 10
        curr.next = ListNode(newVal)
        
        # update pointers
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next