# O(n) time / O(1) space
def compareVersion(version1, version2):
    # convert into list of string 1.001.2 => ['1', '001', '2']
    version1, version2 = version1.split('.'), version2.split('.')

    # iterate through max length if version list length
    for i in range(max(len(version1), len(version2))):
        # int converts 001 => 1
        v1 = int(version1[i]) if i < len(version1) else 0
        v2 = int(version2[i]) if i < len(version2) else 0
        
        # compare
        if v1 > v2: return 1
        elif v1 < v2: return -1

    return 0