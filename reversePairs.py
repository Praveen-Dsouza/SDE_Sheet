# O(n ^ 2) time / O(1) space
def reversePairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > 2 * nums[j]:
                count += 1
    return count

# O(nlogn) time / O(1) space
def reversePairs(nums):
    return mergeSort(nums, 0, len(nums) - 1)

def merge(nums, low, mid, high):
    count = 0 # store total pairs
    j = mid + 1 # start point of right half of array
    
    for i in range(low, mid + 1): # itr left half
        while j <= high and nums[i] > 2 * nums[j]: # move j till out of bound
            j += 1
        count += j - (mid + 1) # count pairs for the ith ele as of now 
            
    # merge
    left, right, temp = low, mid + 1, []
    
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1    

    while left <= mid:
        temp.append(nums[left])
        left += 1
    while right <= high:
        temp.append(nums[right])
        right += 1

    # copy back temp to nums array
    for i in range(low, high + 1):
        nums[i] = temp[i - low]
    return count

def mergeSort(nums, left, right):
    if left >= right: return 0
    mid = (left + right) // 2
    inv = mergeSort(nums, left, mid) # left rec
    inv += mergeSort(nums, mid + 1, right) # right rec
    # compute number of pairs and merge left and right sorted array.
    inv += merge(nums, left, mid, right) 
    return inv