import heapq
# O(nk(log(k)) time / O(k) space
def mergeKArrays(self, arr, K):
    minHeap = []
    res = []
    heapq.heapify(minHeap)
    for idx, array in enumerate(arr):
        if array:
            heapq.heappush(minHeap, (array.pop(0), idx))
    while minHeap:
            value, idx = heapq.heappop(minHeap)
            res.append(value)
            if arr[idx]:
                heapq.heappush(minHeap, (arr[idx].pop(0), idx))
    return res