# O(n^2) time / O(1) space
def inversionCount(arr, n):
    invCount = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                invCount += 1
    return invCount

# O(nlogn) time / O(n) space
def merge(arr, low, mid, high):
        n1 = mid - low + 1
        n2 = high - mid

        # Left sorted array
        left = []
        for i in range(n1):
            left.append(arr[low + i]) 

        # Right sorted array
        right = []
        for j in range(n2):
            right.append(arr[mid + 1 + j])

        # Merging two sorted array
        l, r, k = 0, 0, low
        invCount = 0
        while l < n1 and r < n2:
            if left[l] <= right[r]:
                arr[k] = left[l]
                l += 1
            else:
                arr[k] = right[r]
                r +=1
                invCount = invCount + (n1 - l)
            k +=1
        while l < n1:
            arr[k] = left[l]
            l += 1
            k +=1
        while r < n2:
            arr[k] = right[r]
            r +=1
            k +=1
        return invCount
        
def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        l = mergeSort(arr, low, mid)
        r = mergeSort(arr, mid+1, high)
        m = merge(arr, low, mid, high)
        
        return l + r + m
    return 0
    
def inversionCount(arr, n):
    return mergeSort(arr, 0, n - 1)