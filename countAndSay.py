# O(2^n) time / O(2^n-1) space
def countAndSay(n):
    if n == 1: return '1'
    if n == 2: return '11'
    s = '11'
    for i in range(3, n+1):
        currStr = ''
        s += '$' # check last value
        count = 1
        # string not match to prevStr
        for j in range(1, len(s)):
            if s[j] != s[j-1]:
                currStr += str(count) # str count
                currStr += s[j-1]     # str
                count = 1
            else: # match
                count += 1
        s = currStr
    return s