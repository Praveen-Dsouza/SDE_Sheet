# O(2^n * k) time / O(k * x) space
def combinationSum2(self, candidates, target):
    result = []
    candidates.sort()
    self.dfs(candidates, target, [], result)
    return result

def dfs(self, candidates, target, path, result):
    if target == 0:
        result.append(path)
        return
    for i in range(len(candidates)):
        if candidates[i] > target:
            continue
            
        if i >= 1 and candidates[i] == candidates[i-1]:
            continue
        
        self.dfs(candidates[i+1:], target - candidates[i], path + [candidates[i]], result)