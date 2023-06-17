# O(n) time / O(1) space
def merge(nums1, m, nums2, n):
    res = [0 for i in range(m + n)]
    
    i = j = k = 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            res[k] = nums1[i]
            i += 1
        else:
            res[k] = nums2[j]
            j += 1
        k += 1
    while i < m:
        res[k] = nums1[i]
        i += 1
        k += 1
    while j < n:
        res[k] = nums2[j]
        j += 1
        k += 1
        
    return res

# O(n) time / O(1) space
def merge(nums1, m, nums2, n):
    # last index of nums1
    last = m + n - 1
    
    # merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    
    # fill nums1 with leftover nums2 elements
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1