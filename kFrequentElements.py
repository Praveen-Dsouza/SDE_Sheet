# O(dlog(d)) time / O(d) space
def topKFrequent(nums, k):
    freq = {}
    for num in nums:	
        freq[num] = freq.get(num, 0) + 1
    result = sorted(freq, key=freq.get, reverse=True)
    return result[:k]

# O(klog(d) + dlog(d)) time / O(d) space
import heapq
def topKFrequent(nums, k):
    freq = {}
    for num in nums:	
        freq[num] = freq.get(num, 0) + 1

    maxHeap = []
    for key in freq:
        heapq.heappush(maxHeap, (-1 * freq[key], key))
    
    res = []
    for i in range(k):
        value = heapq.heappop(maxHeap)[1]
        res.append(value)
    
    return res

# O(n) time / O(n) space
def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:	
        count[num] = count.get(num, 0) + 1
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res