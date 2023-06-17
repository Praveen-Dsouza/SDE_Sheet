# O(2^n * n) time / O(1) space
def subsetSums(arr, N):
    total = 1 << N # There are total 2^n subsets
    
    # Consider all numbers from 0 to 2^n - 1
    subsetSum = []
    for i in range(total):
        Sum = 0
        # Consider binary representation of
        # current i to decide which elements to pick.
        for j in range(N):
            if ((i & (1 << j)) != 0):
                Sum += arr[j]
    
        subsetSum.append(Sum)
    return subsetSum
        
# O(2^n + 2^nlogn) time / O(n) space
def solve(self, idx, currSum, arr, N, subsetSum):
    if idx == N: 
        subsetSum.append(currSum)
        return
    self.solve(idx + 1, currSum + arr[idx], arr, N, subsetSum)
    self.solve(idx + 1, currSum, arr, N, subsetSum)

def subsetSums(self, arr, N):
    subsetSum = []
    self.solve(0, 0, arr, N, subsetSum)
    subsetSum.sort()
    return subsetSum