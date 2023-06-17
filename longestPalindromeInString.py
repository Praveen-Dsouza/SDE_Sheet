# odd length string                             |even length string
#     lr = i,i both point to same mid element   |  l r = i, i+1
# b a b a d                                     |c b b d
#_____|_____                                    ___|_|___
# expand out from mid and check each element in string

# O(n^2) time / O(1) space
def longestPalindrome(S):
    res, resLen = "", 0
    
    # odd length
    for i in range(len(S)):
        l, r = i, i
        while l >= 0 and r < len(S) and S[l] == S[r]:
            if (r - l + 1) > resLen:
                res = S[l: r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
        
        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(S) and S[l] == S[r]:
            if (r - l + 1) > resLen:
                res = S[l: r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res