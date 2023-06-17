# O(n! * n) time / O(2n) space (ignore utlimate permutation & auxillary space)
def permute(self, nums):
    res, ds = [], []
    freq = [False for i in range(len(nums))]
    self.permutationsHelper(nums, ds, res, freq)
    return res

def permutationsHelper(self, nums, ds, res, freq):
    if len(ds) == len(nums):
        res.append(ds[:])
    for i in range(len(nums)):
        if not freq[i]:
            freq[i] = True
            ds.append(nums[i])
            self.permutationsHelper(nums, ds, res, freq)
            ds.pop()
            freq[i] = False

# O(n! * n) time / O(1) space (ignore the result array and auxillary space)
def permute(self, nums):
    res = []
    self.permutationsHelper(0, nums, res)
    return res

def permutationsHelper(self, i, nums, res):
    if i == len(nums):
        res.append(nums[:])
    else:
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.permutationsHelper(i + 1, nums, res)
            nums[i], nums[j] = nums[j], nums[i]