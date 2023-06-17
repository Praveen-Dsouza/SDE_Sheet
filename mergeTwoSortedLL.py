# O(n1 + n2) time / O(n1 + n2) space
def mergeTwoLists(list1, list2):
    if list1 is None: return list2
    if list2 is None: return list1
    
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
            
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    
    return dummy.next

# O(n1 + n2) time / O(1) space
def mergeTwoLists(list1, list2):
    if list1 is None: return list2
    if list2 is None: return list1
    
    if list1.val > list2.val:
        list1, list2 = list2, list1
        
    res = list1
    while list1 and list2:
        temp = None
        while list1 and list1.val <= list2.val:
            temp = list1
            list1 = list1.next
        temp.next = list2
        
        list1, list2 = list2, list1
        
    return res