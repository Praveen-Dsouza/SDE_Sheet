# O(2^t * k) time / O(k * n) space
def combinationSum(self, candidates, target):
    result = []
    self.dfs(candidates, target, [], result)
    return result

def dfs(self,candidates, target, path, result):
    if target == 0:
        result.append(path)
        return
    for i in range(len(candidates)):
        if candidates[i] > target:
            continue
        self.dfs(candidates[i:], target - candidates[i], path + [candidates[i]], result)