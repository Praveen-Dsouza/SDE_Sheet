# O(nlogn) time / O(1) space
def findTwoElement(arr, n): 
    arr.sort()
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            dup = arr[i]
    arr.remove(dup)

    sumArr = sum(arr)
    sumVal = n * (n + 1) // 2
    miss = sumVal - sumArr
    return dup, miss

# O(n) time / O(n) space
def findTwoElement(arr, n): 
    freq = {}
    for i in arr:
        if not i in freq:
            freq[i] = True
        else:
            dup = i
        
    for i in range(1, n + 1):
        if not i in freq:
            miss = i

    return dup, miss

# O(n) time / O(1) space
def findTwoElement(arr, n): 
    sumVal = n * (n + 1) // 2
    sumSqVal = n * (n + 1) * (2 * n + 1) // 6
        
    miss = dup = 0
    for i in range(n):
        sumVal -= arr[i]
        sumSqVal -= arr[i] * arr[i]
            
    miss = (sumVal + sumSqVal // sumVal) // 2
    dup = miss - sumVal
            
    return dup, miss

# O(n) time / O(1) space
def findTwoElement(arr, n): 
    for i in range(n):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -1 * arr[abs(arr[i])-1]
        else:
            dup = abs(arr[i])
                
    for i in range(n):
        if arr[i] > 0:
            miss = i + 1
    
    return dup, miss

# O(n) time / O(1) space
# will fail for case [1, 3, 3] it fails to identify which is x an y
def findTwoElement(arr, n):
    x = y = 0
        
    # Will hold xor of all elements and numbers from 1 to n
    xor1 = arr[0]
        
    # Get the xor of all array elements
    for i in range(1, n):
        xor1 = xor1 ^ arr[i]
            
    # XOR the previous result with numbers from 1 to n
    for i in range(1, n + 1):
        xor1 = xor1 ^ i
        
    # Will have only single set bit of xor1
    set_bit_no = xor1 & ~(xor1 - 1)
        
    # Now divide elements into two
    # sets by comparing a rightmost set
    # bit of xor1 with the bit at the same
    # position in each element. Also,
    # get XORs of two sets. The two
    # XORs are the output elements.

    for i in range(n):
        if arr[i] & set_bit_no != 0:
            # arr[i] belongs to first set
            x = x ^ arr[i]
        else:
            # arr[i] belongs to second set
            y = y ^ arr[i]
                
    for i in range(1, n + 1):
        if i & set_bit_no != 0:
            # i belongs to first set
            x = x ^ i
        else:
            # i belongs to second set
            y = y ^ i
    
    return y, x
    