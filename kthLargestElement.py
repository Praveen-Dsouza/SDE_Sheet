# O(nlogn) time / O(1) space
def findKthLargest(self, nums, k):
    nums.sort()
    return nums[len(nums)-k]

# O(k+(n-k)*log(k)), n = size of array time / O(k) space
import heapq
def findKthLargest(self, nums, k):
    nums=list(map(lambda x:-x,nums))  
    heapq.heapify(nums)
    for i in range(k-1):
        heapq.heappop(nums)  #Pop minimum from the list
    return -heapq.heappop(nums)

# average: O(n) / worst: O(n^2) time / O(1) space
def findKthLargest(self, nums, k):
    k = len(nums) - k
    return self.quickSelect(nums, k, 0, len(nums)-1)

def quickSelect(self, nums, k, l, r):
    pivot, p = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
    nums[p], nums[r] = nums[r], nums[p]

    if p > k:   return self.quickSelect(nums, k, l, p-1)
    elif p < k: return self.quickSelect(nums, k, p+1, r)
    else:       return nums[p]
    