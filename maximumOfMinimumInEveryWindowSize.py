# O(n^2) time / O(n) space 
def maxOfMin(arr, n):
    res = [0] * (n + 1)
    # sizes starting from size 1
    for k in range(1, n + 1):
    
        # Initialize max of min for current window size k
        maxOfMin = float('-inf')
    
        # Traverse through all window of current size k
        for i in range(n - k + 1):
    
            # Find minimum of current window
            mini = arr[i]
            for j in range(k):
                if (arr[i + j] < mini):
                    mini = arr[i + j]
    
            # Update maxOfMin if required
            if (mini > maxOfMin):
                maxOfMin = mini
    
        # return max of min for current window size
        res[k] = maxOfMin
    return res[1:]

# O(n) time / O(n) space
def maxOfMin(arr, n):
    s = [] # Used to find previous and next smaller
    # Arrays to store previous and next smaller. Initialize elements of left[] and right[]
    left = [-1] * (n + 1)
    right = [n] * (n + 1)
    for i in range(n):
        while (len(s) and arr[s[-1]] >= arr[i]):
            s.pop()
        if len(s):
            left[i] = s[-1]
        s.append(i)
    # Empty the stack as stack is going to be used for right[]
    while len(s):
        s.pop()
    # Fill elements of right[] using same logic
    for i in range(n - 1, -1, -1):
        while (len(s) and arr[s[-1]] >= arr[i]):
            s.pop()
        if len(s):
            right[i] = s[-1]
        s.append(i)
    # Create and initialize result array
    res = [0] * (n + 1)
    for i in range(n + 1):
        res[i] = 0

    # Fill result array by comparing minimums of all. Lengths computed using left[] and right[]
    for i in range(n):
    # Length of the interval
        Len = right[i] - left[i] - 1
    # arr[i] is a possible result for this Length 'Len' interval, check if arr[i] is more than max for 'Len'
        res[Len] = max(res[Len], arr[i])
    # Some entries in res[] may not be filled yet. Fill them by taking values from right side of res[]
    for i in range(n - 1, 0, -1):
        res[i] = max(res[i], res[i + 1])
    return res[1:] #returning from inde1 to n-1 
    #if u start from 0 index it will gives error