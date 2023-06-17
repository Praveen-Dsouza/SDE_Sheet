# O(2^n * n) + O(nlogn) time / O(2^n) * O(k) and O(n) auxillary space
def findSubsets(self, idx, nums, ds, subsets):
    subsets.append(ds[:])
    for i in range(idx, len(nums)):
        if i != idx and nums[i] == nums[i-1]: continue
        ds.append(nums[i])
        self.findSubsets(i+1, nums, ds, subsets)
        ds.pop()
    
def subsetsWithDup(self, nums):
    nums.sort()
    subsets = []
    self.findSubsets(0, nums, [], subsets)
    return subsets