# O(nlogn) time / O(1) space
def minimumPlatform(n, arr, dep):
    arr.sort()
    dep.sort()
    platNeeded, maxPlatformTaken = 1, 1
    aIdx, dIdx = 1, 0 #2nd arraival train, 1st departure train
    
    while aIdx < n and dIdx < n:
        if arr[aIdx] <= dep[dIdx]:
            platNeeded += 1
            aIdx += 1
        elif arr[aIdx] > dep[dIdx]:
            platNeeded -= 1
            dIdx += 1
        
        if platNeeded > maxPlatformTaken:
            maxPlatformTaken = platNeeded
    
    return maxPlatformTaken