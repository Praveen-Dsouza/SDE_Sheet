import heapq
#  O(n^2 * log(n)) time / O(n) space
def solve(self, A, B, C):
    minHeap = []
    heapLen = 0

    for a in A:
        for b in B:
            heapq.heappush(minHeap, a+b)
            heapLen += 1
            if heapLen > C:
                heapq.heappop(minHeap)
                heapLen -= 1
    res = []
    while minHeap:
        res.append(heapq.heappop(minHeap))
    return res[::-1]

# O(nlogn) time / O(n) space
def solve(self, A, B, C):
        A.sort(reverse=True)
        B.sort(reverse=True)
        n = len(A)
        pq = [(-(A[0] + B[0]), (0, 0))]
        combinationSumIdx = set()
        combinationSumIdx.add((0, 0))
        res = []
        
        while C > 0:
            top = heapq.heappop(pq)
            res.append(top[0] * -1)
            i = top[1][0]
            j = top[1][1]
            if i < n and j < n:
                if (i+1,j) not in combinationSumIdx:
                    heapq.heappush(pq, (-(A[i+1] + B[j]), (i+1, j)))
                    combinationSumIdx.add((i+1, j))
                if (i,j+1) not in combinationSumIdx:
                    heapq.heappush(pq, (-(A[i] + B[j+1]), (i, j+1)))
                    combinationSumIdx.add((i, j+1))
            C -= 1
        return res

