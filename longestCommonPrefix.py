# O(n*m) time / O(1) space
def longestCommonPrefix(strs):
    res = ''

    # traverse all ch of first string
    for i in range(len(strs[0])): 
        # compare first str ch with remaining string
        for s in strs: 
            # no match
            if i == len(s) or s[i] != strs[0][i]: 
                return res
        res += strs[0][i]

    return res