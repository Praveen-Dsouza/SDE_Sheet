# O(n ^ 2) time / O(1) space
def solve(nums, m):
    count = 0
    for i in range(len(nums)):
        xorSum = 0
        for j in range(i, len(nums)):
            xorSum = xorSum ^ nums[j]
            
            if xorSum == m:
                count += 1
    return count

# O(n) time / O(n) space
def solve(nums, m):
    freq ,count, xorSum = {}, 0, 0
    
    for i in range(len(nums)):
        xorSum = xorSum ^ nums[i] # take prefixXor
        y = xorSum ^ m
        # store the ocurrence of y in count
        if y in freq.keys():
            count += freq.get(y, 0)
        # prefixXor equal k increment count
        if xorSum == m:
            count += 1
        # insert if exist else increment count
        freq[xorSum] = 1 + freq.get(xorSum, 0)
    
    return count