# O(m * n) time / O(1) space
def getIntersectionNode(headA, headB):
    while headB:
        d1 = headA
        while d1:
            # if both Nodes are same
            if d1 == headB:
                return headB
            d1 = d1.next
        headB = headB.next
    # intersection is not present between the lists
    return None

# O(m + n) time / O(n) space
def getIntersectionNode(headA, headB):
    hs = set()
    
    while headA:
        hs.add(headA)
        headA = headA.next
    while headB:
        if headB in hs:
            return headB
        headB = headB.next
    return None

# O(2m) time / O(1) space
def getIntersectionNode(headA, headB):
	c1, c2 = getCount(headA), getCount(headB) # find len of l1 and l2

	if c1 > c2:
		d = c1 - c2
		return intersectionNodeTraverse(d, headA, headB)
	else:
		d = c2 - c1
		return intersectionNodeTraverse(d,headB,headA)

def intersectionNodeTraverse(d, headA, headB):
	curr1, curr2 = headA, headB
	
	for i in range(d):
		if curr1 is None:
			return None
		curr1 = curr1.next
	
	while curr1 and curr2:
		if curr1 is curr2:
			return curr1.val # or curr2.val (the val would be same)
	
		curr1 = curr1.next
		curr2 = curr2.next
	return None # no intersection point

def getCount(node):
	curr, count = node, 0
	while curr:
		count += 1
		curr = curr.next
	return count

# O(2m) time / O(1) space
def getIntersectionNode(headA, headB):
    if headA is None or headB is None: return None
    currH1, currH2 = headA, headB
    
    # if currH1 and currH2 have different len, then will stop the loop after 2nd itr
    while currH1 != currH2:
        # reset pointer to other linked list head if None
        currH1 = headB if currH1 is None else currH1.next
        currH2 = headA if currH2 is None else currH2.next
        
    return currH1